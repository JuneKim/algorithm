## runtime 42 ms(35.24%), memory 13.8 MB (98.18%)
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        if len(key) == 0:
            return ""
        abckeys = "abcdefghijklmnopqrstuvwxyz"
        di_secret_keys = {}

        idx = 0
        for keyval in key:
            if keyval != " " and not keyval in di_secret_keys.keys():
                print (di_secret_keys)
                di_secret_keys[keyval] = abckeys[idx]
                idx += 1
        return "".join([di_secret_keys[ch] if ch != " " else " " for ch in message])
