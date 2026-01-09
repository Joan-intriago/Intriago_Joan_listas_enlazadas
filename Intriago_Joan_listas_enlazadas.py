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
    #EJERCICIO 4: Lista a array
    def to_list(self):
        return self.a_lista_python()
    
    #EJERCICIO 5: Limpiar lista
    def clear(self):
        self.cabeza = None


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
    
    #EJERCICIO 7: Detectar ciclo
    def tiene_ciclo(self):
        lento = self.cabeza
        rapido = self.cabeza
        while rapido and rapido.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
            if lento == rapido:
                return True
        return False

    #EJERCICIO 8: Encontrar el medio
    def obtener_medio(self):
        lento = self.cabeza
        rapido = self.cabeza
        while rapido and rapido.siguiente:
            lento = lento.siguiente
            rapido = rapido.siguiente.siguiente
        return lento.dato if lento else None


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

    #EJERCICIO 10: Fusionar dos listas ordenadas
    def fusionar(l1, l2):
        nueva = ListaEnlazada()
        p1, p2 = l1.cabeza, l2.cabeza
        while p1 and p2:
            if p1.dato <= p2.dato:
                nueva.agregar(p1.dato); p1 = p1.siguiente
            else:
                nueva.agregar(p2.dato); p2 = p2.siguiente
        while p1: nueva.agregar(p1.dato); p1 = p1.siguiente
        while p2: nueva.agregar(p2.dato); p2 = p2.siguiente
        return nueva


    # --- EJERCICIOS AVANZADOS ---
    #EJERCICIO 11: Palíndromo
    def es_palindromo(self):
        lista = self.a_lista_python()
        return lista == lista[::-1]


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
    
    #EJERCICIO 13: Particionar lista
    def particionar(self, x):
        menores, mayores = ListaEnlazada(), ListaEnlazada()
        actual = self.cabeza
        while actual:
            if actual.dato < x:
                menores.agregar(actual.dato)
            else:
                mayores.agregar(actual.dato)
            actual = actual.siguiente
        if not menores.cabeza:
            self.cabeza = mayores.cabeza
        else:
            fin = menores.cabeza
            while fin.siguiente:
                fin = fin.siguiente
            fin.siguiente = mayores.cabeza
            self.cabeza = menores.cabeza

    #EJERCICIO 14: Suma de dos listas (números)
    def sumar_listas(l1, l2):
        r = ListaEnlazada()
        p1, p2, carry = l1.cabeza, l2.cabeza, 0
        while p1 or p2 or carry:
            s = (p1.dato if p1 else 0) + (p2.dato if p2 else 0) + carry
            r.agregar(s % 10)
            carry = s // 10
            if p1: p1 = p1.siguiente
            if p2: p2 = p2.siguiente
        return r

    #EJERCICIO 15: Intersección de dos listas
    def interseccion(l1, l2):
        vistos = set()
        a = l1.cabeza
        while a:
            vistos.add(a)
            a = a.siguiente
        b = l2.cabeza
        while b:
            if b in vistos:
                return b.dato
            b = b.siguiente
        return None


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


# EJERCICIOS DE ANÁLISIS Y OPTIMIZACIÓN

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

#EJERCICIO 20: Análisis de casos de uso

#1. Sistema de colas de impresión (FIFO estricto)
    #Lista Simple, Al ser un sistema FIFO, solo necesitamos insertar al final y eliminar al inicio,
    #la lista simple hace ambas operaciones en tiempo constante O(1).
#2. Historial de navegación de un navegador
    #Lista Doble, el usuario necesita retroceder y avanzar. 
    #La lista doble permite navegar en ambas direcciones eficientemente gracias a los punteros.
#3. Sistema de undo/redo con límite de 100 acciones
    #Lista Doble, porque requiere movimiento bidireccional.
#4. Base de datos que necesita acceso rápido por ID
    #Array,Si el ID es numérico, el Array ofrece acceso aleatorio O(1). Las listas enlazadas requerirían recorrer nodo por 
    #nodo O(n), lo cual es muy lento para búsquedas frecuen
#5. Playlist de música con navegación adelante/atrás
    # Lista Doble Permite pasar a la siguiente canción o volver a la anterior de forma inmediata.
#6. Sistema de gestión de memoria del OS
    #Lista Doble, Tener punteros al bloque anterior y siguiente permite 
    #realizar las uniones de bloques de una manera mas rápida
