#!/usr/bin/python
# -*- coding: UTF-8 -*-


from win32gui import *
from time import sleep
from random import randint
from threading import Thread
from math import *
from commctrl import *
from ctypes import *
from ctypes import wintypes
import win32con

SetWindowsHookEx = windll.user32.SetWindowsHookExA
UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx
CallNextHookEx = windll.user32.CallNextHookEx
GetMessage = windll.user32.GetMessageA
GetModuleHandle = windll.kernel32.GetModuleHandleW
# 保存键盘钩子函数句柄
keyboard_hd = None
# 保存按键
key = None


class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [
        ('vkCode', c_int),
        ('scanCode', c_int),
        ('flags', c_int),
        ('time', c_int),
        ('dwExtraInfo', c_uint),
        ('', c_void_p)
    ]


def wait_for_msg():
    msg = wintypes.MSG()
    GetMessage(msg, 0, 0, 0)


def keyboard_pro(nCode, wParam, lParam):
    """
    函数功能：键盘钩子函数，当有按键按下时此函数被回调
    """
    global key
    if nCode == win32con.HC_ACTION:
        KBDLLHOOKSTRUCT_p = POINTER(KBDLLHOOKSTRUCT)
        param = cast(lParam, KBDLLHOOKSTRUCT_p)
        # print(param.contents.vkCode)
        key = param.contents.vkCode
    return CallNextHookEx(keyboard_hd, nCode, wParam, lParam)


def start_keyboard_hook():
    """
    函数功能：启动键盘监听
    """
    HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    pointer = HOOKPROTYPE(keyboard_pro)
    keyboard_hd = SetWindowsHookEx(
        win32con.WH_KEYBOARD_LL,
        pointer,
        GetModuleHandle(None),
        0)
    wait_for_msg()


hProgMan = FindWindow('ProgMan', None)
hShellDefView = FindWindowEx(hProgMan, None, 'SHELLDLL_DefView', None)
SysListView32 = FindWindowEx(hShellDefView, None, 'SysListView32', None)
desk = GetDesktopWindow()
# Nm = GetWindowText(SysListView32)
c = GetWindowRect(SysListView32)
count = SendMessage(SysListView32, LVM_GETITEMCOUNT, 0, 0)
print('count:', count)
print(c)
cur = 2


def MAKELPARAM(x, y):
    x = int(x)
    y = int(y)
    return y << 16 | x


def get_child_windows(parent):
    # 获得parent的所有子窗口句柄
    # 返回子窗口句柄列表
    if not parent:
        return
    hwndChildList = []
    EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList


class vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self, vec):
        return vector(self.x + vec.x, self.y + vec.y)

    def set(self, vec):
        self.x, self.y = vec.x, vec.y

    def mult(self, num):
        return vector(self.x * num, self.y * num)


v = vector(0, 0)

pos = [vector(c[2] / 2, c[3] / 2), vector(c[2] / 2, c[3] / 2),
       vector(randint(100, c[2] - 100), randint(100, c[3] - 100))]
SendMessage(SysListView32, LVM_SETITEMPOSITION, 0, MAKELPARAM(pos[0].x, pos[0].y))
SendMessage(SysListView32, LVM_SETITEMPOSITION, 1, MAKELPARAM(pos[1].x, pos[1].y))
SendMessage(SysListView32, LVM_SETITEMPOSITION, cur, MAKELPARAM(pos[cur].x, pos[cur].y))
for i in range(cur, count):
    pos.append(vector(0, -100))
    SendMessage(SysListView32, LVM_SETITEMPOSITION, i, MAKELPARAM(pos[i].x, pos[i].y))


def run(pv):
    for i in range(cur - 1, 0, -1):
        pos[i].set(pos[i - 1])
    pos[0] = pos[0].add(pv.mult(60))
    for i in range(count):
        SendMessage(SysListView32, LVM_SETITEMPOSITION, i, MAKELPARAM(pos[i].x, pos[i].y))
        # print(pos[i][1],end=' ')
    sleep(0.2)


frame = 0
Thread(target=start_keyboard_hook).start()
while 1:
    frame += 1
    if key == 37:
        v = vector(-1, 0)
    if key == 38:
        v = vector(0, -1)
    if key == 39:
        v = vector(1, 0)
    if key == 40:
        v = vector(0, 1)
    run(v)
    if sqrt((pos[0].x - pos[cur].x) ** 2 + (pos[0].y - pos[cur].y) ** 2) < 60:
        cur += 1
        pos[cur].set(vector(randint(100, c[2] - 100), randint(100, c[3] - 100)))
        SendMessage(SysListView32, LVM_SETITEMPOSITION, cur, MAKELPARAM(pos[cur].x, pos[cur].y))
