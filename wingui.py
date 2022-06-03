import ctypes

from win32 import user32, kernel32, gdi32
from typing import *
from ctypes.wintypes import *
from win32.wintypesex import *


class MessageHandler:
    def __init__(self):
        self.module_handle = kernel32.GetModuleHandleW(None)

    def run(self):
        message = user32.MSG()

        while (result := user32.GetMessageW( \
                ctypes.byref(message),       \
                None, 0, 0)                  \
               ) != 0:

            if result == -1:
                break

            user32.TranslateMessage(ctypes.byref(message))
            user32.DispatchMessageW(ctypes.byref(message))


def _enum_child_proc(hwnd, lparam):
    user32.SendMessageW(hwnd, user32.WindowMessage.SETFONT, WPARAM(lparam), MAKELPARAM(1, 0))
    return True


class Window:
    def __init__(self, msg_handler: MessageHandler, title: str, dimensions: Tuple[int, int], parent=None, onclose=None):
        self.msg_handler = msg_handler
        self.title = title
        self.dimensions = dimensions
        self.controls = []
        self.parent = parent
        self.onclose = onclose

        temp_class = user32.WNDCLASSW()
        result = user32.GetClassInfoW(self.msg_handler.module_handle, self.title, ctypes.byref(temp_class))

        if result != 0:
            user32.UnregisterClassW(title, self.msg_handler.module_handle)

        window_class = user32.WNDCLASSW()
        window_class.style = user32.ClassStyle.VREDRAW | user32.ClassStyle.HREDRAW
        window_class.hbrBackground = HBRUSH(5)

        @user32.WNDPROC
        def __window_proc_fn(hwnd: HANDLE, umsg: user32.MSG, wparam: WPARAM, lparam: LPARAM):
            return self.__window_proc(hwnd, umsg, wparam, lparam)

        self.window_proc_fn = __window_proc_fn

        window_class.lpfnWndProc = self.window_proc_fn
        window_class.hInstance = self.msg_handler.module_handle
        window_class.lpszClassName = self.title

        user32.RegisterClassW(ctypes.byref(window_class))

        self.window_class = window_class

        self.handle = user32.CreateWindowExW(
            0,
            window_class.lpszClassName,
            self.title,
            user32.WindowStyle.OVERLAPPED | user32.WindowStyle.CAPTION \
            | user32.WindowStyle.SYSMENU | user32.WindowStyle.MINIMIZEBOX,
            user32.CW_USEDEFAULT, user32.CW_USEDEFAULT, self.dimensions[0], self.dimensions[1],
            None if not self.parent else self.parent.handle,
            None,
            self.msg_handler.module_handle,
            None
        )


    def show(self):
        metrics = user32.NONCLIENTMETRICSW()
        metrics.cbSize = ctypes.sizeof(user32.NONCLIENTMETRICSW)
        # SPI_GETNONCLIENTMETRICS = 0x0029
        user32.SystemParametersInfoW(0x0029, metrics.cbSize, ctypes.byref(metrics), 0)
        font = gdi32.CreateFontIndirectW(ctypes.byref(metrics.lfMenuFont))

        user32.EnumChildWindows(self.handle, user32.WNDENUMPROC(_enum_child_proc),
                         LPARAM(ctypes.cast(font, ctypes.c_void_p).value))

        user32.ShowWindow(self.handle, 5)

    def set_enable(self, b):
        user32.EnableWindow(self.handle, b)

    def close(self):
        user32.DestroyWindow(self.handle)

    def __window_proc(self, hwnd: HANDLE, umsg: user32.MSG, wparam: WPARAM, lparam: LPARAM):
        if umsg == user32.WindowMessage.DESTROY:
            if self.onclose:
                self.onclose()

            if not self.parent:
                user32.PostQuitMessage(0)
        elif umsg == user32.WindowMessage.CLOSE:
            user32.DestroyWindow(hwnd)
        elif umsg == user32.WindowMessage.COMMAND:
            control_id = LOWORD(wparam).value
            notification_code = HIWORD(wparam).value
            control_hwnd = lparam

            for control in self.controls:
                if control_id == control.control_id and control.onclick:
                    control.onclick()

        return user32.DefWindowProcW(hwnd, umsg, wparam, lparam)


class Control:
    control_id_counter = 0

    @classmethod
    def get_new_control_id(cls) -> int:
        cls.control_id_counter += 1

        return cls.control_id_counter

    def __init__(self, parent: Window, class_name: LPCWSTR, text: str, \
        position: Tuple[int, int], dimensions: Tuple[int, int], styles, onclick=None):
        self.parent = parent
        self.control_id = Control.get_new_control_id()
        self.onclick = onclick

        self.handle = user32.CreateWindowExW(
            0,
            class_name,
            text,
            user32.WindowStyle.TABSTOP | user32.WindowStyle.VISIBLE | user32.WindowStyle.CHILD | styles,
            position[0], position[1], dimensions[0], dimensions[1],
            parent.handle,
            HMENU(self.control_id),
            ctypes.cast(user32.GetWindowLongPtrW(
                parent.handle, user32.GetWindowLong.HINSTANCE),
            HINSTANCE),
            None
        )

        self.parent.controls.append(self)


class Button(Control):
    def __init__(self, parent: Window, text: str, \
        position: Tuple[int, int], dimensions: Tuple[int, int], onclick=None):

        super().__init__(parent, "BUTTON", text, position, dimensions, user32.ButtonStyle.DEFPUSHBUTTON, onclick=onclick)


class EditText(Control):
    def __init__(self, parent: Window, text: str, \
        position: Tuple[int, int], dimensions: Tuple[int, int], onclick=None):

        super().__init__(parent, "EDIT", text, position, dimensions, user32.WindowStyle.BORDER, onclick=onclick)

    def get_text(self):
        length = user32.GetWindowTextLengthW(self.handle)
        text_buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(self.handle, text_buffer, length + 1)

        return text_buffer.value


class Label(Control):
    def __init__(self, parent: Window, text: str, \
        position: Tuple[int, int], dimensions: Tuple[int, int], onclick=None):

        super().__init__(parent, "STATIC", text, position, dimensions, 0, onclick=onclick)