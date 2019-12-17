# @param {Integer[]} a
# @param {Integer} k
# @return {Integer}
def smallest_range_i(a, k)
  min_a = a.min
  max_a = a.max
  if max_a - min_a < 2 * k
    return 0
  else
    return max_a - k - (min_a + k)
  end
end