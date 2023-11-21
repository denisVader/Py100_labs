def find_common_participants(participants_first_group,participants_second_group,arg=","):
    new_participants_first_group = participants_first_group.split(arg)
    new_participants_second_group = participants_second_group.split(arg)
    result = list(set(new_participants_first_group).intersection(new_participants_second_group))
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
res = find_common_participants(participants_first_group, participants_second_group,arg="|")
print(res)

# TODO Провеьте работу функции с разделителем отличным от запятой
