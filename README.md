# ARBOL

https://github.com/enqilin/Arbol.git



Ya conocemos las bases fundamentales de árboles para pasar al diseño del TDA árbol binario de búsqueda, a diferencia de los anteriores solo necesitaremos una variable puntero –que será la raíz del árbol– que apuntará a un nodoArbol. Este último está compuesto de tres elementos, informa- ción, hijo izquierdo e hijo derecho, además de las funciones que detallan su manera de operar, las cuales se enumeran a continuación:

0. el nodo del arbol

```bash
class NodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
```
Crea la clase de Arbol Binarios
```bash
class ArbolBinario(obejct):
```
1.	insertar_nodo(raíz, elemento). Agrega el elemento al árbol;

```bash
    def insertar_nodo(raiz, nodo):
        if raiz is None:
            raiz= NodoArbol(nodo)
        
        elif nodo<raiz.info:
            raiz.izq=ArbolBinario.insertar_nodo(raiz.izq, nodo)
        else:
            raiz.der= ArbolBinario.insertar_nodo(raiz.der, nodo)
        return raiz
```

2.	eliminar_nodo(raíz, clave). Elimina y devuelve del árbol si encuentra un elemento que coincida con la clave dada –el primero que encuentre–, si devuelve None significa que no se encontró la clave en el árbol, y por ende no se elimina ningún elemento;


```bash
def eliminar_nodo(raiz, clave):
        x= None
        if raiz is not None:
            if clave<raiz.info:
                raiz.izq, x= ArbolBinario.eliminar_nodo(raiz.izq, clave)
            elif clave>raiz.info:
                raiz.der, x= ArbolBinario.eliminar_nodo(raiz.der, clave)
            else:
                x= raiz.info
                if raiz.izq is None:
                    raiz= raiz.der
                elif raiz.der is None:
                    raiz= raiz.izq
                else:
                    raiz.izq, aux= ArbolBinario.remplazar(raiz.izq)
                    raiz.info= aux.info
        return raiz, x
```

3.	reemplazar(raíz). Determina el nodo que reemplazará al que se va a eliminar, esta es una fun- ción interna que solo es utilizada por la función eliminar;
 

```bash
    def remplazar(raiz):
        aux= None
        if raiz.der is None:
            aux= raiz
            raiz = raiz.izq
        else:
            raiz, aux= ArbolBinario.remplazar(raiz.der)
        return raiz, aux
    
```

4.	arbol_vacio(raíz). Devuelve verdadero (true) si el árbol no contiene elementos;

```bash
 def arbolvacio(raiz):
        return raiz is None
    
```
5.	buscar(raíz, clave). Devuelve un puntero que apunta al nodo que contiene un elemento que coincida con la clave –el primero que encuentra–, si devuelve None significa que no se encontró la clave en el árbol;

```bash
    def buscar(raiz, clave):
        pos= None
        if raiz is not None:
            if raiz.info==clave:
                pos= raiz
            elif clave<raiz.info:
                pos= ArbolBinario.buscar(raiz.izq, clave)
            else:
                pos= ArbolBinario.buscar(raiz.der, clave)
        return pos
```
6.	preorden(raíz). Realiza un recorrido de orden previo del árbol mostrando la información de los elementos almacenados en el árbol;

```bash
    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            ArbolBinario.preorden(raiz.izq)
            ArbolBinario.preorden(raiz.der)
```
7.	inorden(raíz). Realiza un recorrido en orden del árbol mostrando la información de los ele- mentos almacenados en el árbol;

```bash
    def inorden(raiz):
        if raiz is not None:
            ArbolBinario.inorden(raiz.izq)
            print(raiz.info)
            ArbolBinario.inorden(raiz.der)
```
8.	postorden(raíz). Realiza un recorrido de orden posterior del árbol mostrando la información de los elementos almacenados en el árbol.

```bash
    def postorden(raiz):
        if raiz is not None:
            ArbolBinario.postorden(raiz.der)
            print(raiz.info)
            ArbolBinario.postorden(raiz.izq)
```
9.	por_nivel(raíz). Realiza un recorrido del árbol por nivel mostrando la información de los ele- mentos almacenados.

```bash
    def por_nivel(raiz):
        pendientes = Cola()
        Cola.arribo(pendientes,raiz)
        while not Cola.cola_vacia(pendientes):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if nodo.izq is not None:
                Cola.arribo(pendientes,nodo.izq)
            if nodo.der is not None:
                Cola.arribo(pendientes,nodo.der)

class nodoCola(object):
    def __init__(self):
        self.info , self.sig = None ,None

class Cola(object):
    def __init__(self):
        self.frente , self.final = None , None

    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.final.sig
        if cola.frente is None:
            cola.final = None
        return dato
    def cola_vacia(cola):
        return cola.frente is None
```