# Given an undirected graph G = (V, E) having N (1<N<=1000) vertices V = {1,
# 2, ..., N} and positive weights between vertices E, find the shortest
# path from vertex 1 to vertex N, or state that such path doesn't exist.

import networkx


def solve(graph):
    paths, path_weights = initialize_solutions(graph)
    for i, (p, w) in enumerate(zip(paths, path_weights)):
        print('Path {}: {} (weight {})'.format(i, p, w))
    print('')

    for i in graph.nodes():
        print('Path to node {}'.format(i))
        for j in graph.neighbors(i):
            weight_ij = graph.edges[i, j]['weight']
            path_weight_j = path_weights[j]

            if path_weight_j + weight_ij < path_weights[i]:
                path_weights[i] = path_weight_j + weight_ij
                paths[i] = [*paths[j], i]

                print('Improvement: {} (weight {})'.format(
                    paths[i], path_weights[i],
                ))

        print('Path from 1 to {}: {} (weight {})'.format(
            i, paths[i], path_weights[i]
        ))
        print('')


def initialize_solutions(graph):
    initial_paths = [None for _ in range(graph.number_of_nodes())]
    initial_weights = [float('inf') for _ in range(graph.number_of_nodes())]

    neighbors = set(graph.neighbors(0))
    for i in graph.nodes():
        if i in neighbors:
            initial_paths[i] = [0, i]
            initial_weights[i] = graph.edges[0, i]['weight']

    return initial_paths, initial_weights


if __name__ == '__main__':
    G = networkx.Graph()
    G.add_nodes_from(range(4))
    G.add_edges_from([
        (0, 2, {'weight': 1}),
        (0, 3, {'weight': 15}),
        (1, 3, {'weight': 2}),
        (2, 3, {'weight': 1}),
    ])
    
    solve(graph=G)

