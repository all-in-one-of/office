# coding: utf-8

import os

soft_name = os.getenv('SOFT_NAME')
qtweb = True
pyside = None

# Maya    PySide2.QtWebKitWidgets.QWebView
# Houdini PySide2.QtWebEngineWidgets.QWebEngineView

if soft_name == 'houdini':
    import hou

    try:
        pyside = os.environ['HOUDINI_QT_PREFERRED_BINDING']
        parent = hou.qt.mainWindow()
    except KeyError:
        parent = hou.ui.mainQtWindow()
        pyside = 'PySide'

    if pyside == 'PySide2':
        from PySide2 import QtGui, QtCore, QtWidgets
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
        from PySide2.QtWebEngineWidgets import QWebEngineView

    elif pyside == 'PySide':
        from PySide import QtGui, QtCore
        from PySide.QtGui import *
        from PySide.QtCore import *
        from PySide.QtWebKit import QWebView

else:
    try:
        from PySide import QtGui, QtCore
        from PySide.QtGui import *
        from PySide.QtCore import *

    except ImportError:
        from PySide2 import QtGui, QtCore, QtWidgets
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *

    if soft_name == 'maya':
        try:
            from PySide.QtWebKit import QWebView
        except ImportError:
            from PySide2.QtWebKitWidgets import QWebView

        from pymel.core import *
        parent = ui.PyUI('MayaWindow').asQtObject()  # Maya as QT-object

    if soft_name == 'nuke':
        parent = None
        qtweb = False
        print 'nuke | import QtWeb: ' + str(qtweb)

try:
    print 'PyQt: ', QtCore.__version__
except:
    print 'PyQt:', pyside