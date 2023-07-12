def calculate_coins(sum):
    coins = [100, 50, 20, 10, 5, 2, 1]
    result = 0
    result1 = {"100":0, "50":0, "20":0, "10":0, "5":0, "2":0, "1":0}
    sum = sum * 100

    for coin in coins:
        while result + coin <= sum:
            result += coin
            result1[str(coin)] += 1

    return result1

print(calculate_coins(5.6))