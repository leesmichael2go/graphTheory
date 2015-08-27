# Implementing graphs; https://www.python.org/doc/essays/graphs/
# Graphs with directed edges ('arcs')
graph = { 'A':['B','C'],
          'B':['C','D'],
          'C':['D'],
          'D':['C'],
          'E':['F'],
          'F':['C']}

# Basion function to determine path btw two nodes, which takes graph, start, end as args
# Retuns a list of nodes including start and end making up the path
# If no path, return None
# No cycles within the path returned

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
        return None

# Slight change to function to find all paths, not just the one first seen
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Finding shortest path
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest