#!/usr/bin/python
# -*- coding: UTF-8 -*-


from tkinter import *
import tkinter.messagebox
from sympy import *
from math import *
import scipy.integrate as si


class LoginPage(object):
    def __init__(self, master=None):

        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (800, 600))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        # 创建Frame
        self.page = Frame(self.root)
        self.shot_1 = Shot1Frame(self.root)
        self.shot_2 = Shot2Frame(self.root)
        self.shot_1.pack()
        # 设置菜单栏名称
        menubar = Menu(self.root)
        menubar.add_command(label='命中概率计算方法1', command=self.shot_1_page)
        menubar.add_command(label='命中概率计算方法2', command=self.shot_2_page)

        # 设置菜单栏
        self.root['menu'] = menubar

    # 命中概率计算方法1 界面
    def shot_1_page(self):
        self.shot_1.pack()
        self.shot_2.pack_forget()

    # 命中概率计算方法2 界面
    def shot_2_page(self):
        self.shot_2.pack()
        self.shot_1.pack_forget()


# 命中概率计算方法1 类
class Shot1Frame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.E1 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E2 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E3 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E4 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E5 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E6 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E7 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E8 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E9 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E10 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E11 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        self.createPage()

    # 子界面
    def createPage(self):
        Label(self).grid(row=1, stick=W, pady=10)

        Label(self, text='Ex: ').grid(row=11, column=1, stick=W, pady=10)
        self.E1.grid(row=11, column=3, stick=E)

        Label(self, text='Ey: ').grid(row=15, column=1, stick=W, pady=10)
        self.E2.grid(row=15, column=3, stick=E)

        Label(self, text='alpha: ').grid(row=3, column=13, stick=W, pady=10)
        self.E5.grid(row=5, column=13, stick=E)

        Label(self, text='beta: ').grid(row=3, column=17, stick=W, pady=10)
        self.E6.grid(row=5, column=17, stick=E)

        Label(self, text='sigma: ').grid(row=7, column=13, stick=W, pady=10)
        self.E7.grid(row=9, column=13, stick=E)

        Label(self, text='gamma: ').grid(row=7, column=17, stick=W, pady=10)
        self.E8.grid(row=9, column=17, stick=E)

        Label(self, text='miu_x: ').grid(row=11, column=13, stick=W, pady=10)
        self.E9.grid(row=13, column=13, stick=E)

        Label(self, text='miu_y: ').grid(row=11, column=17, stick=W, pady=10)
        self.E10.grid(row=13, column=17, stick=E)

        Label(self, text='命中概率: ').grid(row=21, column=9, stick=W, pady=10)

        Button(self, text='计算', command=self.click).grid(row=25, column=7, stick=E, pady=10)

        Button(self, text='退出', command=self.page.quit).grid(row=25, column=15, stick=E, pady=10)

    # 点击计算后的计算程序
    def click(self):
        Ex = float(self.E1.get())
        Ey = float(self.E2.get())
        alpha = float(self.E5.get())
        beta = float(self.E6.get())
        sigma = float(self.E7.get())
        gamma = float(self.E8.get())
        miu_x = float(self.E9.get())
        miu_y = float(self.E10.get())

        # 概率密度函数
        def f(x):
            return 2 / sqrt(pi) * e ** (-x ** 2)

        # 设置概率密度函数积分
        def calculate(t):
            x = symbols('x')
            f = 2/sqrt(pi)*e**(-x**2)
            # p = integrate(f, (x, 0, t))
            result = si.quad(f, 0, t)
            return result[0]

        P = 1/4 * (calculate((beta-miu_x)/Ex) - calculate((alpha-miu_x)/Ex)) * (calculate((sigma-miu_y)/Ey)-calculate((gamma-miu_y)/Ey))

        print(str(P))

        Label(self, text=str(P)).grid(row=21, column=11, stick=W, pady=10)

    # 计算结果并返回为字符串


