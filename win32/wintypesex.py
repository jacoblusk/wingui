import ctypes

from ctypes.wintypes import *

def MAKELONG(wLow, wHigh):
    return ctypes.c_long(wLow | wHigh << 16)


def MAKELPARAM(l, h):
    return LPARAM(MAKELONG(l, h).value)


def LOWORD(l):
    return WORD(l & 0xFFFF)


def HIWORD(l):
    return WORD((l >> 16) & 0xFFFF)

LRESULT = ctypes.c_long
HCURSOR = HANDLE
LONG_PTR = LPARAM