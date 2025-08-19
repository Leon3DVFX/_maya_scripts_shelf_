#full_screen.py
#Author: Leon3DVFX
#License: MIT
from maya import OpenMayaUI as omui
from PySide6 import QtWidgets,QtCore
from shiboken6 import wrapInstance

def get_maya_main_window():
    ptr = omui.MQtUtil.mainWindow()  
    return wrapInstance(int(ptr), QtWidgets.QWidget)

mw = get_maya_main_window()
flag0 = mw.windowState()
flag1 = QtCore.Qt.WindowState.WindowFullScreen

mw.setWindowState(flag1 ^ flag0)
