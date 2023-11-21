# def count_letters(main_str):
#     main_str.lover()
#

from collections import Counter

def calculate_frequency(main_str):
    result = ''.join(main_str.lower().split())

    res = []
    for char in result:
        if char.isalpha():
            res.append(char)
    res = ''.join(res)

    res = Counter(res)
    #print(res)
    return res

def frequency(main_str):
    res = calculate_frequency(main_str)
    sum_ = sum(res.values())    # сумма для частоты
    #print(sum_)

    dict = {}
    for char, key in res.items():

        print(f'{char}: {key/sum_:.2f}')

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# result = ''.join(main_str.lower().split())
# res = []
# for char in result:
#     if char.isalpha():
#         res.append(char)
# res = ''.join(res)
# from collections import Counter
# calculate = Counter(res)
# print(calculate)
#print(main_str.capitalize())
# x = calculate_frequency(mai
#res = calculate_frequency(main_str)
# def frequency(main_str):
#     for char, key in res.items():
#         print(char, key)
#
# # for i,y in calculate.items():
# #     print(i, y)
# #
calculate_frequency(main_str)
frequency(main_str)