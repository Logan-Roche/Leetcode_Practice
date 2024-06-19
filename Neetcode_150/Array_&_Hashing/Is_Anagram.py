class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Solution 1
        
        # Checks if length of strings are equal
        if len(s) != len(t):
            return False

        # Creates HashMap of counts of letters
        countS, countT = {}, {}

        # Runs through the length of strings, add to the counts of each letter
        for n in range(len(s)):
            countS[s[n]] = 1 + countS.get(s[n], 0)
            countT[t[n]] = 1 + countT.get(t[n], 0)

        # Checks to see if Hashmaps are equal
        for n in countS:
            if countS[n] != countT.get(n, 0):
                return False

        return True
        
        
        # Solution 2

        # Sorts strings and check if they are the same, Cleaver
        return sorted(s) == sorted(t)
        

        