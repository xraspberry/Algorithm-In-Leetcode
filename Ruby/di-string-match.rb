# @param {String} s
# @return {Integer[]}
def di_string_match(s)
  nums = (0..s.size).to_a
  res = []
  s.each_char do |item|
    if item == "I"
      res.push(nums.shift)
    else
      res.push(nums.pop)
    end
  end
  res.concat(nums)
  return res
end
