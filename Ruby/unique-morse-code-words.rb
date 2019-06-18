# @param {String[]} words
# @return {Integer}
def unique_morse_representations(words)
  word_map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
  morse = []
  words.each do |item|
    morse_res = ""
    item.each_char do |item_char|
      morse_res << word_map[item_char.ord - 97]
    end
    if !morse.include?(morse_res)
      morse.push(morse_res)
    end
  end
  return morse.size
end

words = ["gin", "zen", "gig", "msg"]
times = unique_morse_representations(words)
p times