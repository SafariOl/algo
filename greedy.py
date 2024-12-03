def max_activities(activities):
    # Сортуємо заявки за часом закінчення
    sorted_activities = sorted(activities, key=lambda x: x[1])

    # Обираємо першу заявку
    selected_activities = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]

    # Проходимо по всіх заявках і вибираємо ті, які не перетинаються з обраними
    for i in range(1, len(sorted_activities)):
        if sorted_activities[i][0] >= last_finish_time:
            selected_activities.append(sorted_activities[i])
            last_finish_time = sorted_activities[i][1]

    return selected_activities

# Вхідні дані: список заявок (початок, закінчення)
activities = [(3, 5), (0, 6), (12, 14), (2, 3), (8, 12), (8, 11), (1, 3), (5, 7), (5, 9), (6, 10), (7, 8)]

# Знаходимо максимальну кількість заявок, які можна задовольнити
selected_activities = max_activities(activities)

print(f"Максимальна кількість заявок: {len(selected_activities)}")
print("Обрані заявки:")
for activity in selected_activities:
    print(activity)