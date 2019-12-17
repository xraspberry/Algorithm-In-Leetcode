
# @param {String} s
# @return {String}
def reverse_words(s)
  s_list = s.split(' ')
  s_list.each do |item|
    item.reverse!
  end
  return s_list.join(' ')
end