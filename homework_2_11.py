def calculate_coins(sum):
    coins = [1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    result = 0
    result_before = 0
    string_result = []

    for coin in range(len(coins)):
        for itr in range(len(coins)):
            if result < sum:
                result_before = result
                result += coins[coin]
                

            elif result > sum:
                result = result_before

            else:
                break
    
    return result

print(calculate_coins(5.6))