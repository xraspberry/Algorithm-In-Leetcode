# @param {Integer[]} a
# @return {Integer[]}
def sorted_squares(a)
  a.map!{|item| item ** 2}
  a.sort!
  return a
end