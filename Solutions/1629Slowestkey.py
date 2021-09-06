class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        key = keysPressed[0]
        time = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            new_time = releaseTimes[i] - releaseTimes[i-1]
            if new_time > time:
                key = keysPressed[i]
                time = new_time
            elif new_time == time and keysPressed[i] > key:
                    key = keysPressed[i]
        return key
