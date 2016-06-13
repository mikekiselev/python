import recommendations

print('-------')
result = recommendations.topMatches(recommendations.critics, "Toby", n=4)
print(result)
