player_1 = [2, -4, 3, 5, 6, 1, 4]
player_2 = [-4, 5, 6, 2, -9, 4, 1]
player_3 = [9, 3, 2, -2, 4, 2, -4]
player_4 = [4, 3, 4, -5, -6, 3, -2]


def maxProductCal(list_player):
    x = 0
    produts = []
    productSet = {}
    for i in range(len(list_player) - 1):
        produts.append(list_player[i] * list_player[i + 1])
        max = 0
        for x in produts:
            if(max > x):
                max = max
            else:
                max = x


    return max

print('player_1 ', '=', maxProductCal(player_1))
print('player_2 ', '=', maxProductCal(player_2))
print('player_3 ', '=', maxProductCal(player_3))
print('player_4 ', '=', maxProductCal(player_4))

