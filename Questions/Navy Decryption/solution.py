class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    if i > 0 and j > 0 and matrix[i - 1][j] == 1 and matrix[i][j - 1] == 1 and matrix[i - 1][
                        j - 1] == 1:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    res += dp[i][j]

        return res


k = Solution()

arr = input().split(' ')
m = int(arr[0])
n = int(arr[1])

array_input = []
for x in range(m):
    array_input.append([int(y) for y in input().split()])
print(k.countSquares(array_input))
