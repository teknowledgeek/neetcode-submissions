class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s) + 1

        wordBreakList = [False]* n
        wordBreakList[0] = True

        for i in range(n):
            for word in wordDict:
                wl = len(word)
                print(word , s[max(0,i -wl):i])
                if word == s[max(0,i -wl):i]:
                    prev = i - wl 
                    print(prev, i)
                    wordBreakList[i] = wordBreakList[prev]
                if wordBreakList[i]:
                    break
        print(len(wordBreakList))
        return wordBreakList[n-1]
        