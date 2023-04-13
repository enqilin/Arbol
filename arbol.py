class nodoArbol(object):
    def __init__(self,info):
        self.info = info
        self.izq = None
        self.der = None
class ArbolBinario(object):
    def insertar_nodo(raiz, dato):
        """Insertar un dato añ árbol"""
        if raiz is None:
            raiz = nodoArbol(dato)
        elif(dato < raiz.info):
            raiz.izq = ArbolBinario.insertar_nodo( raiz.izq , dato)
        else:
            raiz.der = ArbolBinario.insertar_nodo(raiz.der, dato)
        return raiz

    def arbolvacio(raiz):
        """Devuleve true si el árbol esta vacio"""
        return raiz is None
    
    def remplazar(raiz):
        aux=None
        if(raiz.der is None):
            aux = raiz
            raiz= raiz.izq
        else:
            raiz.der,aux = ArbolBinario.remplazar(raiz.der)
        return raiz , aux
    
    def eliminar_nodo(raiz,clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
        aux = None
        if(raiz is not None):
            if(clave < raiz.info):
                raiz.izq, aux= ArbolBinario.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der,aux = ArbolBinario.eliminar_nodo(raiz.der , clave)
            else:
                aux = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz =raiz.izq
                else:
                    raiz.izq, aux= ArbolBinario.remplazar(raiz.izq)
                    raiz.info=aux.info
            return raiz,aux

    def buscar(raiz,clave):
        """Devuleve la direccion del elemento buscado"""
        pos = None
        if(raiz is not None):
            if(raiz.info ==clave):
                pos = raiz
            elif clave < raiz.info:
                pos = ArbolBinario.buscar(raiz.izq , clave)
            else:
                pos = ArbolBinario.buscar(raiz.der , clave)
        return pos

    def inorden(raiz):
        """Realiza el barrido inorden del árbol"""
        if(raiz is not None):
            raiz.inorden(raiz.izq)
            print(raiz.info)
            raiz.inorden(raiz.der)

    def preorden(raiz):
        """Realiza el barrido preorden del árbol"""
        if(raiz is not None):
            print(raiz.info)
            raiz.preorden(raiz.der)
            raiz.preorden(raiz.izq)
    
    def postorden(raiz):
        """Realiza el barrido postorden del árbols"""
        if(raiz is not None):
            raiz.preorden(raiz.der)
            print(raiz.info)
            raiz.preorden(raiz.izq)
