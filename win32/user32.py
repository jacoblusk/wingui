import ctypes
import enum

from ctypes.wintypes import *
from win32.wintypesex import *

CW_USEDEFAULT = 0x80000000

WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
WNDENUMPROC = ctypes.WINFUNCTYPE(BOOL, HWND, LPARAM)

class ClassStyle(enum.IntFlag):
    VREDRAW = 0x0001
    HREDRAW = 0x0002
    DBLCLKS = 0x0008
    OWNDC = 0x0020
    CLASSDC = 0x0040
    PARENTDC = 0x0080
    NOCLOSE = 0x0200
    SAVEBITS = 0x0800
    BYTEALIGNCLIENT = 0x1000
    BYTEALIGNWINDOW = 0x2000
    GLOBALCLASS = 0x4000


class MSG(ctypes.Structure):
    _fields_ = [
        ('hwnd', HWND),
        ('message', UINT),
        ('wParam', WPARAM),
        ('lParam', LPARAM),
        ('time', DWORD),
        ('pt', POINT),
        ('lPrivate', DWORD)
    ]


LPMSG = ctypes.POINTER(MSG)

class WNDCLASSW(ctypes.Structure):
    _fields_ = [
        ('style', UINT),
        ('lpfnWndProc', WNDPROC),
        ('cbClsExtra', ctypes.c_int),
        ('cbWndExtra', ctypes.c_int),
        ('hInstance', HINSTANCE),
        ('hIcon', HICON),
        ('hCursor', HCURSOR),
        ('hbrBackground', HBRUSH),
        ('lpszMenuName', LPCWSTR),
        ('lpszClassName', LPCWSTR)
    ]


LPWNDCLASSW = ctypes.POINTER(WNDCLASSW)

class RECT(ctypes.Structure):
    _fields_ = [
        ('left', LONG),
        ('top', LONG),
        ('right', LONG),
        ('bottom', LONG),
    ]

class ICONINFO(ctypes.Structure):
    _fields_ = [
        ('fIcon', BOOL),
        ('xHotspot', DWORD),
        ('yHotspot', DWORD),
        ('hbmMask', HBITMAP),
        ('hbmColor', HBITMAP),
    ]


PICONINFO = ctypes.POINTER(ICONINFO)


class LOGFONTW(ctypes.Structure):
    LF_FACESIZE = 32
    _fields_ = [
        ('lfHeight', LONG),
        ('lfWidth', LONG),
        ('lfEscapement', LONG),
        ('lfOrientation', LONG),
        ('lfWeight', LONG),
        ('lfItalic', BYTE),
        ('lfUnderline', BYTE),
        ('lfStrikeOut', BYTE),
        ('lfCharSet', BYTE),
        ('lfOutPrecision', BYTE),
        ('lfClipPrecision', BYTE),
        ('lfQuality', BYTE),
        ('lfPitchAndFamily', BYTE),
        ('lfFaceName', WCHAR * LF_FACESIZE)
    ]


LPLOGFONTW = ctypes.POINTER(LOGFONTW)


class NONCLIENTMETRICSW(ctypes.Structure):
    _fields_ = [
        ('cbSize', UINT),
        ('iBorderWidth', ctypes.c_int),
        ('iScrollWidth', ctypes.c_int),
        ('iScrollHeight', ctypes.c_int),
        ('iCaptionWidth', ctypes.c_int),
        ('iCaptionHeight', ctypes.c_int),
        ('lfCaptionFont', LOGFONTW),
        ('iSmCaptionWidth', ctypes.c_int),
        ('iSmCaptionHeight', ctypes.c_int),
        ('lfSmCaptionFont', LOGFONTW),
        ('iMenuWidth', ctypes.c_int),
        ('iMenuHeight', ctypes.c_int),
        ('lfMenuFont', LOGFONTW),
        ('lfStatusFont', LOGFONTW),
        ('lfMessageFont', LOGFONTW),
        ('iPaddedBorderWidth', ctypes.c_int)
    ]


LPNONCLIENTMETRICSW = ctypes.POINTER(NONCLIENTMETRICSW)


