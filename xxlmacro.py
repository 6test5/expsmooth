'''
Simple exponential smoothing
Created on 18.03.2019
@author: /dat
y_t = a * y_t + a * (1-a)^1 * y_t-1 + a * (1-a)^2 * y_t-2 + ... + a*(1-a)^n * y_t-n
'''

import numpy as np

import xlrd

dt = []

rb = xlrd.open_workbook('dataimport.xlsx')
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    dt.append(row)

data = []

for lst in dt:
    data.extend(lst)


sss = []
a = []
outdata = []

z = 0


def alpha_counting(alpha):  # Ф-я подбора значения параметра альфа, основанная на поиске наименшего отклонения
    eps = 0
    y = 0
    for i in data:
        if y == 0:
            b = alpha * i + (1 - alpha) * i
            y += 1
        else:
            b = alpha * i + (1 - alpha) * b
            c = (b - i) ** 2
            eps += c
    sigma = eps / (len(data) - 1)
    sss.append(sigma)
    a.append(alpha)
    y = 0
    if z == 20:  # Ф-я расчета прогнозного значения с наилучшим параметром альфа
        kapow = int(sss.index(min(sss)))
        # print(a)
        # print(sss)
        # print(kapow) #Для проверки
        opt_alpha = a[kapow]
        print(opt_alpha)
        for i in data:
            if y == 0:
                output = opt_alpha * i + (1 - opt_alpha) * i
                y += 1
            else:
                output = opt_alpha * i + (1 - opt_alpha) * output
                outdata.append(output)
        print("Прогнозное значение: ", int(output))


for alp in np.arange(0, 2, 0.1):
    z += 1
    alpha_counting(alp)

