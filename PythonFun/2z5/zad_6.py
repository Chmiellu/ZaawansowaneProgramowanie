def final_list(list1: list, list2: list) -> list:
    merged_list = list(set(list1 + list2))
    processed_list = [x ** 3 for x in merged_list]
    return processed_list

list1 = [9, 92, 11]
list2 = [0, 1000, 11]
result = final_list(list1, list2)
print(result)
