import random
import matplotlib.pyplot as plt

rolls = 100000

results = {i: 0 for i in range(2, 13)}

for _ in range(rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    results[total] += 1

probabilities = {k: v / rolls for k, v in results.items()}


print("Сума | Ймовірність (Монте-Карло)|")
for k in probabilities:
    print(f"{k:>4} | {probabilities[k]:.4f}")

plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Ймовірность сум при киданні двох кубиків (метод Монте-Карло)")
plt.show()
