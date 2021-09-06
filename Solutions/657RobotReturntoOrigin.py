class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Time - O(n), Space -O(1)
        # return (moves.count('R') == moves.count('L'))  & (moves.count('U') == moves.count('D'))
        directions = {'L' : [-1,0], 'R': [1,0], 'U': [0,1], 'D': [0,-1]}
        x, y = 0,0
        for move in moves:
            x = x + directions[move][0]
            y = y + directions[move][1]
            
        if x ==0 and y ==0:
            return True
        return False
            
            
