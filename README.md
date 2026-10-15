

# Análisis de Complejidad: Algoritmos Polinómicos (P) y No Determinísticos (NP)

Este documento detalla la implementación en un backend de FastAPI y la evaluación empírica de algoritmos de ruta más corta (**Dijkstra**), el problema del agente viajero mediante heurística voraz (**TSP Voraz**) y su solución exacta con programación dinámica (**TSP Exacto**).

## 1. Comportamiento Teórico

| Algoritmo | Clase | Complejidad Teórica | Descripción |
| :--- | :--- | :--- | :--- |
| **Dijkstra** | P | $O(E \log V)$ | Encuentra el camino mínimo de un nodo a otro usando cola de prioridad. |
| **TSP Voraz** | P (Aprox) | $O(V^2)$ | Heurística voraz que selecciona siempre el vecino más cercano disponible. |
| **TSP Exacto** | NP-Hard | $O(N^2 2^N)$ | Programación dinámica (Held-Karp) para encontrar el ciclo óptimo absoluto. |

---

## 2. Resultados Empíricos de Pruebas

### Pruebas con 5 Nodos
- **Dijkstra:** Tiempo: `0.0781 ms` | Memoria: `0.65 KB` | Costo: `49.0`
- **TSP Voraz:** Tiempo: `0.0360 ms` | Memoria: `1.0 KB` | Costo: `142.0`
- **TSP Exacto:** Tiempo: `0.2712 ms` | Memoria: `3.94 KB` | Costo: `142.0` *(Óptimo)*

### Pruebas con 10 Nodos
- **Dijkstra:** Tiempo: `0.1192 ms` | Memoria: `2.5 KB` | Costo: `14.0`
- **TSP Voraz:** Tiempo: `0.0517 ms` | Memoria: `1.13 KB` | Costo: `235.0`
- **TSP Exacto:** Tiempo: `52.3436 ms` | Memoria: `695.66 KB` | Costo: `180.0`

### Pruebas con 15 Nodos
- **Dijkstra:** Tiempo: `0.2449 ms` | Memoria: `3.62 KB` | Costo: `27.0`
- **TSP Voraz:** Tiempo: `0.0643 ms` | Memoria: `1.13 KB` | Costo: `296.0`
- **TSP Exacto:** Tiempo: `3933.11 ms` | Memoria: `39,464.65 KB` | Costo: `217.0`

---

## 3. Conclusiones
Los resultados reflejan fielmente las cotas asintóticas de la teoría de complejidad. Mientras los algoritmos de clase $P$ procesan grafos de 15 nodos en microsegundos, el algoritmo exacto del TSP evidencia la barrera exponencial de la clase $NP$, incrementando drásticamente el uso de memoria y tiempo de cómputo al aumentar el tamaño del espacio de estados.
