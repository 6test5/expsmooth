'''
Simple exponential smoothing
Created on 18.03.2019
@author: /dat
y_t = a * y_t + a * (1-a)^1 * y_t-1 + a * (1-a)^2 * y_t-2 + ... + a*(1-a)^n * y_t-n
'''

import numpy as np
import pandas as pd
from pandas import DataFrame

f = pd.read_excel('dataimport.xlsx')

data = f
sss = []
a = []
outdata = []

z = 0


def alpha_counting(alpha):           # Ф-я подбора значения параметра альфа, основанная на поиске наименшего отклонения
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
    if z == 10:                                      # Ф-я расчета прогнозного значения с наилучшим параметром альфа
        kapow = int(sss.index(min(sss)))
        # print(sss)
        # print(kapow) #Для проверки
        print(alpha)
        opt_alpha = a[kapow]
        for i in data:
            if y == 0:
                output = opt_alpha * i + (1 - opt_alpha) * i
                y += 1
            else:
                output = opt_alpha * i + (1 - opt_alpha) * output
                outdata.append(output)
        print("Прогнозное значение: ", output)


for alp in np.arange(0.15, 1.5, 0.15):
    z += 1
    alpha_counting(alp)