# 命中概率计算方法2 类
class Shot2Frame(object):
    def __init__(self, master=None):
        pass



class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.T = StringVar()
        self.Q = StringVar()
        self.E1 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E2 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E3 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E4 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E5 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E6 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E7 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E8 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E9 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E10 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E11 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E12 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E13 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E14 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E15 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)
        self.E16 = Entry(self, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10)

        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        self.createPage()

    def Isspace(self, text):
        temp = 0
        for i in text:
            if not i.isspace():
                temp = 1
                break

        if temp == 1:
            return 0
        else:
            return 1

    def click(self):

        global T
        global Q

        times = self.T.get().rstrip().split()
        index = self.Q.get().rstrip().split()

        T = int(times[0])
        Q = int(index[0]) - 1

        global arrList1
        arrList1 = [[] for i in range(N)]
        arrList = []
        ba1 = self.E1.get().rstrip().split()
        ba2 = self.E2.get().rstrip().split()
        ba3 = self.E3.get().rstrip().split()
        ba4 = self.E4.get().rstrip().split()
        ba5 = self.E5.get().rstrip().split()
        ba6 = self.E6.get().rstrip().split()
        ba7 = self.E7.get().rstrip().split()
        ba8 = self.E8.get().rstrip().split()
        ba9 = self.E9.get().rstrip().split()
        ba10 = self.E10.get().rstrip().split()
        ba11 = self.E11.get().rstrip().split()
        ba12 = self.E12.get().rstrip().split()
        ba13 = self.E13.get().rstrip().split()
        ba14 = self.E14.get().rstrip().split()
        ba15 = self.E15.get().rstrip().split()
        ba16 = self.E16.get().rstrip().split()

        if N == 3:
            if M == 2:
                a1 = ba1[0]
                a2 = ba2[0]
                a5 = ba5[0]
                a6 = ba6[0]
                a9 = ba9[0]
                a10 = ba10[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a9)
                arrList.append(a10)

            if M == 3:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]

                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]

                a9 = ba9[0]
                a10 = ba10[0]
                a11 = ba11[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                # arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
                # arrList.append(a8)
                arrList.append(a9)
                arrList.append(a10)
                arrList.append(a11)
                # arrList.append(a12)
                # arrList.append(a13)
                # arrList.append(a14)
                # arrList.append(a15)
                # arrList.append(a16)
            if M == 4:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]
                a4 = ba4[0]
                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]
                a8 = ba8[0]
                a9 = ba9[0]
                a10 = ba10[0]
                a11 = ba11[0]
                a12 = ba12[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
                arrList.append(a8)
                arrList.append(a9)
                arrList.append(a10)
                arrList.append(a11)
                arrList.append(a12)
                # arrList.append(a13)
                # arrList.append(a14)
                # arrList.append(a15)
                # arrList.append(a16)
        elif N == 4:
            if M == 2:
                a1 = ba1[0]
                a2 = ba2[0]

                a5 = ba5[0]
                a6 = ba6[0]

                a9 = ba9[0]
                a10 = ba10[0]

                a13 = ba13[0]
                a14 = ba14[0]

                arrList.append(a1)
                arrList.append(a2)
                # arrList.append(a3)
                # arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                # arrList.append(a7)
                # arrList.append(a8)
                arrList.append(a9)
                arrList.append(a10)
                # arrList.append(a11)
                # arrList.append(a12)
                arrList.append(a13)
                arrList.append(a14)
                # arrList.append(a15)
                # arrList.append(a16)
            if M == 3:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]

                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]

                a9 = ba9[0]
                a10 = ba10[0]
                a11 = ba11[0]

                a13 = ba13[0]
                a14 = ba14[0]
                a15 = ba15[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                # arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
                # arrList.append(a8)
                arrList.append(a9)
                arrList.append(a10)
                arrList.append(a11)
                # arrList.append(a12)
                arrList.append(a13)
                arrList.append(a14)
                arrList.append(a15)
                # arrList.append(a16)
            if M == 4:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]
                a4 = ba4[0]
                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]
                a8 = ba8[0]
                a9 = ba9[0]
                a10 = ba10[0]
                a11 = ba11[0]
                a12 = ba12[0]
                a13 = ba13[0]
                a14 = ba14[0]
                a15 = ba15[0]
                a16 = ba16[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
                arrList.append(a8)
                arrList.append(a9)
                arrList.append(a10)
                arrList.append(a11)
                arrList.append(a12)
                arrList.append(a13)
                arrList.append(a14)
                arrList.append(a15)
                arrList.append(a16)
        elif N == 2:
            if M == 2:
                a1 = ba1[0]
                a2 = ba2[0]

                a5 = ba5[0]
                a6 = ba6[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a5)
                arrList.append(a6)
            if M == 3:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]

                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                # arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
            if M == 4:
                a1 = ba1[0]
                a2 = ba2[0]
                a3 = ba3[0]
                a4 = ba4[0]
                a5 = ba5[0]
                a6 = ba6[0]
                a7 = ba7[0]
                a8 = ba8[0]

                arrList.append(a1)
                arrList.append(a2)
                arrList.append(a3)
                arrList.append(a4)
                arrList.append(a5)
                arrList.append(a6)
                arrList.append(a7)
                arrList.append(a8)

        print(arrList)
        count = 0
        for j in range(len(arrList)):
            if arrList[j] != ' ':
                arrList1[count].append(float(arrList[j]))
                if ((j+1) % int(M)) == 0:
                    count += 1

        print(arrList1)
        main()

    def createPage(self):
        Label(self).grid(row=1, stick=W, pady=10)

        self.E1.grid(row=3, column=1, stick=E)

        self.E2.grid(row=3, column=2, stick=E)

        self.E3.grid(row=3, column=3, stick=E)

        self.E4.grid(row=3, column=4, stick=E)

        Label(self).grid(row=4, stick=W, pady=10)

        self.E5.grid(row=5, column=1, stick=E)

        self.E6.grid(row=5, column=2, stick=E)

        self.E7.grid(row=5, column=3, stick=E)

        self.E8.grid(row=5, column=4, stick=E)

        Label(self).grid(row=6, stick=W, pady=10)

        self.E9.grid(row=7, column=1, stick=E)

        self.E10.grid(row=7, column=2, stick=E)

        self.E11.grid(row=7, column=3, stick=E)

        self.E12.grid(row=7, column=4, stick=E)

        Label(self).grid(row=8, stick=W, pady=10)

        self.E13.grid(row=19, column=1, stick=E)

        self.E14.grid(row=19, column=2, stick=E)

        self.E15.grid(row=19, column=3, stick=E)

        self.E16.grid(row=19, column=4, stick=E)

        Label(self).grid(row=20, stick=W, pady=10)

        Label(self.page, text='循环次数: ').grid(row=21, stick=W, pady=10)

        Entry(self.page, textvariable=self.T, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10). \
            grid(row=21, column=1, stick=E)

        Label(self.page, text='局中人1的选择: ').grid(row=22, stick=W, pady=10)

        Entry(self.page, textvariable=self.Q, borderwidth=3, highlightcolor='red', highlightthickness=1, width=10). \
            grid(row=22, column=1, stick=E)

        Button(self, text='计算', command=self.click).grid(row=40, column=1, stick=E, pady=10)

        Button(self, text='退出', command=self.page.quit).grid(row=40, column=3, stick=E, pady=10)


