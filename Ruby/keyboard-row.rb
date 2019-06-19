# @param {String[]} words
# @return {String[]}

line_1 = "qwertyuiop"
line_2 = "asdfghjkl"
line_3 = "zxcvbnm"
$word_map = {}
line_1.each_char do |item|
  $word_map[item] = 1
end
line_2.each_char do |item|
  $word_map[item] = 2
end
line_3.each_char do |item|
  $word_map[item] = 3
end

def find_words(words)
  res = []
  words.each do |item|
    if same_line(item)
      res.push(item)
    end
  end
  return res
end


def same_line(item)
  line = 0
  item.each_char{|s|
    s = s.downcase
    if line == 0
      line = $word_map[s]
    elsif line != $word_map[s]
      return false
    end
  }
  return true
end

p find_words(["Hello","Alaska","Dad","Peace"])


def find_words1(words)
  a = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
  words.select do |word|
    s = word.downcase
    s.delete(a[0]).empty? || s.delete(a[1]).empty? || s.delete(a[2]).empty?
  end
end