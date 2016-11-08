import recommendations

print('-------')
movies = recommendations.transformPrefs(recommendations.critics);
result = recommendations.topMatches(movies, 'Supermen Returns')
print(result)

print('-------')
result = recommendations.getRecommendations(movies,'Just My Luck')
print(result)

