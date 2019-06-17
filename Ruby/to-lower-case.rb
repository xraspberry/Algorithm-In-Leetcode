# @param {String} str
# @return {String}
def to_lower_case(str)
  res = ""
  str.each_char do |item|
    item_ord = item.ord
    if 65 <= item_ord and item_ord <= 90
      res.concat((item_ord + 32).chr)
    else
      res.concat(item)
    end
  end
  return res
end

def to_lower_case1(str)
  return str.downcase
end

res = to_lower_case1("ABc")
p res