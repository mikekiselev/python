import recommendations

for item in recommendations.critics :
    print(item)
    for value in recommendations.critics :
        if item == value : continue
        print(value)
        result = recommendations.sim_distance(recommendations.critics, item, value)
        print(result)
