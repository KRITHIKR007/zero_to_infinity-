import numpy as np
# Initialize graph with adjacency matrix.
graph = np.array([[2, 1, np.inf, 3, 5],
                  [0, np.inf, 4, 5, 3],
                  [1, 2, np.inf, 6, 7],
                  [np.inf, 6, 3, 0, 1],
                  [4, 2, 2, 3, np.inf]]
                  )


# Initialize distance vector with direct link costs.
def initialize_distance_vector(graph):
    n = len(graph)
    distance_vector = np.full((n, n), np.inf)
    for i in range(n):
        distance_vector[i][i] = 0  # Distance to self is 0
        for j in range(n):
            if graph[i][j] != np.inf:
                distance_vector[i][j] = graph[i][j]
    return distance_vector


# Implement route poisoning for a failed link.
def route_poisoning(distance_vector, failed_link_index):
    n = len(distance_vector)
    # Set the distance to the failed link as infinity
    for i in range(n):
        distance_vector[i][failed_link_index] = np.inf
        distance_vector[failed_link_index][i] = np.inf

# Simulate a failed link between router 2 and router 3.
distance_vector = initialize_distance_vector(graph)
print("Initial Distance Vector:\n", distance_vector)

# Simulate link failure for router 2.
route_poisoning(distance_vector, 2)
print("Updated Distance Vector after Route Poisoning:\n", distance_vector)

