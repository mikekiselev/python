__author__ = 'm.kiselev@gmail.com'
import pandas
import operator
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
# print(data.head())
#вопрос 1
# вычисляем кол-во мужчин женщин
#print(data['Sex'].value_counts()) #male - 577   female - 314 -

# %выживших вопрос 2
print('Выжившие')
#print(data['Survived'].value_counts()) # 0    549 | 1    342
param = data['Survived'].value_counts()
print(param)
print(round(param[1]/891 *100., 2)) #38.38

# %1 класса 3
param = data['Pclass'].value_counts()
print('class')
print(param)
print(round(param[1]/891 *100., 2)) #21.21

#Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.
print('median ')
param = data['Age']
print(round(param.mean(), 4)) #29.70
print(param.median()) # 28

#Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
print('Задание 5')

param_sib = data['SibSp']
param_parch = data['Parch']

corr= param_sib.corr(param_parch, method='pearson')
print(round(corr, 2)) #0.41483769862 0.41

#Какое самое популярное женское имя на корабле?
# Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных.
# Данные очень разнородные и шумные, но из них требуется извлечь необходимую информацию.
# Попробуйте вручную разобрать несколько значений столбца Name и выработать правило для извлечения имен,
# а также разделения их на женские и мужские.

print('Задание 6')
res = data['Name'].get_values()
i=0
list_name = []
for name_row in res:

    if ("Miss." not in name_row) and ("Mrs." not in name_row) : continue

    index_brace = name_row.find("(")
    if index_brace != -1:
        name_row = name_row[index_brace + 1:]
        index_space = name_row.find(" ")
        name_row = name_row[:index_space]
        list_name.append(name_row)
    else:
        index_point = name_row.find(".")
        name_row = name_row[index_point + 2:]
        index_space = name_row.find(" ")
        name_row = name_row[:index_space]
        list_name.append(name_row)
    # print(name_row)
    i += 1
    # print(res)
print(list_name)
dict_name = {}
for name in list_name   :
    value = dict_name.get(name)
    if value is None:
        dict_name[name] = 1
    else:
        dict_name[name] = value + 1
    sorted_x = sorted(dict_name.items(), key=operator.itemgetter(1))
print(sorted_x) #Anna