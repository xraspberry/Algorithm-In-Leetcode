"""
剑指offer第2章 面试题3 二维数组中的查找
"""


def find_ele_in_array(array, ele):
    """数组规律是向右向下增大，所以可以找中间的数字然后就可以排除了
    比如9，如果要找的数字比9小，那么就可以排除1列，因为在第一列9是最小的
    如果要找的数字比9大，那么就可以排除1行，因为在第一行9是最大的
    同理也可以找6，由此可见，要找到中间数字，这样容易进行排除"""
    # 右上角的元素坐标
    if not array:
        return False
    columns = len(array[0])
    rows = len(array)

    # 从第一行开始迭代
    # 迭代条件是扫描的行row 必须小于 总行数，并且列数往回缩必须大于等于0
    # 用行号和列号来查找，这样避免删除数组元素这个不优雅的过程
    # 先从右上角的元素开始
    row = 0
    column = columns - 1
    while row < rows and column >= 0:
        find_ele = array[row][column]
        if find_ele == ele:
            return True
        elif find_ele > ele:
            column -= 1
        else:
            row += 1
    return False


def find_ele_in_array_left(array, ele):
    """从左下角开始寻找"""
    if not array:
        return False
    rows = len(array)
    columns = len(array[0])

    # 从最后一行，第一列开始
    row = rows - 1
    column = 0
    while column < columns and row >= 0:
        find_ele = array[row][column]
        if find_ele == ele:
            return True
        elif find_ele > ele:
            row -= 1
        else:
            column += 1
    return False


if __name__ == "__main__":
    test_array = [[1, 2, 8, 9],
                  [2, 4, 9, 12],
                  [4, 7, 10, 13],
                  [6, 8, 11, 15]]
    test_search_ele1 = 7
    test_search_ele2 = 5

    # 从右上角开始寻找
    assert find_ele_in_array(test_array, test_search_ele1)
    assert not find_ele_in_array(test_array, test_search_ele2)

    # 从左下角开始寻找
    assert find_ele_in_array_left(test_array, test_search_ele1)
    assert not find_ele_in_array_left(test_array, test_search_ele2)

    test_array = []
    assert not find_ele_in_array(test_array, test_search_ele2)
    assert not find_ele_in_array_left(test_array, test_search_ele2)

