class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_cord = {
            "L": (-1, 0),
            "R": (1, 0),
            "U": (0, 1),
            "D": (0, -1)
        }
        
        pos = (0, 0)
        for move in moves:
            move_pos = move_cord.get(move, (0, 0))
            pos = pos[0] + move_pos[0], pos[1] + move_pos[1]
        
        return pos[0] == 0 and pos[1] == 0


class Solution2:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')