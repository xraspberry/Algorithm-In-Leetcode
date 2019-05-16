def method_1(array):
    """
    通过排序的办法
    :return:
    """
    if len(array) <= 1:
        return False, None
    sorted_array = sorted(array)
    for idx, item in enumerate(sorted_array[1:], 1):
        if item == sorted_array[idx-1]:
            return True, item
    return False, None


def method_2(array):
    """
    通过哈希表
    :param array:
    :return:
    """
    if len(array) <= 1:
        return False, None
    itered = set()
    for item in array:
        if item not in itered:
            itered.add(item)
        else:
            return True, item
    return False, None


def method_3(array):
    """
    书中重点讲到的部分，通过交换数字，基于如果没有重复数字的话，数组下标i应该等于实际存储的元素
    所以遍历过程中，将没有在对应下标的数字挪到相应的位置，如果相应位置已经有对应元素的话，就说明重复
    :param array:
    :return:
    """
    if len(array) <= 1:
        return False, None
    for item in array:
        if item < 0 or item > len(array) - 1:
            return False, None
    for idx in range(len(array)):
        while idx != array[idx]:
            # 如果对应下标的数据已经等于item，说明有重复
            if array[array[idx]] == array[idx]:
                return True, array[idx]
            # 否则将其和对应下标数据交换
            temp = array[idx]
            array[idx] = array[temp]
            array[temp] = temp
    return False, None


if __name__ == '__main__':
    array = [2, 3, 1, 0, 2, 5, 3]
    found, item = method_1(array)
    assert found is True
    print("found dup item is: {}".format(item))

    found, item = method_2(array)
    assert found is True
    print("found dup item is: {}".format(item))

    found, item = method_3(array)
    assert found is True
    print("found dup item is: {}".format(item))
