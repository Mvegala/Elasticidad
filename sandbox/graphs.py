import networkx as net
import matplotlib.pyplot as plt

# ----------------------------------------------------


relaciones = [['e', 'h'], ['h', 's'], ['h', 'g'], ['h', 'hx'], ['s', 'g'], ['s', 'v'], ['s', 's'],
                           ['s', 'sx'], ['v', 'g'], ['v', 'vx'], ['g', 'b'], ['g', 'c'], ['g', 'gx'], ['b', 'bx'],
                           ['c', 'cx']]
numVertices = 0

g = net.Graph()

# Se crean los nodos con sus relaciones

for i in range(len(relaciones)):
    g.add_edge((relaciones[i][0]), (relaciones[i][1]))
    print(g.edges())

    # g.add_edge('e', 'h')

    # g.add_edge('h', 's')

    # g.add_edge('h', 'g')

    # g.add_edge('s', 'g')

    # g.add_edge('s', 'v')

    # g.add_edge('s', 's')

    # g.add_edge('v', 'g')

    # g.add_edge('g', 'b')

    # g.add_edge('g', 'c')

print("Nodos: ", g.nodes())

print("Relaciones: ", g.edges())

# Se define un tamagno al nodo a y un peso a la relacion entre el nodo e y h

g.node['e']['size'] = 25

g['e']['h']['weight'] = 1

print("Vecinos de h: ", g.neighbors('h'))

print("Valor del nodo h: ", g['h'])

print("Peso de la relacion entre e y h: ", g['e']['h'])

# Se dibuja el grafo

net.draw(g, node_size=500, node_color='r')
g.node['e']['size'] = 25
# Se muestra el grafico

plt.show()

# Ecuaciones

Ve = 1
Vh = 1

vecinosS = g.neighbors('s')
print(vecinosS)


for n in range(len(vecinosS)):
    print(vecinosS[n])

# Vs = Vh *