class Solution(object):
   def Strive_School(self, n):
      result = []
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("Strive School")
         elif i %3==0:
            result.append("Strive")
         elif i% 5 == 0:
            result.append("School")
         else:
            result.append(str(i))
      return result
ob1 = Solution()
print(ob1.Strive_School(30))