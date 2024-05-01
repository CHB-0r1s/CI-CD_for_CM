import os
import sys
import matplotlib

an = open("lab1_test_result.txt", "w")

def main(dim, nums, eps):
    ret = diag_matr(dim, nums)
    nums = ret[0]
    d = ret[1]
    res = ret[2]

    res_lin = check_lin(dim, nums)

    if res_lin:
        print("Матрица линейно зависима, а значит существует бесконечное число решений, следовательно данный метод не применим.")
        an.write("0")
        sys.exit()

    ddd = False
    if not res:
        print("Для данной матрицы условие преобладания диагональных элементов не выполняется, а значит сходимость не гарантированна. Будет проведено 100 итераций. Если в результате не будет достигнута заданная точность, значит найти решение таким методом невозможно.")
        ddd = True
        an.write("1")

    coef = []
    for i in range(dim):
        coef.append([])
        for z in range(dim):
            if i != z:
                coef[i].append(-nums[i][z] / nums[i][i])
            else:
                coef[i].append(0)
        d[i] /= nums[i][i]

    apr = d.copy()
    res_table = [[], []]

    res_table[0].append("k")
    res_table[0] += [f"x{x}^k" for x in range(1, dim+1)]
    res_table[0] += [f"x{x}^(k) - x{x}^(k-1)" for x in range(1, dim+1)]
    res_table[0].append("max|xi^(k) - xi^(k-1)|")

    res_table[1].append("0")
    res_table[1] += list(map(str, apr))
    res_table[1] += ["-" for x in range(dim+1)]
    for k in range(100):
        next_apr = []
        res_table.append([])
        for i in range(dim):
            next_apr.append(sum((
                coef[i][x]*apr[x] for x in range(dim)
            )) + d[i])
        dif_apr = [abs(next_apr[x]-apr[x]) for x in range(dim)]
        rr = False
        if max(dif_apr) < eps:
            rr = True
            #break
        apr = next_apr.copy()
        # for i in range(dim):
        #     next_apr[i] = round(next_apr[i], 12)
        # for i in range(dim):
        #     dif_apr[i] = round(dif_apr[i], 12)
        res_table[k+2].append(str(k+1))
        res_table[k+2] += list(map(str, next_apr))
        res_table[k+2] += list(map(str, dif_apr))
        res_table[k+2].append(str(max(dif_apr)))

        if rr:
            break

    if len(res_table) == 102:
        print("Метод не сходится")
    else:
        col_width = []
        for i in range(len(res_table[0])):
            ma = 0
            for z in res_table:
                if len(str(z[i])) > ma:
                    ma = len(str(z[i]))
            col_width.append(ma+4)
        col_width.append(0)
        for i in res_table:
            print("".join(i[z].ljust(col_width[z]) for z in range(len(i))))

    if not ddd:
        for i in res_table[-1][1:dim+1]:
            an.write(i + " ")

def check_lin(dim, nums):
    res = False
    for i in range(len(nums)):
        loc_res = True
        for z in range(i+1, len(nums)):
            k = ""
            for l in range(len(nums[i])):
                try:
                    if k == "":
                        k = nums[i][l]/nums[z][l]
                    else:
                        if nums[i][l]/nums[z][l] != k:
                            loc_res = False
                            break
                except:
                    if k == "":
                        k = " "
                    elif k != " ":
                        loc_res = False
                        break
                    continue
            if loc_res:
                res = True
                break
        if loc_res:
            break
    return res

def diag_matr(dim, nums):
    d = []
    diag_d = []
    for i in range(dim):
        d.append(nums[i].pop(-1))
        diag_d.append(0)

    sort_nums = []
    diag_nums = []
    for i in range(dim):
        diag_nums.append([])
        sort_nums.append([])
        for z in range(dim):
            sort_nums[i].append((nums[i][z], z))
        sort_nums[i].sort(key=lambda x: x[0], reverse=True)

    for i in range(dim):
        for z in sort_nums[i]:
            if diag_nums[z[1]] == []:
                diag_nums[z[1]] = nums[i]
                diag_d[z[1]] = d[i]
                break
            else:
                continue
    for i in range(dim):
        s = 0
        for z in range(dim):
            if i != z:
                s += abs(diag_nums[i][z])
        if abs(diag_nums[i][i]) < s:
            return [diag_nums, diag_d, False]
    return [diag_nums, diag_d, True]

def enter_var():
    print("Хотите осуществить ввод с клавиатуры или из файла?\n"
          "Введите 1 если с клавиатуры и 2 если из файла:")
    while True:
        var = input()
        if not (var == "1" or var == "2"):
            print("Введите 1 если с клавиатуры и 2 если из файла:")
            continue
        break
    return var

def enter_n():
    print("Вводите размерность матрицы:")
    while True:
        try:
            n = int(input())
        except:
            print("Введенная строка не число")
            continue
        if n < 2:
            print("Размерность матрицы должна быть 2 или больше. Повторите ввод:")
            continue
        break
    return n

def enter_eps():
    print("Введите допустимую погрешность")
    while True:
        eps = input()
        eps = eps.replace(',', '.')
        try:
            eps = float(eps)
        except:
            print("Введенная строка не является числом. Повторите ввод:")
            continue
        if eps <= 0:
            print("Допустимая погрешность должна быть положительной. Повторите ввод:")
            continue
        break
    return eps

def enter_coef_line(n):
    while True:
        line = list(input().split())
        if len(line) != n + 1:
            print(
                f"Число введенных чисел равно {len(line)}. В строке должно быть {n} коэффициентов и 1 свободный член.  Повторите ввод этой строки:")
            continue
        err = []
        for i in line:
            try:
                float(i)
            except:
                err.append(i)
        if len(err) != 0:
            print(f"{', '.join(err)} не являются числами. Повторите ввод этой строки:")
            continue
        break
    return line

def enter_path():
    print("Введите путь до файла.\n"
          "Структура файла должна быть такой:\n"
          "в 1 строке размерность(натуральное положительное число больше 1)\n"
          "во 2 строке допустимая погрешность(дробное число больше 0)\n"
          "коэффициенты матрицы построчно через пробел. Свободный член является самым последним числом в строке")
    while True:
        pa = input()
        if not os.path.isfile(pa):
            print("Файла по такому пути нет. Повторите ввод:")
            continue
        break
    return pa


def data_entry():
    var = enter_var()
    nums = []
    if var == "1":
        n = enter_n()
        eps = enter_eps()
        print("Вводите коэффициенты построчно через пробел. Свободный член вводите самым правым элементом:")
        for i in range(n):
            nums.append(list(map(float, enter_coef_line(n))))
        main(n, nums, eps)
    elif var == "2":
        pa = enter_path()
        file = open(pa, "r")
        res = True
        err_line = ""
        l = -1
        try:
            l = file.readline()
            n = int(l)
            if n < 2:
                res = False
                err_line = l
            l = file.readline()
            eps = float(l)
            if eps <= 0:
                res = False
                err_line = l
            for i in range(n):
                l = file.readline()
                nums.append(list(map(float, l.split())))
        except:
            res = False
            err_line = l
        if not res:
            if err_line != -1:
                print(f"Формат файла неверный. Ошибка в строке:\n"
                  f"{err_line}")
            else:
                print("Файл пуст")
        else:
            main(n, nums, eps)

if __name__ == "__main__":
    data_entry()

