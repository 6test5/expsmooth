'''
Simple exponential smoothing
Created on 18.03.2019
@author: /dat
y_t = a * y_t + a * (1-a)^1 * y_t-1 + a * (1-a)^2 * y_t-2 + ... + a*(1-a)^n * y_t-n
'''

import numpy as np
import xlwings as xw


@xw.func
def main(st):
    data = []  # Основная data
    # sht = xw.Book.caller().sheets[0]  # Выбор файла Excel # Выбор листа
    for values in st:  # Считывание данных из ячеек
        data.append(values)

    sss = []  # Список сигм
    a = []  # Список альфа, рассмотренных с шагом 0.1
    opt_a = []  # Итерация альфа с шагом 0.001
    a2 = []  # Список альфа, рассмотренных с шагом 0.001
    sss2 = []  # Список сигм, полученных при более подробном рассмотрении параметра альфа

    def alpha_counting(alpha):  # Ф-я подбора значения параметра альфа, основанная на поиске наименшего отклонения
        global output
        eps = 0
        y = 0
        for i in data:
            if y == 0:
                b = alpha * i + (1 - alpha) * i
                y += 1
            else:
                c = (b - i) ** 2
                eps += c
                b = alpha * i + (1 - alpha) * b
        sigma = eps / (len(data))
        sss.append(sigma)
        a.append(alpha)
        y = 0
        if len(a) == 19:  # Ф-я расчета прогнозного значения с наилучшим параметром альфа
            k = int(sss.index(min(sss)))
            # print(sss)
            # print(k) #Для проверки
            opt_alpha = a[k]
            print(opt_alpha)  # Вывод первоначального оптимального значения альфа
            for alp2 in np.arange(opt_alpha - 0.2, opt_alpha + 0.2, 0.001):
                opt_a.append(alp2)
            # print(opt_a)
            for q in opt_a:
                eps = 0
                y = 0
                for i in data:
                    if y == 0:
                        b = q * i + (1 - q) * i
                        y += 1
                    else:
                        c = (b - i) ** 2
                        eps += c
                        b = q * i + (1 - q) * b
                sigma = eps / (len(data))
                sss2.append(sigma)
                a2.append(q)
                y = 0
                if len(a2) == 400:  # Ф-я расчета прогнозного значения с наилучшим параметром альфа
                    k2 = int(sss2.index(min(sss2)))
                    # print(sss2)
                    # print(k2)               # Для проверки
                    opt_alpha2 = a2[k2]
                    print(opt_alpha2)  # Вывод наилушего значения альфа
                    for i in data:  # Финальный расчет прогноза
                        if y == 0:
                            output = opt_alpha2 * i + (1 - opt_alpha2) * i
                            y += 1
                        else:
                            output = opt_alpha2 * i + (1 - opt_alpha2) * output
                        !!!!!return output!!!!!

    for alp in np.arange(0.1, 2, 0.1):  # Итерация всех допустимых значений параметра альфа с заданным шагом
        alpha_counting(alp)


if __name__ == '__main__':
    xw.Book().set_mock_caller()
    main()
