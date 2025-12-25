items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):

    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - cost] + calories
                )
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(names[i - 1])
            w -= items[names[i - 1]]["cost"]

    return result[::-1], dp[n][budget]



budget = 100

greedy_result, greedy_cal = greedy_algorithm(items, budget)
dp_result, dp_cal = dynamic_programming(items, budget)

print("Бюджет:", budget)
print("Жадібний алгоритм:", greedy_result, "Калорії:", greedy_cal)
print("Динамічне програмування:", dp_result, "Калорії:", dp_cal)
