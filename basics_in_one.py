from collections import deque , defaultdict

dict_ = {

    "a":["b", "c"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]

    }


stack = ["a"]
#dfs traversal 
while stack:
    curr = stack.pop()
    #print(curr)
    
    for i in range(len(dict_[curr])):
        stack.append(dict_[curr][i])




#recurssive for dfs


source = "a"
def dfs(dict_ , source):
    print(source)
    if not source:
        return 
    for i in dict_[source]:
        dfs(dict_ , i)


#dfs(dict_ , source)










#bsf traversal- using queue



dq = deque()


source = "a"

dq.append(source)

while dq:
    curr = dq.popleft()
    #print(curr)
    for i in range(len(dict_[curr])):
        dq.append(dict_[curr][i])







adj = {
    'f':['g' , 'i'],
    'g':['h'],
    'h':[],
    'i':['g' , 'k'],
    'j':['i'],
    'k':[]

    }

source , dest = 'f' , 'k'
found = False
# dfs  approach on how to get the path from one node to another with in the graph

def hasPath(adj , source, dest ):
    
  
    if source == dest:
        return True

   
        
        
    
    for i in adj[source]:
        
            
        if hasPath(adj , i , dest):
            return True
        



#print(hasPath(adj , source, dest) == True)
#bfs approach on how to get the path from one node to another with in the graph
dq = deque()
dq.append(source)

def bsf(dest):
    while dq:
        curr = dq.popleft()
        if curr == dest:
            return True
        for i in range(len(adj[curr])):
            dq.append(adj[curr][i])

    return False
print(bsf(dest))


    



#Problem - Undirected Path - determining whether there exist a path for undirected graph

#edge lists for undirected one - which is bidirectional in either way
edges = [['i' , 'j'] , ['k' , 'i'] , ['m', 'k'] , ['k' , 'l'] , ['o' , 'n']]

adj = defaultdict(list)

for i in edges:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])

#finished setting up the adjecency list
visited = set()
src = 'l'
dest = 'm'
def dfs(src , dest):
    visited.add(src)
    if src == dest:
        return True
    for i in adj[src]:
        if i in visited:
            continue
        else:
            if dfs(i , dest):
                return True

print(dfs(src , dest) == True)





# Problem - count the number of the components from the given adjecency lists


adj = {
   1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]


    }


count = 0
visited = set()

def dfs(adj , curr):
   
    if curr in visited:
        return 0
    count = 1
    visited.add(curr)
    for i in adj[curr]:
        count += dfs(adj , i)

    return count
    
    

   
max_ = 0
for i in adj:
    val = dfs(adj , i)
    max_ = max(max_ , val)
    
    
    


#print(max_)










#Shortest path
q = deque()

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
];
start = 'y'
end = 'x'
counter = 0

adj = defaultdict(list)
for i in range(len(edges)):
    adj[edges[i][0]].append(edges[i][1])
    adj[edges[i][1]].append(edges[i][0])



q.append((start , 0))
while q:

    curr = q.popleft()
 
    val , count = curr
    if val == end:
         counter = count
         break
    for i in adj[val]:
        q.append((i  , count + 1))
#print(counter)
    
visited = set()
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if explore(grid , i , j):
            count+=1

            



def explore(grid , r , c):
    rowBounded, colBounded = 0 <= r < len(grid), 0 <= c < len(grid[0])
    if not rowBounded or not colBounded:
        return False
    if (r,c) in visited:
        return False
    visited.add((r , c))



    explore(grid , r - 1 , c)
    explore(grid , r + 1  , c)
    explore(grid , r , c - 1)
    explore(grid , r , c + 1)

    return True


    

print(count)
        




















