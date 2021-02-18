from igraph import *
import numpy as np
import itertools

class GraphMaking:


    def __init__(self):
        self.graph = None
        self.order = 0
        self.infinities = []

    def create_graph(self):
        self.graph = Graph()
        input_file = open('input.txt', 'r')
        self.vertices_list = []  # List that contains all the vertices of the graph
        adjacency_list = input_file.readlines()  # holds the read file's list.
        for row in adjacency_list:  # Iterate for each row in the read list
            row = row.rstrip('\n')  # Removes the break line character
            try:
                v1, v2 = row.split(',')  # Temporary vavriables to get each node of the input line
                if v1 not in self.vertices_list:  # Verifies if the node is not on the vertices_list
                    self.graph.add_vertex(v1)  # Adds the new vertex to the graph
                    self.vertices_list.append(v1)  # Adds the new vertex to the vertices_list
                if v2 not in self.vertices_list:
                    self.graph.add_vertex(v2)  # Adds the new vertex to the graph
                    self.vertices_list.append(v2)  # Adds the new vertex to the vertices_list
                self.graph.add_edge(v1, v2)  # Creates a connection between the pair o vertices
            except:  # if there there's only one vertice in the input line
                v1 = row[0:]  # v1 will be that value
                if v1 not in self.vertices_list:  # Verify if the vertex is not on the vertices_list
                    self.graph.add_vertex(v1)  # Adds the new vertex to the graph
                    self.vertices_list.append(v1)  # Adds the new vertex to the vertices_list

        input_file.close()
        self.graph.vs['label'] = self.vertices_list  # labels the vertices according to the vertices_list
        self.order = self.graph.vcount()

    def isolation(self):
        for i in range(0,self.order):
            self.accumulates_infinities = 0
            graph_copy = self.graph.copy()
            del_list = []  # lista que conterá os ids das arestas do vértice 'i' que serão removidas. #will contain the edge's ids (the ones that will be removed)
            for target_vertex_id in range(0, self.order):
                try:
                    del_list.append(graph_copy.get_eid(i,target_vertex_id))  #Gets the id of the edge that belongs to the pair of vertices(i,target_vertex_id) and puts it in 'del_list'
                except:
                    pass  # in case the id does not exist
            graph_copy.delete_edges(del_list)   #deletes all edges connected to the node i

            self.shortest_paths = graph_copy.shortest_paths_dijkstra() #List of the graph's shortest paths
            self.infinities.append(list(itertools.chain(*self.shortest_paths)).count(float('inf')))  #counts the number of infinite lenght paths in the graph

    def create_results(self):
        output_local = open('output_local.txt', 'a')
        output_local.write('vertice' + ':' + 'isolation_index \n')
        for i in range(0, grp.order):
            output_local.write(str(self.vertices_list[i]) + ':' + str(self.infinities[i]) + '\n')


grp = GraphMaking()
grp.create_graph()
grp.isolation()
grp.create_results()
