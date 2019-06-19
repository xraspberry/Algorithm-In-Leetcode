
# @param {Integer[]} a
# @return {Integer[]}
def sort_array_by_parity(a)
  res = []
  a.each do |item|
    if item % 2 == 0
      res.unshift(item)
    else
      res.push(item)
    end
  end
  return res
end

def sort_array_by_parity1(a)
  i = 0
  j = a.size - 1
  while i < j
    while i < j and a[i] % 2 == 0
      i += 1
    end
    while i < j and a[j] % 2 != 0
      j -= 1
    end
    if i >= j
      break
    end
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1
  end
end