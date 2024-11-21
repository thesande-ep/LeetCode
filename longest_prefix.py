class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

        if not strs:
          return ""
        
        prefix = strs[0]
        for i in range(1, len(strs)):
          while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            print(prefix)
            if not prefix:
              return ""
        
        return prefix
    
arr = ["flower", "flow", "flowless", "flour"]
# arr = ["rose", "marigold", "lily", "lotus"]


p1 = Solution()
store = p1.longestCommonPrefix(arr)
print(store)