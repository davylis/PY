def second_largest(list1):
    distinct=sorted(set(list1))

    if len(distinct)<2:
        return None

    return distinct[-2]