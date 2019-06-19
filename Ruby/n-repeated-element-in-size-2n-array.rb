# @param {Integer[]} a
# @return {Integer}
def repeated_n_times(a)
  # 这道题用哈希表当然可以做，但是可以有更trick的方法
  # 因为2N个数组，至少有N次重复，那么将数组排序后
  # 重复元素一定在最中间元素左边或者右边
  a.sort!
  if a[a.size/2] == a[a.size/2 + 1]
    return a[a.size/2]
  else
    return a[a.size/2-1]
  end
end
