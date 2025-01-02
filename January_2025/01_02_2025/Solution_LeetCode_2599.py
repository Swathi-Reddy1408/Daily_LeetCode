class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set(['a','e', 'i', 'o', 'u'])
        prefix_sum = [0] * (len(words))
        ans = []
        
        def isGoodWord(word):
            flag = False
            if word[0] in vowel_set and word[-1] in vowel_set:
                flag = True
            return flag
        sum = 0
        for i in range(0, len(words)):
            if isGoodWord(words[i]):
                sum += 1
            prefix_sum[i] = sum

        for [start, end] in queries:
            if start == 0:
                ans.append(prefix_sum[end])
            else:
                ans.append(prefix_sum[end] - prefix_sum[start-1])
        return ans
        
            

        