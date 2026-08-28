n=4
adjmatrix=[[0]*n for i in range(n)]
edges=[(0,1),(0,2),(1,2),(2,3)]
for v,e in edges:
    adjmatrix[e][v]=1
    adjmatrix[v][e]=1
for i in adjmatrix:
    print(i)