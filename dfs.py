from collections import defaultdict
import resource
import sys

#set rescursion limit and stack size limit
# sys.setrecursionlimit(10 ** 6)
# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class Tracker(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes.
    
    'self.leader' is in the form of {node: leader, ...}."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()



def read_graph(input_file, reverse=False):

    graph = defaultdict(list)
    with open('SCC.txt') as file_in:
        for line in file_in:
            x = line.strip().split()
            x1, x2 = int(x[0]), int(x[1])
            graph[x1].append(x2)
    return graph

def graph_reverse(graph):
    """Given a directed graph in forms of {tail:[head_list], ...}, compute
    a reversed directed graph, in which every edge changes direction."""

    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph


def dfs(graph_dict, node, tracker):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail: [head_list], ...}. Depth first search runs recursively and keeps
    track of the parameters"""
    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time

def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""
    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)

def main():
    filename = 'SCC.txt'
    #filename = 'test2.txt'
    G = read_graph(filename)



if __name__ == '__main__':
    main()