# 找列表中的最小值所在位置
def min_num(t):
    num = min(t)
    for i in range(0, len(t)):
        if t[i] == num:
            return i


# 找列表中的最大值所在位置
def max_num(t):
    num = max(t)
    for i in range(0, len(t)):
        if t[i] == num:
            return i


# 寻找鞍点
def saddle(list1):
    row_min = []
    col_max = []
    for row in range(len(list1)):
        row_min.append(min(list1[row]))

    list2 = []
    for j in range(len(list1[0])):
        temp = []
        for i in range(len(list1)):
            temp.append(list1[i][j])
        list2.append(temp)

    for col in range(len(list2)):
        col_max.append(max(list2[col]))

    t = [i for i in row_min if i in col_max]
    if len(t) == 0:
        return None
    else:
        return t[0]


# 获取鞍点数所在位置
def get_adress(list1):
    # saddle_point = saddle(list1)
    num_address = [[] for i in range(M)]

    row_min = []
    col_max = []

    # 行最小值
    for row in range(len(list1)):
        row_min.append(min(list1[row]))

    # 转置
    list2 = []
    for j in range(len(list1[0])):
        temp = []
        for i in range(len(list1)):
            temp.append(list1[i][j])
        list2.append(temp)

    # 转置矩阵的行最大值（列最大值）
    for col in range(len(list2)):
        col_max.append(max(list2[col]))

    count = 0
    t = [i for i in row_min if i in col_max]
    if len(t) != 0:
        for i in range(len(row_min)):
            for j in range(len(col_max)):
                if row_min[i] == t[0] and col_max[j] == t[0]:
                    num_address[count].append(i+1)
                    num_address[count].append(j+1)
                    count += 1
    else:
        num_address = 0
    return num_address


