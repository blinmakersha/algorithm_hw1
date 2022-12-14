# данная функция проверяет одно число и считывает количество шагов 
# необходимое для преобразования его в ноль. сложность: O(log n).

def numberOfSteps(num: int):
    steps = 0       # задаем переменную для количества шагов.
    while num > 0:      # используем цикл для того, чтобы он работал пока 
			# число не станет нулем.
        if num % 2 == 0:        # через условный оператор задаем операции 
				# для нашего числа.
            num = num // 2      # если число четное, то делим его на два.
            steps += 1
        else:
            num = num - 1       # если число нечетное, то вычитаем один, и 
				# снова возвращаемся к первому действию.
            steps += 1
    return steps

print(numberOfSteps(8))
