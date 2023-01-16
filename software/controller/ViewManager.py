# This Python file uses the following encoding: utf-8
from os import path
from PySide2.QtCore import QObject, QUrl
from PySide2.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide2.QtQuick import QQuickItem
from .ViewManagerBase import ViewManagerBase
from fsm.States import States
from fsm.ViewContext import ViewContext
import logging


class ViewManager(ViewManagerBase):
    def __init__(self,
                 rootPath: str,
                 engine: QQmlApplicationEngine,
                 viewContext: ViewContext,
                 parent=None):
        super().__init__(rootPath, parent)
        self._viewModel = None
        self._state = States.Options.Undefined
        self._engine: QQmlApplicationEngine = engine
        self._viewContext = viewContext
        self._mainWindow()
        self._switchState(States.getInitialState())

    def switchState(self, state: States.Options):
        self._switchState(state)

    def _mainWindow(self):
        _entry = self._viewContext.getMainContent()
        _localPath = path.join(self._rootPath, _entry["qml"])
        _context: QObject = _entry["vm"](self)
        _contextName: str = _entry["contextName"]
        self._engine.load(_localPath)
        self._window = self._engine.rootObjects()[0]
        self._window.setProperty(_contextName, _context)
        self._content: QQuickItem = self._window.findChild(QQuickItem, "content")

    def _switchState(self, state: States.Options):
        logging.info("switch state from %s -> %s" % (self._state.name, state.name))
        self._state = state
        _entry = self._viewContext.getStateContent(self._state)
        localPath = path.join(self._rootPath, _entry["qml"])
        context: QObject = _entry["vm"](self)
        if not context:
            logging.warning("switch state context not created")
        self._loadView(localPath, context, _entry["contextName"])

    def _deletePreviousView(self):
        _children = self._content.childItems()
        if len(_children) > 0:
            _oldView = _children[0]
            if self._viewModel:
                self._viewModel.deactivating()
            _oldView.setParent(None)
            _oldView.setParentItem(None)
            _oldView.deleteLater()
            if self._viewModel:
                self._viewModel.deactivated()
                self._viewModel = None

    def _loadView(self, localPath, context, contextName):
        if context:
            context.activating()
        component = QQmlComponent(self._engine)
        component.loadUrl(QUrl.fromLocalFile(localPath))
        _view = component.create()
        if _view:
            self._deletePreviousView()
            _view.setParentItem(self._content)
            self._viewModel = context
            _view.setProperty(contextName, context)
            context.activated()
        else:
            if component.isError():
                logText = "loadView( %s ) failed:\n" % localPath
                for error in component.errors():
                    logText += "\t %s" % error.toString()
                logging.error(logText)
            else:
                logging.error("loadView( %s ) failed: %i" % (localPath, component.status()))
