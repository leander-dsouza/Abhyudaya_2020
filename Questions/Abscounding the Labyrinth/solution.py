class Solution:
    def calculateMinimumHP(self,mat):
        dp=[[float('inf') for i in range(len(mat[0])+1)] for j in range(len(mat)+1)]
        dp[-1][-2]=1
        dp[-2][-1]=1
        for i in range(len(mat)-1,-1,-1):
            for j in range(len(mat[0])-1,-1,-1):
                dp[i][j]=max(min(dp[i][j+1],dp[i+1][j])-mat[i][j],1)
        return dp[0][0]

arr = input().split(' ')
m = int(arr[0])
n = int(arr[1])
k = Solution()

array_input = []
for x in range(m):
    array_input.append([int(y) for y in input().split()])
print(k.calculateMinimumHP(array_input))
