import networkx as nx
vis = []
v = []

G = nx.DiGraph()

import sys
f = open(sys.argv[1],"r")
list_vertice = []
nv = int(f.readline())
#print (nv)
v = f.readline().replace("\n","").split(" ")
#print (v)
G.add_nodes_from(v)
ne = int(f.readline())
for x in range(ne):
    #https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html#networkx.DiGraph.add_edge
    edge = f.readline().replace("\n","").split(" ")
    G.add_edge(edge[0],edge[1],weight=float(edge[2]))
vi = f.readline().replace("\n","").split(" ")[0]

f.close()





#verifica lista de visinhos
# v é a lista de arestas
# vs é um determinado indice
# retorno é a lista de vértices visinhos
print("visinhos do nó ",v[0],":")
print(list(G.adj[v[0]]))
#peso de todos os arcos dos visinhos de um vértice
for u in list(G.adj[v[0]]):
    print("(",v[0],",",u,"): weight = ",G.get_edge_data(v[0],u)['weight'])


print("Nó inicial: ",vi)
print("Lista de Vértices: ",G.nodes)
while True:
    vf = input("Informe o nó final: ")
    if(vf in G.nodes):
        break
    else:
        print("O vértice informado não está listado...") 
print("Nó final: ",vf)
print("===== Dados do Caminho ========")
print("Origem  : ",vi)
print("Destino : ",vf)
print("calculando caminho mais curto...")

###aqui vai o código
''' Dados de entrada:
	 G, 
	 vi = vertice inicial
	 vf = vertice destino
    Dados da saída:
         Caminho do vértice vi ao vértice vf e a distância total percorrida

'''
#comando abaixo irá desenhar o grafo
pos=nx.spring_layout(G)
options = {
    "font_size": 5,
    "node_size": 80,
    
    "linewidths": 1,
    "with_labels":True, 
    "font_color":"red",
    "arrowsize":10,
}

nx.draw_networkx(G,pos,options)
# specifiy edge labels explicitly
edge_labels=dict([((u,v,),d['weight'])
for u,v,d in G.edges(data=True)])

import matplotlib.pyplot as plt
options = {
    "font_size": 5,
    "font_color": 'red',
    "edge_labels":edge_labels,
    "alpha":0.5,
}

nx.draw_networkx_edge_labels(G,pos,**options)



# show graphs
plt.savefig('demo2.pdf')

#print (G.number_of_nodes())
#print (G.number_of_edges())


               
        
