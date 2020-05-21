#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk


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


# 输入二维矩阵
def input_array():
    global N
    global M
    msg = '输入错误,请重新输入矩阵行列数:'

    N, M = map(int, input('请输入矩阵行列数:').split())
    a = []
    for _ in range(N):
        a.append(list(map(float, input('输入第%s行数字:' % str(_ + 1)).rstrip().split())))
    # N = 3
    # M = 3
    d = [[0.3, 0.2, 0.3], [0.5, 0.4, 0.1], [0.1, 0.3, 0.4]]
    b = [[7, 2, 9], [2, 9, 0], [9, 0, 11]]
    c = [[9, 8, 11, 8], [2, 4, 6, 3], [5, 8, 7, 8], [10, 7, 9, 6]]
    e = [[0, 1, 2], [-1, 0, 9], [-2, 0.7, 0.8]]
    return a


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
    # if saddle_point is None:
    #     # print('此矩阵无解！')
    #     return None
    # # print(arr)
    # else:
    #     count = 0
    #     for i in range(N):
    #         for j in range(M):
    #             if arr[i][j] == saddle_point:
    #                 num_address[count].append(i+1)
    #                 num_address[count].append(j+1)
    #                 count += 1
    #     print(num_address)

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
        num_address = [[] for i in range(M)]
    return num_address


# 主函数
def main():
    arr = input_array()
    address = get_adress(arr)
    print('初始矩阵为：')
    for i in range(N):
        for j in range(M):
            print(arr[i][j], end='\t')
        print()
    if address is None:
        print('此矩阵无解！')
    # print(arr)
    else:
        print('\tVg=', saddle(arr))
        for index in address:
            if len(index) == 0:
                break
            print('此对策的解：', 'A%s' % str(index[0]), 'B%s' % str(index[1]))


if __name__ == '__main__':
    judge = input("输入任意值开始，输入quit结束计算：")
    while judge != 'quit':
        main()
        judge = input("输入任意值开始，输入quit结束计算：")
