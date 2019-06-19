# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def self_dividing_numbers(left, right)
  nums = left..right
  nums = nums.select do |num|
    cond = true
    old_num = num
    while num > 0
      ans = num.divmod(10)
      num, remain = ans[0], ans[1]
      if remain != 0 and old_num % remain != 0
        cond = false
        break
      elsif remain == 0
        cond = false
        break
      end
    end
    cond
  end
  return nums
end

self_dividing_numbers(1, 22)