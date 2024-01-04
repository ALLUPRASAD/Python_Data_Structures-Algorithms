class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=[c for c in jewels]
        s=[k for k in stones]
        total=0
        for jew in j:
            if jew in s:
                total=total+int(s.count(jew))
            if len(j)<=1:
                if jew not in s:
                    return 0
            if len(s)<=1:
                if jew not in s:
                    return 0
                

        return total
