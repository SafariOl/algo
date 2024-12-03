import numpy as np

def find_max_reward(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = np.zeros((rows, cols), dtype=int)

    # Початкове значення (нижній лівий кут)
    dp[rows-1][0] = matrix[rows-1][0]

    # Заповнюємо таблицю знизу вгору і зліва направо
    for i in range(rows-1, -1, -1):
        for j in range(cols):
            if i == rows-1 and j == 0:
                continue
            max_prev = float('-inf')
            # Рухаємося вверх
            if i < rows - 1:
                max_prev = max(max_prev, dp[i+1][j])
            # Рухаємося вліво
            if j > 0:
                max_prev = max(max_prev, dp[i][j-1])
            # Рухаємося по діагоналі
            if i < rows - 1 and j > 0:
                max_prev = max(max_prev, dp[i+1][j-1])
            
            dp[i][j] = matrix[i][j] + max_prev

    # Максимальна сума призів в верхньому правому куті
    return dp[0][cols-1]

# Вхідна таблиця
matrix = [
    [-1, 5, -2, 4, -2, 3, 2],
    [2, -1, 3, -2, 2, 1, -3],
    [3, 1, -2, 4, -2, 3, 4],
    [-1, 3, -2, -1, 4, -2, 1],
    [3, -2, 2, -1, 2, 3, -2],
    [-1, 1, -3, 2, -3, 1, -1],
    [3, -3, -2, 3, 1, 4, -1],
]

max_reward = find_max_reward(matrix)
print(max_reward)