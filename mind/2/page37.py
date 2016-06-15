import recommendations

print('-------')
result = recommendations.getRecommendations(recommendations.critics, 'Toby')
print(result)
print('-------')
result = recommendations.getRecommendations(recommendations.critics, 'Toby', similarity=recommendations.sim_distance)
print(result)
