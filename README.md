![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Sorted_binary_tree.svg/350px-Sorted_binary_tree.svg.png)

# Arboles-PostOrden

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
