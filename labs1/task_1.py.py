numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0  # Меняе значение None на 0, для вычесленя среднего без ошибки
sum(numbers)
len(numbers)

average = sum(numbers) / len(numbers)  # Вычисляем  среднее значение

numbers[4] = average

print("Измененный список:", numbers)
