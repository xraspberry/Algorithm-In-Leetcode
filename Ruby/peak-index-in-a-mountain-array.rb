# @param {Integer[]} a
# @return {Integer}
def peak_index_in_mountain_array(a)
  left = 0
  right = a.size
  while left < right
    mid = left + (right - left) / 2
    if a[mid-1] < a[mid] and a[mid] > a[mid+1]
      return mid
    elsif a[mid] >= a[mid-1]
      left = mid+1
    elsif a[mid] >= a[mid+1]
      right = mid
    end
  end
end

p peak_index_in_mountain_array([0,2,1,0])
