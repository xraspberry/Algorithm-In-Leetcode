# @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
  sort_heights = heights.sort
  count = 0
  heights.zip(sort_heights) do |height, sort_height|
    if height != sort_height
      count += 1
    end
  end
  return count
end