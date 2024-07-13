class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Using default dict to avoid error with initalizing collections
        hash_map = defaultdict()

        # Loops through the initial strings of words
        for word in strs:
            
            '''
            Sorts the words to act as key, sorted() returns a list and lists 
            cannot be keys since they are mutable, get around this by converting
            list into tuple
            '''
            sorted_word = tuple(sorted(word))
            
            # If has map is empty create key for first word
            if(len(hash_map) == 0):
                hash_map[sorted_word] = []
            
            # If key is not in dict, make it and add unsorted word
            if sorted_word not in hash_map:
                hash_map[sorted_word] = []
                hash_map[sorted_word].append(word)
            # If key exists, add unsorted word to key
            else: 
                hash_map[sorted_word].append(word)
        
        return hash_map.values()
        

        
            
        