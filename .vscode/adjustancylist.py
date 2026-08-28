n=4
adj_list=[[] for i in range(n)]
edges=[(0,1),(0,2),(1,2),(2,3)]
for v,e in edges:
    adj_list[e].append(v)
    adj_list[v].append(e)
for i in range(n):
    print(i,"->",adj_list[i])