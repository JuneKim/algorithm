## runtime: 50.88%, memory: 42.57%
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {"b": 1, "a": 1, "l": 2, "o":2, "n":1}
        target = {"b": 0, "a": 0, "l": 0, "o": 0, "n":0}
        for ch in text:
            if ch in balloon.keys():
                target[ch] += 1

        minVal = min(target.values())
        continued = True
        myCnt = 0
        for _ in range(minVal):
            for key, val in balloon.items():
                if target[key] >= balloon[key]:
                    target[key] -= balloon[key]
                else:
                    continued = False
                    break

            if continued:
                myCnt += 1
        
        return myCnt
