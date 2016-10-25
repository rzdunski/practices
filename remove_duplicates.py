def remove_duplicates(old_list):
    new_list = []
    for index1 in range(len(old_list)):
        while old_list[index1] not in new_list:
            new_list.append(old_list[index1])

    return new_list

print remove_duplicates([1,1,2,2,3,3,4,4,3,3,2,6])