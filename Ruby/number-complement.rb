# @param {Integer} num
# @return {Integer}
def find_complement(num)
  res = ""
  num.to_s(2).each_char do |item|
    res.concat(item == "1" ? "0" : "1")
  end
  return res.to_i(2)
end

p find_complement(1)
