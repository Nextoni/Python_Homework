def what_is_my_sign(day, month):
    result = ""
    signs = [22, 20, 12, 1, "capricorn"], [21, 19, 1, 2, "aquarius"], [20, 20, 2, 3, "pisces"], [21, 20, 3, 4, "aries"], [21, 21, 4, 5, "taurus"], [22, 21, 5, 6, "gemini"], [22, 22, 6, 7, "cancer"], [23, 22, 7, 8, "leo"], [23, 23, 8, 9, "virgo"], [24, 23, 9, 10, "libra"], [24, 22, 10, 11, "scorpio"], [23, 21, 11, 12, "sagittarius"]
    month = month - 1

    for sgn in range(len(signs)):
        if signs[sgn][1] <= day >= signs[sgn][0] and signs[sgn][2] <= month >= signs[sgn][3]:
            result = signs[sgn][4]
            

    return result

print(what_is_my_sign(26, 4))
    