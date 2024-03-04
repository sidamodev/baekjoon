N = int(input())
input_lst = list(map(int, input().split()))
M = int(input())
tree = [[] for _ in range(N)]
for i in range(1, N):
    tree[input_lst[i]].append(i)
# tree.pop(M)
cnt = 0
for elem in tree:
    if not elem:
        cnt += 1
print(tree)

def traverse(tree, elem):
    if elem in tree:

    traverse()