def find_common_participants(first, second, seperator=','):
    first_list_participants = first.split(seperator)
    second_list_participants = second.split(seperator)
    first_list_participants = set(first_list_participants)
    list_common_participants = list(first_list_participants.intersection(second_list_participants))
    list_common_participants.sort()
    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, "|"))
