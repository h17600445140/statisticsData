
def getdateNum(my_datas, dict) -> int:
    dict_len = len(dict)
    key = [key for key in dict.keys()]
    value = [value for value in dict.values()]
    result = []

    for dict in my_datas:
        for i in range(dict_len):
            if dict[key[i]] != value[i]:
                break
            if i == dict_len - 1 and dict[key[i]] == value[i]:
                result.append(list)
    result_len = len(result)
    return result_len