class GetWindowLong(enum.IntEnum):
    EXSTYLE = -20
    HINSTANCE = -6
    HWNDPARENT = -8
    ID = -12
    STYLE = -16
    USERDATA = -21
    WNDPROC = -4


class WindowMessage(enum.IntEnum):
    SETFOCUS = 0x0007
    KILLFOCUS = 0x0006
    ENABLE = 0x000A
    SETREDRAW = 0x000B
    SETTEXT = 0x000C
    SETFONT = 0x0030
    GETFONT = 0x0031
    GETTEXT = 0x000D
    GETTEXTLENGTH = 0x000E
    PAINT = 0x000F
    CLOSE = 0x00010
    QUIT = 0x0012
    SHOWWINDOW = 0x0018
    NULL = 0x0000
    CREATE = 0x0001
    DESTROY = 0x0002
    MOVE = 0x0003
    SIZE = 0x0005
    ACTIVATE = 0x0006
    COMMAND = 0x0111
    NOTIFY = 0x004E


class ButtonStyle(enum.IntFlag):
    PUSHBUTTON = 0x00000000
    DEFPUSHBUTTON = 0x00000001
    CHECKBOX = 0x00000002
    AUTOCHECKBOX = 0x00000003
    RADIOBUTTON = 0x00000004
    _3STATE = 0x00000005
    AUTO3STATE = 0x00000006
    GROUPBOX = 0x00000007
    USERBUTTON = 0x00000008
    AUTORADIOBUTTON = 0x00000009
    PUSHBOX = 0x0000000A
    OWNERDRAW = 0x0000000B
    TYPEMASK = 0x0000000F
    LEFTTEXT = 0x00000020
    TEXT = 0x00000000
    ICON = 0x00000040
    BITMAP = 0x00000080
    LEFT = 0x00000100
    RIGHT = 0x00000200
    CENTER = 0x00000300
    TOP = 0x00000400
    BOTTOM = 0x00000800
    VCENTER = 0x00000C00
    PUSHLIKE = 0x00001000
    MULTILINE = 0x00002000
    NOTIFY = 0x00004000
    FLAT = 0x00008000
    RIGHTBUTTON = LEFTTEXT


class WindowStyle(enum.IntFlag):
    BORDER = 0x00800000
    CAPTION = 0x00C00000
    CHILD = 0x40000000
    CHILDWINDOW = 0x40000000
    CLIPCHILDREN = 0x02000000
    CLIPSIBLINGS = 0x04000000
    DISABLED = 0x08000000
    DLGFRAME = 0x00400000
    GROUP = 0x00020000
    HSCROLL = 0x00100000
    ICONIC = 0x20000000
    MAXIMIZE = 0x01000000
    MAXIMIZEBOX = 0x00010000
    MINIMIZE = 0x20000000
    MINIMIZEBOX = 0x00020000
    OVERLAPPED = 0x00000000
    POPUP = 0x80000000
    SIZEBOX = 0x00040000
    SYSMENU = 0x00080000
    TABSTOP = 0x00010000
    THICKFRAME = 0x00040000
    TILED = 0x00000000
    VISIBLE = 0x10000000
    VSCROLL = 0x00200000
    OVERLAPPEDWINDOW = OVERLAPPED | CAPTION | SYSMENU | THICKFRAME \
        | MINIMIZEBOX | MAXIMIZEBOX
    TILEDWINDOW = OVERLAPPEDWINDOW
    POPUPWINDOW = POPUP | BORDER | SYSMENU


class GetWindowLong(enum.IntEnum):
    EXSTYLE = -20
    HINSTANCE = -6
    HWNDPARENT = -8
    ID = -12
    STYLE = -16
    USERDATA = -21
    WNDPROC = -4

try:
    GetWindowLongPtrW = ctypes.windll.user32.GetWindowLongPtrW
except:
    GetWindowLongPtrW = ctypes.windll.user32.GetWindowLongW
GetWindowLongPtrW.argtypes = [HWND, ctypes.c_int]
GetWindowLongPtrW.restype = LONG_PTR

