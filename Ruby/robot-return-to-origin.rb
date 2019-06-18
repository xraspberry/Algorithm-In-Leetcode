# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
  move_map = {
      "U" => [0, 1],
      "D" => [0, -1],
      "L" => [-1, 0],
      "R" => [1, 0]
  }
  origin = [0, 0]
  moves.each_char do |item|
    move_step = move_map[item]
    origin[0] += move_step[0]
    origin[1] += move_step[1]
  end
  return origin == [0, 0]
end

def judge_circle1(moves)
  return moves.count('U') == moves.count('D') && moves.count('L') == moves.count('R')
end