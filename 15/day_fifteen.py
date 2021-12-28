import math
import numpy as np

def read_input_1(filename):
    file = open(filename)
    matrix = []

    for line in file:
        row = []
        row.append(float('inf'))
        for num in line:
            if num != '\n':
                row.append(int(num))
        row.append(float('inf'))
        matrix.append(row)

    inf_row = len(matrix[0]) * [float('inf')]
    matrix.append(inf_row)
    matrix.insert(0,inf_row)
    return matrix


def read_input_2(filename):
    file = open(filename)
    matrix = []

    for line in file:
        row = []
        for num in line:
            if num!='\n':
                row.append(int(num))
        matrix.append(row) 

    initial_map = np.array(matrix)
    cave_map_p2 = initial_map.copy()
    for row in range(1, 5):
        new_values = (initial_map + row - 1) % 9 + 1
        cave_map_p2 = np.append(cave_map_p2, new_values, axis=0)

    initial_map = cave_map_p2.copy()
    for column in range(1, 5):
        new_values = (initial_map + column - 1) % 9 + 1
        cave_map_p2 = np.append(cave_map_p2, new_values, axis=1)

    matrix = cave_map_p2.tolist()

    for row in matrix:
        row.insert(0,float('inf'))
        row.append(float('inf'))

    row_inf = (len(matrix[0])) * [float('inf')] 
    matrix.insert(0,row_inf)
    matrix.append(row_inf)
            
    return matrix
    

def concat(a, b):
    print(a,b)
    return int(str(a) + str(b))


def create_edges(matrix):
    edges = {}  # (start) -> (end)
    costs = {}  # (start,end) -> (costs)

    for i in range(1,len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            start = (i,j)

            # down
            edges[(i,j)] = [(i+1,j)]
            costs[(start,(i+1,j))] = matrix[i+1][j]

            # right
            edges[(i,j)].append((i,j+1))
            costs[(start,(i,j+1))] = matrix[i][j+1]  

            # left              
            edges[(i,j)].append((i,j-1))
            costs[(start,(i,j-1))] = matrix[i][j-1]   

            # up
            edges[(i,j)].append((i-1,j))
            costs[(start,(i-1,j))] = matrix[i-1][j]  

    return edges, costs
    
class Graph:
    def __init__(self, matrix):
        self.edges, self.costs = create_edges(matrix)      


    def vertices(self):
        vertices = set()

        for v, u in self.edges.items():
            vertices.add(v)
            for end in u:
                vertices.add(end)

        return vertices


    def get_neighbors(self, vertex):
        neighbors = []

        for v in self.edges[vertex]:
            neighbors.append(v)

        return neighbors


    def dijkstra(self, source, destination):
        vertices = list(self.vertices())[:]
        distances = {v: float('inf') for v in vertices}

        distances[source] = 0
        while len(vertices) > 0:
            q = min(vertices, key = lambda u: distances[u])
            vertices.remove(q)
            if distances[q] == float('inf'):
                break
            
            for neighbor in self.get_neighbors(q):
                path_cost = distances[q] + self.costs[q,neighbor]
                distances[neighbor] = min(distances[neighbor], path_cost) 

        print(distances[destination]) 


def main():
    print('advent_of_code: day fifteen')
    print('----------------------------')

    # read input for part 1
    matrix = read_input_1('test_input.txt')

    # solution part 1
    print('part 1:')
    graph = Graph(matrix)
    dest = (len(matrix)-2,len(matrix[0])-2)
    graph.dijkstra((1,1), dest)


    # read input for part 2
    matrix2 = read_input_2('example_input.txt')

    # solution part 2
    #print('part 2:')
    #graph = Graph(matrix2)
    #dest = (len(matrix2)-2,len(matrix2[0])-2)
    #graph.dijkstra((1,1), dest)





if __name__ == '__main__':
    main()