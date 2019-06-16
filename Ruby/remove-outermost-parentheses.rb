# @param {String} s
# @return {String}
def remove_outer_parentheses(s)
  stack = [s[0]]
  i = 1
  start = 0
  res = ""
  length = s.size
  while i < length
    ele = s[i]
    if stack[-1] == "(" and ele == ")"
      stack.pop
    elsif stack.empty?
      res.concat(s[start+1...i-1])
      start = i
      stack.push(ele)
    else
      stack.push(ele)
    end
    i += 1
  end
  res.concat(s[start+1...length-1])
  return res
end


examples = [
    ["(()())(())", "()()()"],
    ["(()())(())(()(()))", "()()()()(())"],
    ["()()", ""]
]

examples.each do |item|
  res = remove_outer_parentheses(item[0])
  if res == item[1]
    p 'equal'
  else
    p 'unequal'
  end
end
