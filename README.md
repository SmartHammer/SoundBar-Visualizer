# SoundTouch Visualization using PySide2 and QML

## [Install PySide2 on RaspberryPi OS](https://forum.qt.io/topic/112813/installing-pyside2-on-raspberry-pi/6)
``` bash
apt-get install -f \
                    python3-pyside2.qt3dcore \
                    python3-pyside2.qt3dinput \
                    python3-pyside2.qt3dlogic \
                    python3-pyside2.qt3drender \
                    python3-pyside2.qtcharts \
                    python3-pyside2.qtconcurrent \
                    python3-pyside2.qtcore \
                    python3-pyside2.qtgui \
                    python3-pyside2.qthelp \
                    python3-pyside2.qtlocation \
                    python3-pyside2.qtmultimedia \
                    python3-pyside2.qtmultimediawidgets \
                    python3-pyside2.qtnetwork \
                    python3-pyside2.qtopengl \
                    python3-pyside2.qtpositioning \
                    python3-pyside2.qtprintsupport \
                    python3-pyside2.qtqml \
                    python3-pyside2.qtquick \
                    python3-pyside2.qtquickwidgets \
                    python3-pyside2.qtscript \
                    python3-pyside2.qtscripttools \
                    python3-pyside2.qtsensors \
                    python3-pyside2.qtsql \
                    python3-pyside2.qtsvg \
                    python3-pyside2.qttest \
                    python3-pyside2.qttexttospeech \
                    python3-pyside2.qtuitools \
                    python3-pyside2.qtwebchannel \
                    python3-pyside2.qtwebsockets \
                    python3-pyside2.qtwidgets \
                    python3-pyside2.qtx11extras \
                    python3-pyside2.qtxml \
                    python3-pyside2.qtxmlpatterns
```

## File structure
```
software
├── assets
│   ├── PLASMA-ColorCycling.gif
│   ├── i-feel-empty.jpg
│   ├── search animation.gif
│   ├── shazam-blue.png
│   ├── tv-icon.png
│   └── tv.jpg
├── components
│   ├── Headline.qml
│   ├── MediaPlayer.qml
│   ├── ProductTV.qml
│   ├── PropertyViewer.qml
│   ├── ShazamResult.qml
│   ├── ShazamSearching.qml
│   ├── SongViewer.qml
│   ├── Standby.qml
│   ├── TextWithShadow.qml
│   └── WebRadio.qml
├── controller
│   ├── Application.py
│   ├── ViewManager.py
│   └── ViewManagerBase.py
├── fsm
│   ├── States.py
│   └── ViewContext.py
├── helper
│   ├── MicrophoneListener.py
│   ├── NetworkChecker.py
│   └── singletondecorator.py
├── main.py
├── main.pyproject
├── main.pyproject.user
├── models
│   ├── ShazamBackend.py
│   ├── ShazamSearchState.py
│   ├── SoundTouchBackend.py
│   ├── SoundTouchDeviceSearcher.py
│   ├── SoundTouchSearchBackend.py
│   ├── selected.pickle
│   ├── shazam-this.mp3
│   └── soundtouch.dump
├── requirements.txt
├── run.sh
├── viewmodels
│   ├── BaseVM.py
│   ├── Header.py
│   ├── MainWindowVM.py
│   ├── ShazamVM.py
│   ├── Song.py
│   ├── SoundTouchSearchVM.py
│   ├── SoundTouchVM.py
│   ├── States.py
│   └── soundtouch.json
└── views
    ├── BaseView.py
    ├── MainWindow.qml
    ├── ShazamView.qml
    ├── ShutdownView.qml
    ├── SoundTouchSearchView.qml
    └── SoundTouchView.qml
```
