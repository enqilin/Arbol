# ARBOL

https://github.com/enqilin/Arbol.git



Ya conocemos las bases fundamentales de árboles para pasar al diseño del TDA árbol binario de búsqueda, a diferencia de los anteriores solo necesitaremos una variable puntero –que será la raíz del árbol– que apuntará a un nodoArbol. Este último está compuesto de tres elementos, informa- ción, hijo izquierdo e hijo derecho, además de las funciones que detallan su manera de operar, las cuales se enumeran a continuación:

0. el nodo del arbol

```bash

```

1.	insertar_nodo(raíz, elemento). Agrega el elemento al árbol;

```bash

```

2.	eliminar_nodo(raíz, clave). Elimina y devuelve del árbol si encuentra un elemento que coincida con la clave dada –el primero que encuentre–, si devuelve None significa que no se encontró la clave en el árbol, y por ende no se elimina ningún elemento;


```bash

```

3.	reemplazar(raíz). Determina el nodo que reemplazará al que se va a eliminar, esta es una fun- ción interna que solo es utilizada por la función eliminar;
 

```bash

```

4.	arbol_vacio(raíz). Devuelve verdadero (true) si el árbol no contiene elementos;

```bash

```
5.	buscar(raíz, clave). Devuelve un puntero que apunta al nodo que contiene un elemento que coincida con la clave –el primero que encuentra–, si devuelve None significa que no se encontró la clave en el árbol;

```bash

```
6.	preorden(raíz). Realiza un recorrido de orden previo del árbol mostrando la información de los elementos almacenados en el árbol;

```bash

```
7.	inorden(raíz). Realiza un recorrido en orden del árbol mostrando la información de los ele- mentos almacenados en el árbol;

```bash

```
8.	postorden(raíz). Realiza un recorrido de orden posterior del árbol mostrando la información de los elementos almacenados en el árbol.

```bash

```


"""
