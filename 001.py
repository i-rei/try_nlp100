t = list("パタトクカシーー")
ans = []
for i, v in enumerate(t):
    if i % 2 == 0:
        ans.append(v)
print("".join(ans))

# str = "パタトクカシーー"
# print(str[::2]) 先頭から末尾まで移動幅2
