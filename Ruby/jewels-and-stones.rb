# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
  count = Hash.new(0)
  s.each_char do |item|
    count[item] += 1
  end
  res = 0
  j.each_char do |item|
    if count.key?(item)
      res += count[item]
    end
  end
  return res
end


def num_jewels_in_stones1(j, s)
  s.count(j)
end


J = "aA"
S = "aAAbbbb"
res = num_jewels_in_stones1(J, S)
p res
