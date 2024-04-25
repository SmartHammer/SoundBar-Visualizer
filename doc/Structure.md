## Application

The application contains a main.py

This file just creates an object of type __*Application*__

### The application class

The application class is located in the folder __*controller*__

It is derived from [QGuiApplication](https://doc.qt.io/qt-5/qguiapplication.html)

It creates 
- a [QQmlApplicationEngine](https://doc.qt.io/qt-5/qqmlapplicationengine.html),
- a ViewContext and
- a ViewManager

And finally starts the QApplication event loop

### The view context class

The view context class is located in the folder __*fsm*__

It contains 
- an dictionary for the main window creation and 
- a dictionary for the view creation

Each entry contains
- the path to the corresponding QML file
- the name of the context (viewModel within the QML) and
- a lambda expression for the creation of the viewModel

The entries for the views have a key that represents a state

### The view mananger class

The view manager class is located in the folder __*controller*__

It is derived from __*ViewManagerBase*__

The view manager creates the main window according to the __*ViewContext*__

It also allows to switch states which lead to creation of views accoding to the __*ViewContext*__

### The views


### The view models

