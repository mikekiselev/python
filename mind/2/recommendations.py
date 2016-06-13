from math import sqrt

critics = {'Lisa Rose' : {'Lady in the Water' : 2.5,
                          'Snakes on a Plane' : 3.5,
                          'Just My Luck' : 3.0,
                          'Supermen Returns' : 3.5,
                          'You, Me and Dupree' : 2.5,
                          'The Night Listener' : 3.0
                          },
           'Gene Seymour' : {'Lady in the Water' : 3.0,
                          'Snakes on a Plane' : 3.5,
                          'Just My Luck' : 1.5,
                          'Supermen Returns' : 5.,
                          'You, Me and Dupree' : 3.5,
                          'The Night Listener' : 3.0
                          },
           'Michael Phillips' : {'Lady in the Water' : 2.5,
                          'Snakes on a Plane' : 3.,
                          'Supermen Returns' : 3.5,
                          'The Night Listener' : 4.0
                          },
           'Claudia Puig': { 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0,
                         'Supermen Returns': 4.,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 4.5
                         },
           'Mick LaSalle': {'Lady in the Water': 3.,
                         'Snakes on a Plane': 4.,
                         'Just My Luck': 2.0,
                         'Supermen Returns': 3.,
                         'You, Me and Dupree': 2.0,
                         'The Night Listener': 3.0
                         },
           'Jack Matthews': {'Lady in the Water': 3.,
                         'Snakes on a Plane': 4.,
                         'Just My Luck': 3.0,
                         'Supermen Returns': 5,
                         'You, Me and Dupree': 3.5,
                         'The Night Listener': 3.0
                         },
           'Toby': {'Snakes on a Plane': 4.5,
                         'Supermen Returns': 4.,
                         'You, Me and Dupree': 1.0,
                         },

           }

def sim_distance(prefs, person1, person2) :
    # получить список предметов оцененных обоими
    si = {}
    for item in prefs[person1] :
        if item in prefs[person2] :
            si[item] = 1

    # если нет общих оценок то возвращаем 0
    if len(si) == 0 : return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])

    return 1./(1. + sum_of_squares )


def sim_pearson(prefs, person1, person2) :
    # получить список предметов оцененных обоими
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    n = len(si)

    # если нет общих оценок то возвращаем 0
    if n == 0: return 0

    # Вычислить сумму всех предпочтений
    sum1 = sum(prefs[person1][item] for item in si)
    sum2 = sum(prefs[person2][item] for item in si)

    # Вычислить сумму квадратов
    sum1Sq = sum(pow(prefs[person1][item], 2) for item in si)
    sum2Sq = sum(pow(prefs[person2][item], 2) for item in si)

    # сума произведений
    pSum = sum(prefs[person1][item] * prefs[person2][item] for item in si)

    # коэф-т Пирсона
    num = pSum - (sum1 * sum2/n)
    den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))
    if den == 0 : return 0

    r = num / den

    return r