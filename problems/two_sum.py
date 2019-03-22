# num, target = [2, 7, 11, 15], 9

# num, target = [3, 2, 4], 6

num, target = [3, 3], 6

num_restruct = list(range(len(num)))
a = [[x, y] for x in num_restruct for y in num_restruct if not x == y]

first_idx, second_idx = None, None
for n in a:
    if sum([num[n[0]], num[n[1]]]) == target:
        print([n[0], n[1]])

print(first_idx, second_idx)
