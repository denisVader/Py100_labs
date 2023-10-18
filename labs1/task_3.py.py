list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Разделить участников на две команды.
middle_value = len(list_players) // 2
left_team = list_players[:middle_value]
right_team = list_players[middle_value:]

# Вывести на экран
print(left_team)
print(right_team)
