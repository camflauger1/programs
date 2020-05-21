#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import xlwt
import xlutils3.copy
import random
import matplotlib.pyplot as plt


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
    # N, M = map(int, input('请输入矩阵行列数:').split())
    # a = []
    # for _ in range(N):
    #    a.append(list(map(float, input('输入第%s行数字:' % str(_ + 1)).rstrip().split())))
    N = 3
    M = 3
    a = [[0.3, 0.2, 0.3], [0.5, 0.4, 0.1], [0.1, 0.3, 0.4]]
    # b = [[7, 2, 9], [2, 9, 0], [9, 0, 11]]
    # c = [[9, 8, 11, 8], [2, 4, 6, 3], [5, 8, 7, 8], [10, 7, 9, 6]]
    return a


# 主函数
def main():
    # N行M列
    orign_arr = input_array()
    # print(orign_arr)
    # save_arr = [[0] for _ in range(N)]
    r_arr1 = [0] * M
    c_arr1 = [0] * N
    solution = []
    f_p = [0] * N
    s_p = [0] * M
    i = int(input('输入循环次数：'))
    count = 1
    ll = 0
    index_arr = [1, 1, 2, 2, 2, 1, 1, 1, 2, 0]
    # index_arr = [2, 1, 1, 1, 0, 2, 1, 1, 1, 0]
    wb = xlrd.open_workbook(r'C:\Users\MACHENIKE\Desktop\1.xlsx')
    # ws = wb.sheet_by_index(0)
    wb = xlutils3.copy.copy(wb)
    ws = wb.get_sheet(0)

    first_line1 = ['局数', '第一位选手']
    first_line2 = []
    for p in range(N):
        first_line2.append('A'+str(p+1))
    first_line3 = ['第二位选手']
    first_line4 = []
    for p in range(M):
        first_line4.append('B' + str(p+1))
    first_line5 = [' ']
    first_line6 = ['B_MIN', 'A_MAX', 'AVE']
    # first_line = ['局数', '第一位选手', 'A1', 'A2', 'A3',  '第二位选手', 'B1', 'B2', 'B3', 'B_MIN', 'A_MAX', 'AVE']
    first_line = first_line1 + first_line2 + first_line3 + first_line4 + first_line5 + first_line6
    for j in range(len(first_line)):
        ws.write(0, j, first_line[j])
    style = "font:colour_index red;"
    red_style = xlwt.easyxf(style)
    index = 0

    while count <= i:
        c_arr = []
        r_arr = orign_arr[index][:]
        # 迭代的目标行
        for q in range(M):
            r_arr1[q] = r_arr1[q] + r_arr[q]
        # 选出目标行的中最小数所在位置
        min_n = min_num(r_arr1)
        # 找到最小值
        min_small = min(r_arr1)
        min_r = min_small
        # 找出行中最大值所在的列
        for j in range(N):
            c_arr.append(orign_arr[j][min_n])
        # 迭代的目标列
        for j in range(N):
            c_arr1[j] = c_arr1[j] + c_arr[j]
        max_big = max(c_arr1)
        max_n = max_big
        address_r = max_num(c_arr1)
        index = address_r
        f_p[index] += 1
        s_p[min_n] += 1

        min_small = (float(min_small)/float(count))
        max_big = (float(max_big)/float(count))
        ave = float(min_small + max_big)/2.0
        solution.append(round(ave, 4))

        ws.write(count, 0, count)
        ws.write(count, 1, str(index + 1) + '号')
        # ws.write(count, 2, r_arr1[0])
        # ws.write(count, 3, r_arr1[1])
        # ws.write(count, 4, r_arr1[2])
        for p in range(N):
            ws.write(count, 2+p, r_arr1[p])
        ws.write(count, 2+N, str(min_n + 1) + '号')
        for p in range(M):
            ws.write(count, 2+N+p+1, c_arr1[p])
        # ws.write(count, 6, c_arr1[0])
        # ws.write(count,
        # 7, c_arr1[1])
        # ws.write(count, 8, c_arr1[2])

        ws.write(count, 2+N+M+2, min_small)
        ws.write(count, 2+N+M+3, max_big)
        ws.write(count, 2 + N + M+4, ave)

        ws.write(count, 2 + min_n, min_r, red_style)
        ws.write(count, 2 + N + 1 + address_r, max_n, red_style)
        # print('x:', index, ' ', r_arr, ' y:', max_n, ' ', c_arr)
        # print('x目标：', r_arr1, max_big,  ' y目标：', min_small, c_arr1)
        # print('*' * 10 + '-' * 10 + '*' * 10)

        del r_arr
        del c_arr

        count += 1
    # for j in range(len(f_p)):
    #     ws.write(count, )
    wb.save(r'C:\Users\MACHENIKE\Desktop\1.xlsx')
    print('第一个人：', f_p)
    print('第二个人：', s_p)
    sum1 = sum(f_p)
    sum2 = sum(s_p)

    for mn in range(len(f_p)):
        f_p[mn] = float(f_p[mn])/float(sum1)
    for mn in range(len(s_p)):
        s_p[mn] = float(s_p[mn])/float(sum2)
    print('第一个人：', f_p)
    print('第二个人：', s_p)
    # print(r_arr1)
    # print(c_arr1)
    print(solution)
    # draw(solution)
    # print('*'*10 + '-'*10 + '*'*10)


# 画出折线图
def draw(arr):
    x = [i for i in range(len(arr))]
    plt.plot(x, arr)
    plt.show()


if __name__ == '__main__':
    main()










