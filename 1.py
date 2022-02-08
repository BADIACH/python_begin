###задание №1 + гугл
#a = 10
#b = 15
#print("Переменные a и b - ", a, b)
#string1 = input("Введите первую строку ")
#number1 = int(input("Введите первое число "))
#string2 = input("Введите вторую строку ")
#number2 = int(input("Введите второе число "))
#print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))

###задание №2 +гугл
#q = int(input()) #ввод секунд
#a = str(q // 3600) # часы
#b = str((q // 60) % 60) # минуты
#c = str(q % 60) # секунды
#print(a+':'+b+':'+c)

###задание №3 сделал сам
#q = int(3)
#n = str(q)
#nn = str(q + q)
#nnn = str(q + q + q)
#print(n + nn + nnn)

### задание №4 гугл
#n = int(input("Введите целое положительное число "))
#max = n % 10
#while n >= 1:
   # n = n // 10
   # if n % 10 > max:
   #     max = n % 10
   # if n > 9:
   #     continue
   # else:
   #     print("Максимальное цифра в числе ", max)
   #     break

### задание №5
#revenue = float(input('выручка фирмы: '))
#cost = float(input('издержка фирмы: '))
#if revenue > cost:
  #  print(f'фирма работает в прибыль. {revenue / cost:.2f}')
  #  staff = int(input('кол-во сотрудников: '))
 #   print(f'прибыль фирмы на одного собрудника: {revenue / staff:.2f}')
#elif  cost == revenue:
 #   print("Фирма работает в ноль")
#else:
 #   print('фирма работает в убыток: ')
 ### задание №6
a = float(input('первый день '))
b = float(input('желаемый результат '))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)



