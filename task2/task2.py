inp = [[1, 2], [1, 3], [2, 3]]

inp_dict = {}
for i, j in inp:
    inp_dict[i] = inp_dict.get(i, []) + [j]

ans = None 
for i, j in inp_dict.items():
    if len(j) == len(inp)-1:
        if ans is None:
            ans = i
        else:
            break
else:
    if ans is None:
        print("No spies")
    else:
        print(ans)