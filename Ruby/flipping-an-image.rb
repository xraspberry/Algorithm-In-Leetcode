# @param {Integer[][]} a
# @return {Integer[][]}
def flip_and_invert_image(a)
  row_len = a.size
  col_len = a[0].size
  i = 0
  while i < row_len
    a[i].reverse!
    j = 0
    while j < col_len
      a[i][j] = a[i][j] == 1 ? 0 : 1
      j += 1
    end
    i += 1
  end
  return a
end
