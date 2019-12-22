class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # sliding window
        n = len(s)
        cnt = collections.Counter()

        for i in range(n - minSize + 1):
            sub = s[i: i + minSize]
            tmp = collections.Counter(sub)
            
            if len(tmp) <= maxLetters:
                cnt[sub] += 1
        
        return max(cnt.values()) if cnt else 0
        