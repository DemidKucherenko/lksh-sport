# -*- coding: utf-8 -*-
def is_time(str):
    if (len(str) != 5) or (str[0] not in ['0', '1', '2']) or \
            (not str[1].isdigit()) or (str[3] not in ['0', '1', '2', '3', '4', '5']) or (not str[4].isdigit()):
        return False
    if str[0] == 2:
        return str[1] in ['0', '1', '2', '3']
    return True


def convert_start_time(str):
    assert len(str) == 5
    assert '0' <= str[0] <= '2'
    assert '0' <= str[1] <= '9'
    if str[0] == '2':
        assert '0' <= str[1] <= '3'
    assert '0' <= str[3] <= '5'
    assert '0' <= str[4] <= '9'
    return 60 * int(str[0:2]) + int(str[3:])


def convert_to_time(time):
    h = str(time // 60) if (time >= 600) else "0" + str(time // 60)
    m = str(time % 60) if (time % 60 >= 10) else "0" + str(time % 60)
    return h + ":" + m


def remove_bad_symbol(name):
    return name.replace('ё', 'е')


def is_sport_name(str, sports):
    for sport in sports:
        if sport.name == str:
            return True
    return False


# def transliterate(name):
#     dictionary = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
#               'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
#               'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
#               'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
#               'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#               'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
#               'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'X': 'H',
#               'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
#               'Ю': 'U', 'Я': 'Ya'}
#
#     for key in dictionary:
#         name = name.replace(key, dictionary[key])
#     return name