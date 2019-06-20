# @param {String[]} a
# @return {Integer}
def min_deletion_size(a)
  # 将所有需要删除的删除掉，就可以了
  # 也就是相当于统计下降序的列数
  row = a.size
  col = a[0].size
  deleted = 0
  for j in 0...col
    for i in 1...row
      if a[i][j] < a[i-1][j]
        deleted += 1
        break
      end
    end
  end
  return deleted
end

p min_deletion_size(["rrjk","furt","guzm"])


def min_deletion_size1(a)
  ans = 0
  n = a[0].size
  m = a.size - 1
  n.times do |i|
    m.times do |j|
      if a[j][i] > a[j+1][i]
        ans += 1
        break
      end
    end
  end
  ans
end