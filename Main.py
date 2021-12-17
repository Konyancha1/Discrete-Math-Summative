# Import libraries
import sys
import random
import matplotlib.pyplot as plt
import networkx
from networkx.generators.random_graphs import erdos_renyi_graph


# Function to get graph path
def dfs(u, graph, visited_edge, path=[]):
    path = path + [u]
    # creating adjacency list
    # v is the vertex and u is the adjacent vertices that determines the degree
    try:
        for v in graph[u]:
            if not visited_edge[u][v]:  # checks if the vertices u, v are not visited
                visited_edge[u][v], visited_edge[v][u] = True, True  # follows that the vertices are unvisited;

                path = dfs(v, graph, visited_edge, path)
        return path
    # Handle error
    except KeyError as e:
        print("Kindly run the code again", e)
        sys.exit()


# checking if graph has euler path or circuit
def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        # checking if the nodes have even degrees
        if len(graph[i]) % 2 == 1:
            # count the number of odd nodes
            odd_degree_nodes += 1
            odd_node = i
    print(f"Number of odd nodes:{odd_degree_nodes}")
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node


# Function to check if a graph is Eulerian
def check_euler(graph, max_node):
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("Graph is not Eulerian")
        print("No path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("Graph is not Eulerian")
    if check == 1:
        print("Graph has a Euler cycle")
    # Get path of graph
    path = dfs(start_node, graph, visited_edge)
    print(path)


# Function to check if node has been visited
def check_node_visited(graph, start):
    vertexList, edgeList = graph
    # Empty lists
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex


# Main program
def main():
    # Number of vertices in the graph
    max_node = 10
    # Probability a node will have an edge
    probability = random.random()
    # Random graph generated
    graph = erdos_renyi_graph(max_node, probability)
    # Get the edges of the graph
    edges = graph.edges
    print("These are the graph edges")
    print(edges)
    # Get the nodes of the graph
    nodes = graph.nodes
    print("These are the graph nodes")
    print(nodes)
    vertexList = nodes
    edgeList = edges
    project_graph = (vertexList, edgeList)
    # Create list of neighbours of each node
    print("\nList of neighbours of each node")
    G = {
        1: list(networkx.Graph.neighbors(graph, 0)),
        2: list(networkx.Graph.neighbors(graph, 1)),
        3: list(networkx.Graph.neighbors(graph, 2)),
        4: list(networkx.Graph.neighbors(graph, 3)),
        5: list(networkx.Graph.neighbors(graph, 4)),
        6: list(networkx.Graph.neighbors(graph, 5)),
        7: list(networkx.Graph.neighbors(graph, 6)),
        8: list(networkx.Graph.neighbors(graph, 7)),
        9: list(networkx.Graph.neighbors(graph, 8)),
        10: list(networkx.Graph.neighbors(graph, 9))
    }
    print(G)
    # Plot the graph
    networkx.draw(graph, label=True)
    plt.show()
    # Call function to check if node has been visited
    check_connection = check_node_visited(project_graph, 0)
    # Check if the number of visited nodes
    if len(check_connection) == max_node:
        print("The graphs visited:", check_connection)
        print("All nodes have been visited")
        print("Graph is connected")
        check_euler(G, max_node)
    if len(check_connection) != max_node:
        print("The nodes visited:", check_connection)
        print("Only", len(check_connection), "nodes have been visited. Therefore, the Graph is not connected")


# Call main program
main()
