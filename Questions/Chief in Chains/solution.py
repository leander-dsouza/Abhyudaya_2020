class Solution(object):


    def reconstructQueue(self, people):

        people.sort(key=lambda x: (-x[0], x[1]))

        output = []
        for p in people:
            output.insert(p[1], p)
        return output




m = int(input())

k = Solution()

array_input = []
for x in range(m):
    array_input.append([int(y) for y in input().split()])
gh =k.reconstructQueue(array_input)

for s in gh:
    print(*s)