#7. Editor de texto que solo permite append al final
    #Lista Simple, si no hay ediciones intermedias ni navegación hacia atrás, 
    #la lista simple funcionara mejor para ir agregando nodos al final.
#8. Implementación de una pila (Stack)
    #Lista Simple, esto debido a quetodas las operaciones ocurren en un solo extremo
#9. Juego que necesita insertar/eliminar enemigos frecuentemente
    #Lista Doble, Los enemigos pueden morir o aparecer en cualquier momento. 
    #Si tenemos la referencia del enemigo, la lista doble permite eliminarlo 
    #en O(1) sin tener que buscar el nodo anterior manualmente.
#10. Sistema de logs que solo escribe al final y lee todo
    #Array, porque los logs suelen leerse de forma secuencial y masiva, 
    #por lo que el array va a aprovechar mejor donde esten localizados.

# SECCIÓN DE PRUEBAS
def ejecutar_pruebas():

    # PRUEBA EJERCICIOS 1, 2 y 3: Búsqueda y Conteo
    print("\n[PRUEBA EJERCICIOS 1, 2 y 3]")
    l_basica = ListaEnlazada()
    for x in [10, 20, 10, 30]: l_basica.agregar(x)
    print(f"1. Contar el número 10: {l_basica.contar(10)} (Esperado: 2)")
    print(f"2. Obtener dato en índice 3: {l_basica.obtener(3)} (Esperado: 30)")
    print(f"3. Buscar índice del 50: {l_basica.indice_de(50)} (Esperado: -1)")

    #PRUEBA EJERCICIO 4
    print("\n[PRUEBA EJERCICIO 4]")
    l = ListaEnlazada()
    for x in [1,2,3]: l.agregar(x)
    print(l.to_list())  # [1,2,3]

    #PRUEBA EJERCICIO 5
    print("\n[PRUEBA EJERCICIO 5]")
    l.clear()
    print(l.a_lista_python())  # []

    # PRUEBA EJERCICIO 6: Invertir
    print("\n[PRUEBA EJERCICIO 6]")
    l_basica.invertir()
    print(f"1. Lista invertida: {l_basica.a_lista_python()} (Esperado: [30, 10, 20, 10])")
 

    # PRUEBA EJERCICIO 7:
    print("\n[PRUEBA EJERCICIO 7]")
    lc = ListaEnlazada()
    for x in [1,2,3]: lc.agregar(x)
    print(lc.tiene_ciclo())  # False
    lc.cabeza.siguiente.siguiente.siguiente = lc.cabeza
    print(lc.tiene_ciclo())  # True

    # PRUEBA EJERCICIO 8
    print("\n[PRUEBA EJERCICIO 8]")
    l = ListaEnlazada()
    for x in [1,2,3,4,5]: l.agregar(x)
    print(l.obtener_medio())  # 3


    # PRUEBA EJERCICIO 9: Duplicados
    print("\n[PRUEBA EJERCICIO 9]")
    l_basica.eliminar_duplicados()
    print(f"1. Sin duplicados: {l_basica.a_lista_python()} (Esperado: [30, 10, 20])")

    # PRUEBA EJERCICIO 11:
    print("\n[PRUEBA EJERCICIO 11]")
    l = ListaEnlazada()
    for x in [1,2,1]: l.agregar(x)
    print(l.es_palindromo())  # True

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

    # PRUEBA EJERCICIO 17: Cache LRU
    print("\n[PRUEBA EJERCICIO 17]")
    cache = CacheLRU(2)
    cache.poner(1, "A")
    cache.poner(2, "B")
    print(f"1. Obtener clave 1: {cache.obtener(1)} (Esperado: A)")
    cache.poner(3, "C")  # Elimina clave 2 (LRU)
    print(f"2. Obtener clave 2: {cache.obtener(2)} (Esperado: -1)")
    print(f"3. Obtener clave 3: {cache.obtener(3)} (Esperado: C)")

    #PRUEBA EJERCICIO 18: Editor Multi-cursor
    print("\n[PRUEBA EJERCICIO 18]")
    editor = EditorMultiCursor()
    editor.agregar_cursor("c1", 0)
    editor.agregar_cursor("c2", 5)
    editor.escribir_en_cursor("c1", "Buenas")
    editor.escribir_en_cursor("c2", "Tardes")

    # PRUEBA EJERCICIO 19: Benchmark
    print("\n[PRUEBA EJERCICIO 19]")
    realizar_benchmark()

if __name__ == "__main__":

    ejecutar_pruebas()
