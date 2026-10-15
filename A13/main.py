from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import algoritmo

app = FastAPI(title="Algoritmos P y NP Backend", version="1.0.0")

class GraphRequest(BaseModel):
    num_nodes: int
    weighted: Optional[bool] = True

class SearchRequest(BaseModel):
    graph: List[List[float]]
    start_node: int
    end_node: int

class TspRequest(BaseModel):
    graph: List[List[float]]
    start_node: Optional[int] = 0

@app.post("/api/graph/generate")
def generate_graph(req: GraphRequest):
    if req.num_nodes < 2:
        raise HTTPException(status_code=400, detail="El número mínimo de nodos es 2.")
    graph = algoritmo.generate_synthetic_graph(req.num_nodes, req.weighted)
    return {"num_nodes": req.num_nodes, "graph": graph}

@app.post("/api/algorithm/dijkstra")
def dijkstra_endpoint(req: SearchRequest):
    result = algoritmo.run_dijkstra(req.graph, req.start_node, req.end_node)
    return {"algorithm": "Dijkstra (P)", "result": result}

@app.post("/api/algorithm/tsp-greedy")
def tsp_greedy_endpoint(req: TspRequest):
    result = algoritmo.run_tsp_greedy(req.graph, req.start_node)
    return {"algorithm": "TSP Heurística Voraz (P - Aproximación)", "result": result}

@app.post("/api/algorithm/tsp-exact")
def tsp_exact_endpoint(req: TspRequest):
    if len(req.graph) > 15:
        raise HTTPException(status_code=400, detail="El tamaño máximo para el TSP exacto en este servidor es de 15 nodos.")
    result = algoritmo.run_tsp_exact(req.graph)
    return {"algorithm": "TSP Exacto - Programación Dinámica (NP)", "result": result}