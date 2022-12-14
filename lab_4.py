# Edges to adjacent matrix of weighted undirected graph

def edges_to_adjacency_matrix(edges,total_vertices):
    
    matrix = [[0 for a in range(total_vertices)] for b in range(total_vertices)]
    
    for edge in edges:
        v1,v2,w = edge
        matrix[v1-1][v2-1] = w
        matrix[v2-1][v1-1] = w
        
    return matrix
    
    
if __name__ == '__main__':
    
    v = int(input("Enter Number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    
    print("\nStart entering dges (s,d,w): ")
    edges = [list(map(int,input().split(" "))) for i in range(num_edges)]
    
    matrix = edges_to_adjacency_matrix(edges,v)
    
    print("\nAdjacency Matrix is ")
    for row in matrix:
        print(row)
