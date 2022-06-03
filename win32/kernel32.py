import ctypes

from ctypes.wintypes import *
from win32.wintypesex import *

GetModuleHandleW = ctypes.windll.kernel32.GetModuleHandleW
GetModuleHandleW.argtypes = [LPCWSTR]
GetModuleHandleW.restype = HMODULE