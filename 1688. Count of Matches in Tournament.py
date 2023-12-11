class Solution:
    def numberOfMatches(self, n: int) -> int:   
        matchesPlayed = 0
        matchPair = 0
        while n > 1:
            if n % 2 == 0:
                matchPair = n / 2
                matchesPlayed = matchesPlayed + matchPair
                n = n - matchPair
            else:
                matchPair = (n - 1) / 2
                matchesPlayed = matchesPlayed + matchPair
                n = n - matchPair
        matchesPlayed = int(matchesPlayed)
        return(matchesPlayed)
