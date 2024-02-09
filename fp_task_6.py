def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            total_cost += item_info['cost']
            total_calories += item_info['calories']
            selected_items.append(item_name)

    return {"selected_items": selected_items, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, item_info = list(items.items())[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, _ = list(items.items())[i - 1]
            selected_items.append(item_name)
            j -= items[item_name]['cost']

    return {"selected_items": selected_items, "total_cost": budget - j, "total_calories": dp[n][budget]}


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Greedy Algorithm:")
print(greedy_algorithm(items, budget))
print("\nDynamic Programming:")
print(dynamic_programming(items, budget))
