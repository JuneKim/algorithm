class Solution:
    def countBits(self, n: int):
        _answers = []
        for idx in range(n+1):
            _cnt = 0
            _remain = idx
            while _remain > 0:
                if _remain % 2 == 1:
                    _cnt += 1
                _remain //= 2
            _answers.append(_cnt)
        return _answers
    
s = Solution()
print (s.countBits(5))