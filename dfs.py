def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # Add neighbouring nodes to the stack
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in stack:
                    stack.append(neighbour)

    return visited


# --- User input section ---
print("--- Build your Graph ---")

student_graph = {}

# Get the total number of connections
num_edges = int(input("How many edges (connections) does your graph have? "))

print("Enter each edge separated by a space:")

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    # Initialize lists if the nodes don't exist
    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    # Add connections (Undirected Graph)
    student_graph[u].append(v)
    student_graph[v].append(u)


# Get the starting point
start = input("Enter the starting node for the DFS: ")

print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting DFS traversal...")

result = dfs(student_graph, start)

print("DFS Traversal:", result)