# 纯策略核心算法
def main():
    arr = arrList1
    address = get_adress(arr)
    print('初始矩阵为：')
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end='\t')
        print()
    if address == 0:
        print('此矩阵无解！')
        end = main_mixture()
        tkinter.messagebox.showinfo(title='结果', message=end)
    # print(arr)
    else:
        tkinter.messagebox.showinfo(title='结果', message='此矩阵请使用纯策略方法！')


# 混合策略
def main_mixture():
    # N行M列
    orign_arr = arrList1
    r_arr1 = [0] * M
    c_arr1 = [0] * N
    solution = []
    f_p = [0] * N
    s_p = [0] * M

    count = 1
    index = Q

    while count <= T:
        c_arr = []
        r_arr = orign_arr[index][:]
        # 迭代的目标行
        for q in range(M):
            r_arr1[q] = r_arr1[q] + r_arr[q]
        # 选出目标行的中最小数所在位置
        min_n = min_num(r_arr1)
        # 找到最小值
        min_small = min(r_arr1)
        # 找出行中最大值所在的列
        for j in range(N):
            c_arr.append(orign_arr[j][min_n])
        # 迭代的目标列
        for j in range(N):
            c_arr1[j] = c_arr1[j] + c_arr[j]
        max_big = max(c_arr1)

        address_r = max_num(c_arr1)
        index = address_r
        f_p[index] += 1
        s_p[min_n] += 1

        min_small = (float(min_small)/float(count))
        max_big = (float(max_big)/float(count))
        ave = float(min_small + max_big)/2.0
        solution.append(round(ave, 4))

        del r_arr
        del c_arr

        count += 1

    print('第一个人：', f_p)
    print('第二个人：', s_p)

    sum1 = sum(f_p)
    sum2 = sum(s_p)

    for mn in range(len(f_p)):
        f_p[mn] = float(f_p[mn]) / float(sum1)
    for mn in range(len(s_p)):
        s_p[mn] = float(s_p[mn]) / float(sum2)

    show_solution = ' '
    show_solution += '\tV=%s' % (str(solution[-1])) + '\n' + '局中人1： '
    for mn in f_p:
        show_solution += str(mn) + '\t'
    show_solution += '\n' + '局中人2：'
    for mn in s_p:
        show_solution += str(mn) + '\t'
    show_solution += '\n'
    return show_solution


# 主函数（tk窗口）
def mainTk():
    root = Tk()
    root.title('运筹学混合策略')
    LoginPage(root)
    root.mainloop()


if __name__ == '__main__':
    mainTk()