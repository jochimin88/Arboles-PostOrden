![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Sorted_binary_tree.svg/350px-Sorted_binary_tree.svg.png)

# Arboles - PostOrden

En ciencias de la computación, el recorrido de árboles se refiere al proceso de visitar de una manera sistemática, 
exactamente una vez, cada nodo en una estructura de datos de árbol (examinando y/o actualizando los datos en los nodos).
Tales recorridos están clasificados por el orden en el cual son visitados los nodos.

Los siguientes algoritmos son descritos para un árbol binario, pero también pueden ser generalizados a otros árboles.

Comparado a las estructuras de datos lineales como las listas enlazadas y arreglos unidimensionales, 
que tienen un método canónico de recorrido, las estructuras arborescentes pueden ser recorridas de muchas 
maneras diferentes. Comenzando en la raíz de un árbol binario, hay tres pasos principales que pueden ser 
realizados y el orden en la cual son realizados define el tipo de recorrido. 

Estos pasos (en ningún orden particular) son: ejecución de una acción en el nodo actual 
(referido como “visitando” el nodo), recorriendo al nodo hijo de la izquierda, 
y recorriendo al nodo hijo de la derecha.
Así el proceso más fácilmente descrito a través de la recursión.


Postorden: (izquierdo, derecho, raíz). Para recorrer un árbol binario no vacío en postorden, 
hay que realizar las siguientes operaciones recursivamente en cada nodo:

1. Atraviese el sub-árbol izquierdo
2. Atraviese el sub-árbol derecho
3. Visite la raíz


## Pseudo-Codigo
```
postorden(nodo)
  si nodo == nulo entonces retorna
  postorden(nodo.izquierda)
  postorden(nodo.derecha)
  imprime nodo.valor
 
  ```

# Base de Datos basadas en Grafos u Orientadas a Grafos

### Neo4j
### Dgraph
### OrientDB
### Amazon Neptune
### FlockDB
### DataStax
### Cassandra
### Titan
### Azure Cosmo DB
### IBM Graph
### Apache Giraph
### HyperGraphDB
### Oracle Spatial and Graph
### Redis
### AnzoGraph
### GraphDB
### FaunaDB
### GraphBase


# Importancia de los Grafos en el campo de la Informatica.

Los grafos son una estructura de datos que sirve para modelar una infinidad de problemas que se pueden expresar de manera computacional. A diferencia de la estructura de árbol, los grafos no son una estructura rígida(sino mucho más flexible), por lo cual permite utilizarlos en aplicaciones de este tipo:


* Mapas, está claro que las rutas de un mapa puede ser modelado por grafos, para encontrar la ruta más corta o con menos congestión.
    Computación distribuida(computadoras conectadas a una red), bueno internet es el mayor sistema distribuido del mundo, cada uno de nuestros computadores podría ser un nodo dentro de un enorme grafo. Por lo cual cuando estas usando internet indirectamente esta todo trabajando sobre grafos.
    
* Redes sociales Por ejemplo facebook usa grafos para manejar la relaciones de amistad entre personas. Cuando te dice “Personas que quizá conozcas”, es básicamente el resultado de un algoritmo que trabaja sobre grafos, el cual dice que tal persona(nodo externo) está cerca de tu “nodo”, basado en que existe una conexión de unos de tus amigos directos a ese “nodo externo”, por lo cual tiene un mayor “peso” de que lo conozcas.
 
* Movilidad de personas(IoT), cada persona que se mueve en la ciudad(con su teléfono móvil), podría ser un nodo dentro de un grafo, el cual permita detectar grandes afluencias de personas en determinado sector y hora del dia dentro de la ciudad(densidad). Y esto claramente se debe realizar con grafos.
  
  
* Base de datos, para todas las aplicaciones anteriormente mencionadas, se pueden utilizar BD NoSQL, para persistir el grafo en disco. Un ejemplo de estas bd es: Neo4j, the world's leading graph database - Neo4j Graph Database

* Inteligencia artificial, Las famosas redes neuronales, no es una aplicación pero son algoritmos que son modelados a través de grafos, mira, dime si no es hermoso esto:

![](https://qph.fs.quoracdn.net/main-qimg-78a02b07081458cab02f695d18d26c01)