RegisterClassW = ctypes.windll.user32.RegisterClassW
RegisterClassW.argtypes = [LPWNDCLASSW]
RegisterClassW.restype = ATOM

UnregisterClassW = ctypes.windll.user32.UnregisterClassW
UnregisterClassW.argtypes = [LPCWSTR, HINSTANCE]
UnregisterClassW.restype = BOOL

GetClassInfoW = ctypes.windll.user32.GetClassInfoW
GetClassInfoW.argtypes = [HINSTANCE, LPCWSTR, LPWNDCLASSW]
GetClassInfoW.restype = BOOL

DefWindowProcW = ctypes.windll.user32.DefWindowProcW
DefWindowProcW.argtypes = [HWND, UINT, WPARAM, LPARAM]
DefWindowProcW.restype = LRESULT

CreateWindowExW = ctypes.windll.user32.CreateWindowExW
CreateWindowExW.argtypes = [DWORD, LPCWSTR, LPCWSTR, DWORD, ctypes.c_int,
                            ctypes.c_int, ctypes.c_int, ctypes.c_int,
                            HWND, HMENU, HINSTANCE, LPVOID]
CreateWindowExW.restype = HWND

ShowWindow = ctypes.windll.user32.ShowWindow
ShowWindow.argtypes = [HWND, ctypes.c_int]
ShowWindow.restype = BOOL

GetMessageW = ctypes.windll.user32.GetMessageW
GetMessageW.argtypes = [LPMSG, HWND, UINT, UINT]
GetMessageW.restype = BOOL

TranslateMessage = ctypes.windll.user32.TranslateMessage
TranslateMessage.argtypes = [LPMSG]
TranslateMessage.restype = BOOL

DispatchMessageW = ctypes.windll.user32.DispatchMessageW
DispatchMessageW.argtypes = [LPMSG]
DispatchMessageW.restype = BOOL

PostQuitMessage = ctypes.windll.user32.PostQuitMessage
PostQuitMessage.argtypes = [ctypes.c_int]
PostQuitMessage.restype = None

DestroyWindow = ctypes.windll.user32.DestroyWindow
DestroyWindow.argtypes = [HWND]
DestroyWindow.restype = BOOL

EnumChildWindows = ctypes.windll.user32.EnumChildWindows
EnumChildWindows.argtypes = [HWND, WNDENUMPROC, LPARAM]
EnumChildWindows.restype = BOOL

SystemParametersInfoW = ctypes.windll.user32.SystemParametersInfoW
SystemParametersInfoW.argtypes = [UINT, UINT, LPVOID, UINT]
SystemParametersInfoW.restype = BOOL

SendMessageW = ctypes.windll.user32.SendMessageW
SendMessageW.argtypes = [HWND, UINT, WPARAM, LPARAM]
SendMessageW.restype = LRESULT

GetWindowTextLengthW = ctypes.windll.user32.GetWindowTextLengthW
GetWindowTextLengthW.argtypes = [HWND]
GetWindowTextLengthW.restype = ctypes.c_int

GetWindowTextW = ctypes.windll.user32.GetWindowTextW
GetWindowTextW.argtypes = [HWND, LPCWSTR, ctypes.c_int]
GetWindowTextW.restype = ctypes.c_int

GetWindowTextW = ctypes.windll.user32.GetWindowTextW
GetWindowTextW.argtypes = [HWND, LPCWSTR, ctypes.c_int]
GetWindowTextW.restype = ctypes.c_int

GetClassNameW = ctypes.windll.user32.GetClassNameW
GetClassNameW.argtypes = [HWND, LPCWSTR, ctypes.c_int]
GetClassNameW.restype = ctypes.c_int

EnableWindow = ctypes.windll.user32.EnableWindow
EnableWindow.argtypes = [HWND, BOOL]
EnableWindow.restype = BOOL

CloseWindow = ctypes.windll.user32.CloseWindow
CloseWindow.argtypes = [HWND]
CloseWindow.restype = BOOL
