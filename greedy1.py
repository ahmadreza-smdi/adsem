import pprint
pp = pprint.PrettyPrinter(indent=4)

def moves(mat):
    """
    Returns a list of all possible moves
    """
    m=eval(mat)
    output = []
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)
    if i > 0:
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];
    if i < 3:
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
    if j > 0:
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
    if j < 3:
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
    return output

def h2(c):
    """
    Manhattan distance
    """
    distance = 0
    m = eval(c)
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - ((m[i][j]-1)/4)) + abs(j -  ((m[i][j]-1)%4))
            # print   abs(i - ((m[i][j]-1)/4)) + abs(j -  ((m[i][j]-1)%4))
    return distance

def greedy(n):
    global expanded,expanded_nodes,goal
    mini=n
    # while mini!=goal:
    m=50
    for i in range(len(moves(n))):
        if moves(n)[i] in expanded:continue
        if h2(moves(n)[i])<m :
            m=h2(moves(n)[i])
            mini=moves(n)[i]
    for y in eval(mini):
        print str(y)+"\n"
    print "===========================\n"
    expanded.append(mini)
    expanded_nodes += 1
    if mini!=goal:
        greedy(mini)


expanded = []
expanded_nodes=0
goal = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])
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

greedy(current)
# print expanded
