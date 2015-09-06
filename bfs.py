#https://www.hackerrank.com/challenges/bfsshortreach
T = int(input())
t = 0
while t < T:
    N,M = [int(x) for x in input().split()]
    from collections import defaultdict
    adjL = defaultdict(list)
    for i in range(1,N+1):
        adjL[i].append(i)
        adjL[i].remove(i)
    for i in range(0,M):
        x,y = [int(x) for x in input().split()]
        adjL[x].append(y)
        adjL[y].append(x)
    s = int(input())
    
    visited = {}
    weights = {}
    
    def bfs(s, adj):
        for i in range(1,len(adj)+1):
            visited[i]=False
            weights[i]=float("inf")
        from collections import deque
        itr = 0
        q = deque(maxlen=len(adj))
        visited[s] = True
        weights[s] = itr
        q.append(s)
        while(len(q)>0):
            x = q.popleft()
            for y in adj[x]:
                if not visited[y]:
                    visited[y] = True
                    weights[y] = weights[x] + 1
                    q.append(y)
                else:
                    continue
    
    bfs(s,adjL)            
    weights = list(weights.values())
    weights.remove(0)
    for i in range(0,len(weights)):
        weights[i] = weights[i]*6
    toprint = ''
    for i in weights:
        if i > 0:
            if i != float("inf"):
                toprint += str(i) + " "
            else:
                toprint += "-1 "
    toprint.strip()
    print(toprint)
    t += 1

        


            
