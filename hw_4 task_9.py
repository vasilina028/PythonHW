dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

def mix(dict1, dict2):
    result = {**dict1, **dict2}
    for key in result:
        if key in dict1 and key in dict2:
            result[key] = [dict1[key], dict2[key]]
    return result

m = mix(dict1, dict2)
print(m)