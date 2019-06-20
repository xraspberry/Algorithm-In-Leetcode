# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
  nums.sort!
  res = 0
  nums.each_with_index do |n, index|
    if index % 2 == 0
      res += n
    end
  end
  return res
end

p array_pair_sum([1,1])