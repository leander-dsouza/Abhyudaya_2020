class Solution:
    def maxUncrossedLines(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return 0

        T = [[0 for _ in B] for _ in A]

        T[0][0] = int(A[0] == B[0])
        for j in range(1, len(B)):
            T[0][j] = max(T[0][j - 1], int(A[0] == B[j]))

        for i in range(1, len(A)):
            T[i][0] = max(T[i - 1][0], int(A[i] == B[0]))
            for j in range(1, len(B)):
                T[i][j] = max(T[i - 1][j], T[i - 1][j - 1] + int(A[i] == B[j]), T[i][j - 1])

        return T[-1][-1]

k = Solution()

arr = input().split(' ')
m = int(arr[0])
n = int(arr[1])

A = input().split(' ')
B = input().split(' ')

A = [int(i) for i in A]
B = [int(i) for i in B]

print(k.maxUncrossedLines(A,B))
