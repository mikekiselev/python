import recommendations

#@todo сделать вывод в виде таблицы

for item in recommendations.critics :
    print(item)
    for value in recommendations.critics :
        if item == value : continue
        print(value)
        result = recommendations.sim_pearson(recommendations.critics, item, value)
        print(result)
print('-------')
result = recommendations.sim_pearson(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
print(result)
