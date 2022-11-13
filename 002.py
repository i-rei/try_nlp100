t1 = "パトカー"
t2 = "タクシー"
ans = []
for i in range(4):
    ans.append(t1[i])
    ans.append(t2[i])
print("".join(ans))

# ans = "".join([i + j in zip(t1, t2)])
