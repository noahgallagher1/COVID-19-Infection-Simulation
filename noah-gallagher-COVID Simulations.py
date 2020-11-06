import numpy
import random
import networkx as nx
import matplotlib.pyplot as plt
from random import choice


class Graph1():
    
    def __init__(self,n,A):
        self.n = n #vertices
        self.A = A #interactions

    def getIG(self,n):
        g = nx.Graph()
        #g = nx.line_graph()
        for i in range(self.n):
            g.add_node(i, state = 0, recover = 0) #person
        for l in range(self.A):
            for j in range(self.n):
                i = choice(list(g.nodes())) #random node
                if random.uniform(0,1) < 0.1:
                    g.add_edge(j,i)
                else:
                    k = g.neighbors(i)
                    g.add_edge(j,k)
        self.start(g)
                    
    def start(self,g):
        for node in g.nodes():
            state = nx.get_node_attributes(g,'state')
            #recover = nx.get_node_attributes(g,'recover')
            if state == 1:
                if random.uniform(0,1) < 0.01:
                    #state[node] == 1
                    nx.set_node_attributes(g,'state',1)
                    #recover[node] == 20
                    nx.set_node_attributes(g,'recover',20)
                else:
                    state[node] == 0
        self.sim(90,g)
    
    def sim(self,days,g):
        #g = nx.Graph()
        for v in g.nodes(): #each node in g.nodes
            state = nx.get_node_attributes(g,'state')
            recover = nx.get_node_attributes(g,'recover')
            if state == 1:
                w = g.neighbors(v)
                #wstate = nx.get_node_attributes(g,'state')
                for i in w:
                    if state == 0:
                        if random.uniform(0,1)<0.1:
                            #state[i] == 1
                            nx.set_node_attributes(g,'state',1)
                            #recover[i] == 20
                            nx.set_node_attributes(g,'recover',20)
                #recover[v] -= 1
                nx.set_node_attributes(g,'recover',recover-1)            
                if recover == 0:
                    if random.uniform < 0.06:
                        #state[v] == 2
                        nx.set_node_attributes(g,'state',2)
                    else:
                        #state[v] == 3
                        nx.set_node_attributes(g,'state',3)
        #fig, ax = plt.subplots()
        fig = plt.figure()
        ax = plt.axes()
        nx.draw(g,ax=ax)
        plt.axis('on')
        plt.draw()
        plt.show()
        
#Graph 1: Interactions = 5 , Vertices = 100
n = 100 #people
A = 5 #interactions

g = Graph1(n,A) #defining new graph
g.getIG(n)  #running Graph1()

#Graph 2: Interactions = 100 , Vertices = 10,000
n = 10000 #people
A = 100 #interactions

g = Graph1(n,A) #defining new graph
g.getIG(n) #running Graph1()



