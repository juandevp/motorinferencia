#Libreria que hace manejo de grafos, permite calcular la mejor
import networkx as nx

def grafo_transporte_reglas():
#Se crea un grafo dirigido (es un tipo de grafo en el que las aristas tienen un sentido definido)
    grafo = nx.DiGraph()
    # Se definen las reglas (Nodos y aristas), representando estaciones y un peso en tiempo
    grafo.add_edge("A", "B", weight=10)
    grafo.add_edge("A", "C", weight=15)
    grafo.add_edge("B", "D", weight=12)
    grafo.add_edge("C", "D", weight=10)
    grafo.add_edge("C", "E", weight=5)
    grafo.add_edge("D", "E", weight=8)
    grafo.add_edge("B", "E", weight=20)
    return grafo

def mejor_ruta_moverse(nodoIni, nodoFin):
    try:
        grafo = grafo_transporte_reglas()
        #Se encuentra la mejor ruta entre nodoIni y nodoFin minimizando el peso, que para nosotros es el tiempo
        rutaOptima = nx.shortest_path(grafo, source=nodoIni, target=nodoFin, weight='weight')
        tiempo = nx.shortest_path_length(grafo, source=nodoIni, target=nodoFin, weight='weight')
        return rutaOptima, tiempo
    except nx.NetworkXNoPath:
        return None, float(0)

# Definicion de nodos
nodoIni, nodoFin = "A", "E"
rutas, tiempo = mejor_ruta_moverse(nodoIni, nodoFin)
if rutas:
    print(f"La mejor ruta para moverse de {nodoIni} a {nodoFin}: {' -> '.join(rutas)}, Tiempo: {tiempo} min")
else:
    print("No hay ruta disponible.")