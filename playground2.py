class Solution:
    def getRange(self,arr,target):
        a = arr.count(target)
        b = arr.index(target)
        print(b,b + a)
arr = [1,2,2,3,3,3,3,3,3,4,5]
x = 3
print(Solution().getRange(arr,x))
