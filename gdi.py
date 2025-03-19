import ctypes
import random
import time
import ctypes.wintypes

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
dc = user32.GetDC(0)

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

FillRect = user32.FillRect
FillRect.argtypes = [ctypes.wintypes.HDC, ctypes.POINTER(RECT), ctypes.wintypes.HBRUSH]

while True:
    x, y = random.randint(0, user32.GetSystemMetrics(0)), random.randint(0, user32.GetSystemMetrics(1))
    color = random.randint(0, 0xFFFFFF)
    brush = gdi32.CreateSolidBrush(color)
    rect = RECT(x, y, x + 10, y + 10)
    hdc = user32.GetDC(0)
    FillRect(hdc, ctypes.byref(rect), brush)
    user32.ReleaseDC(0, hdc)
    gdi32.DeleteObject(brush)
    user32.ScrollWindow(user32.GetDesktopWindow(), -5, -5, None, None)
    time.sleep(0.0003)
