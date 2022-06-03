import ctypes

from ctypes.wintypes import *
from win32.wintypesex import *

from win32.user32 import LPLOGFONTW

CreateFontIndirectW = ctypes.windll.gdi32.CreateFontIndirectW
CreateFontIndirectW.argtypes = [LPLOGFONTW]
CreateFontIndirectW.restype = HFONT

DeleteObject = ctypes.windll.gdi32.DeleteObject
DeleteObject.argtypes = [LPVOID]
DeleteObject.restype = BOOL

GetStockObject = ctypes.windll.gdi32.GetStockObject
GetStockObject.argtypes = [ctypes.c_int]
GetStockObject.restype = HANDLE

GetObjectW = ctypes.windll.gdi32.GetObjectW
GetObjectW.argtypes = [HANDLE, ctypes.c_int, LPVOID]
GetObjectW.restype = ctypes.c_int