# EJERCICIOS PRÁCTICOS - LISTAS ENLAZADAS
# Nombre: Intriago Rade Joan Samir
#Fecha: 20/12/2025
#Ejercicios Resueltos: 19

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        """Añade un elemento al final de la lista"""
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def a_lista_python(self):
        """Método auxiliar para ver la lista como un arreglo normal"""
        res = []
        actual = self.cabeza
        while actual:
            res.append(actual.dato)
            actual = actual.siguiente
        return res

    # --- EJERCICIOS BÁSICOS ---

    # Ejercicio 1: Contar elementos
    def contar(self, elemento):
        veces = 0
        actual = self.cabeza
        while actual:
            if actual.dato == elemento:
                veces += 1
            actual = actual.siguiente
        return veces

    # Ejercicio 2: Obtener elemento por índice
    def obtener(self, indice):
        actual = self.cabeza
        pos = 0
        while actual:
            if pos == indice:
                return actual.dato
            actual = actual.siguiente
            pos += 1
        raise IndexError("Indice fuera de rango")

    # Ejercicio 3: Encontrar índice de elemento
    def indice_de(self, elemento):
        actual = self.cabeza
        pos = 0
        while actual:
            if actual.dato == elemento:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1

    # --- EJERCICIOS INTERMEDIOS ---

    # Ejercicio 6: Invertir lista
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    # Ejercicio 9: Eliminar duplicados
    def eliminar_duplicados(self):
        if not self.cabeza: return
        vistos = {self.cabeza.dato}
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato in vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                vistos.add(actual.siguiente.dato)
                actual = actual.siguiente

    # --- EJERCICIOS AVANZADOS ---

    # Ejercicio 12: Rotar lista
    def rotar(self, n):
        if not self.cabeza or n == 0: return
        actual = self.cabeza
        largo = 1
        while actual.siguiente:
            actual = actual.siguiente
            largo += 1
        n = n % largo
        if n == 0: return
        actual.siguiente = self.cabeza
        pasos = largo - n
        nuevo_final = self.cabeza
        for _ in range(pasos - 1):
            nuevo_final = nuevo_final.siguiente
        self.cabeza = nuevo_final.siguiente
        nuevo_final.siguiente = None

# --- EJERCICIO 16: Navegador Web (Clase aparte por ser Lista Doble) ---
class HistorialNavegador:
    def __init__(self, inicio):
        self.actual = Nodo(inicio)

    def visitar(self, url):
        nueva = Nodo(url)
        nueva.anterior = self.actual
        self.actual.siguiente = nueva
        self.actual = nueva

    def atras(self, pasos):
        while pasos > 0 and self.actual.anterior:
            self.actual = self.actual.anterior
            pasos -= 1
        return self.actual.dato
#Ejercicio 17: LRU Cache
class CacheLRU:
    def __init__(self, capacidad):
        self.cap = capacidad
        self.cache = {}
        self.orden = []
    def obtener(self, llave):
        if llave in self.cache:
            self.orden.remove(llave)
            self.orden.append(llave)
            return self.cache[llave]
        return -1
    def poner(self, k, v):
        if k in self.cache: self.orden.remove(k)
        elif len(self.cache) >= self.cap:
            del self.cache[self.orden.pop(0)]
        self.cache[k] = v
        self.orden.append(k)

#EJERCICIO 18: Editor Multi-cursor:
class EditorMultiCursor:
    def __init__(self):
        self.cursores = {} # ID: posicion
    def agregar_cursor(self, id_cursor, pos):
        self.cursores[id_cursor] = pos
    def escribir_en_cursor(self, id_cursor, texto):
        pos = self.cursores.get(id_cursor, 0)
        print(f"Escribiendo '{texto}' en posicion {pos}")

# ============================================================================
# EJERCICIOS DE ANÁLISIS Y OPTIMIZACIÓN
# ============================================================================

#EJERCICIO 19: Benchmark de operaciones:
import time
def realizar_benchmark():
    n = 5000
    inicio = time.time()
    lista_py = []
    for i in range(n): lista_py.insert(0, i)
    fin_py = time.time() - inicio
    
    inicio = time.time()
    mi_lista = ListaEnlazada()
    for i in range(n):
        nuevo = Nodo(i)
        nuevo.siguiente = mi_lista.cabeza
        mi_lista.cabeza = nuevo
    fin_mia = time.time() - inicio
    
    print(f"Benchmark (Insertar {n} al inicio):")
    print(f"Lista Python: {fin_py:.5f}s | Mi Lista: {fin_mia:.5f}s")

# SECCIÓN DE PRUEBAS
def ejecutar_pruebas():

    # PRUEBA EJERCICIOS 1, 2 y 3: Búsqueda y Conteo
    print("\n[PRUEBA EJERCICIOS 1, 2 y 3]")
    l_basica = ListaEnlazada()
    for x in [10, 20, 10, 30]: l_basica.agregar(x)
    print(f"1. Contar el número 10: {l_basica.contar(10)} (Esperado: 2)")
    print(f"2. Obtener dato en índice 3: {l_basica.obtener(3)} (Esperado: 30)")
    print(f"3. Buscar índice del 50: {l_basica.indice_de(50)} (Esperado: -1)")

    # PRUEBA EJERCICIO 6: Invertir
    print("\n[PRUEBA EJERCICIO 6]")
    l_basica.invertir()
    print(f"1. Lista invertida: {l_basica.a_lista_python()} (Esperado: [30, 10, 20, 10])")

    # PRUEBA EJERCICIO 9: Duplicados
    print("\n[PRUEBA EJERCICIO 9]")
    l_basica.eliminar_duplicados()
    print(f"1. Sin duplicados: {l_basica.a_lista_python()} (Esperado: [30, 10, 20])")

    # PRUEBA EJERCICIO 12: Rotar
    print("\n[PRUEBA EJERCICIO 12]")
    l_rot = ListaEnlazada()
    for x in [1, 2, 3, 4, 5]: l_rot.agregar(x)
    l_rot.rotar(2)
    print(f"1. Rotar 2 posiciones [1,2,3,4,5]: {l_rot.a_lista_python()} (Esperado: [4, 5, 1, 2, 3])")

    # PRUEBA EJERCICIO 16: Historial
    print("\n[PRUEBA EJERCICIO 16]")
    nav = HistorialNavegador("uleam.edu.ec")
    nav.visitar("google.com")
    nav.visitar("youtube.com")
    print(f"1. Atrás 1 paso: {nav.atras(1)} (Esperado: google.com)")
    print(f"2. Atrás 10 pasos (límite): {nav.atras(10)} (Esperado: uleam.edu.ec)")

if __name__ == "__main__":
    ejecutar_pruebas()