def bfs(current,goal):
    leaf = [[current]]
    expanded = []
    expanded_nodes=0
    while leaf:
        i = 0
        for j in range(1, len(leaf)):
            if len(leaf[i]) > len(leaf[j]):
                i = j
        path = leaf[i]
        leaf = leaf[:i] + leaf[i+1:]    #DELETE THE LEAF HAS BEEN SELECTED FROM LEAVES
        endnode = path[-1]
        if endnode in expanded: continue
        for k in moves_possible(endnode):
            if k in expanded: continue
            leaf.append(path + [k])
        expanded.append(endnode)
        expanded_nodes += 1
        if endnode == goal: break
    print ("Expanded nodes:",expanded_nodes)
    return path
# ================================================================================
def moves_possible(m):
    output = []
    matrix = eval(m)
    i = 0
    while 0 not in matrix[i]: i += 1
    j = matrix[i].index(0)

    if j > 0:
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]   #left
      output.append(str(matrix))
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]

    if j < 3:
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]   #right
      output.append(str(matrix))
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

    if i > 0:
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j];  #up
      output.append(str(matrix))
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j];

    if i < 3:
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]   #down
      output.append(str(matrix))
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

    return output
# ================================================================
"""
READ FROM FILE
"""
current = []
for line in open('test.txt').readlines():
    l1=line.split()
    l2=[]
    for x in l1:
        l2.append(int(x))
    current.append(l2)
current=str(current)

goal = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])

path = bfs(current,goal)
print ("Solution:")
for x in path:
    for y in eval(x):
        print str(y)+"\n"
    print "\n"
