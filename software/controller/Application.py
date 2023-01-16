# This Python file uses the following encoding: utf-8

import sys
import logging
import logging.handlers
from PySide2.QtGui import QGuiApplication, QCursor
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQml import qmlRegisterType
from PySide2.QtCore import Qt
from viewmodels.States import SoundtouchState, ShazamState
from fsm.ViewContext import ViewContext
from .ViewManager import ViewManager
from views.BaseView import BaseView
from subprocess import run


qmlRegisterType(BaseView, 'Views', 1, 0, 'BaseView')
qmlRegisterType(SoundtouchState, 'States', 1, 0, 'SoundtouchState')
qmlRegisterType(ShazamState, 'States', 1, 0, 'ShazamState')


class Application (QGuiApplication):
    def __init__(self, argv, rootPath):
        super().__init__(argv)
        run('vcgencmd display_power 1', shell=True)
        self._setupLogging()
        logging.info("Enter application")
        QGuiApplication.setOverrideCursor(QCursor(Qt.BlankCursor))
        self._rootPath = rootPath
        self._engine = QQmlApplicationEngine()
        self._viewContext = ViewContext()
        self._viewManager = ViewManager(self._rootPath,
                                        self._engine,
                                        self._viewContext,
                                        self)
        if not self._engine.rootObjects():
            _exit_code = -1
        else:
            _exit_code = super().exec_()
        self._cleanupLogging()
        run('vcgencmd display_power 1', shell=True)
        sys.exit(_exit_code)

    def _setupLogging(self):
        self._logHandlers = [
            logging.StreamHandler(sys.stderr),
            logging.handlers.RotatingFileHandler(
                "/tmp/" + __name__ + ".log", maxBytes=(1048576*5), backupCount=7
            )
        ]
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(module)s::%(funcName)s#%(lineno)d: %(message)s",
            handlers=self._logHandlers
        )

    def _cleanupLogging(self):
        for _handler in self._logHandlers:
            logging.getLogger().removeHandler(_handler)
            _handler.close()
        logging.shutdown()
