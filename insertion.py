def insertion_sort_desc(arr):
    # Лічильник порівнянь
    comparison_count = 0
    
    # Перебираємо масив починаючи з другого елемента
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Переміщуємо елементи, що більші за key, на одну позицію вправо
        while j >= 0 and arr[j] < key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparison_count += 1  # останнє порівняння коли while завершується
        arr[j + 1] = key

    return arr, comparison_count

# Вхідний масив
arr = [1, 4, 6, 7, 8, 10, 15]

# Сортування у порядку спадання
sorted_arr, comparison_count = insertion_sort_desc(arr)
print("Відсортований масив (спадання):", sorted_arr)
print("Кількість порівнянь:", comparison_count)
