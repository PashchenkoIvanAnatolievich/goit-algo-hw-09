import timeit

# --- ЗАВДАННЯ 1: ЖАДІБНИЙ АЛГОРИТМ ---

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin
            
    return result


# --- ЗАВДАННЯ 2: АЛГОРИТМ ДИНАМІЧНОГО ПРОГРАМУВАННЯ ---

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [float('inf')] * (amount + 1)
    last_coin_used = [0] * (amount + 1)
    
    min_coins[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if 1 + min_coins[i - coin] < min_coins[i]:
                    min_coins[i] = 1 + min_coins[i - coin]
                    last_coin_used[i] = coin
            else:
                break 
                
    if min_coins[amount] == float('inf'):
        return {} 

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin
        
    return result



test_amount = 113
large_amount = 12345

print("--- Тестування на сумі 113 ---")
print(f"Жадібний алгоритм: {find_coins_greedy(test_amount)}")
print(f"Динамічне програмування: {find_min_coins(test_amount)}")
print("-" * 40)

print(f"--- Порівняння ефективності на великій сумі {large_amount} ---")

greedy_time = timeit.timeit(lambda: find_coins_greedy(large_amount), number=1000)
print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} сек")

dp_time = timeit.timeit(lambda: find_min_coins(large_amount), number=10)
print(f"Час виконання ДП (на 10 запусках): {dp_time:.6f} сек")
print(f"Приблизний час на один запуск ДП: {dp_time/10:.6f} сек")