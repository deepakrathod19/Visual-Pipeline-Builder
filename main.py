from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
from collections import defaultdict, deque

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PipelineRequest(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]


def is_dag(nodes, edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for edge in edges:
        src = edge["source"]
        tgt = edge["target"]
        graph[src].append(tgt)
        indegree[tgt] += 1

    queue = deque()
    for node in nodes:
        if indegree[node["id"]] == 0:
            queue.append(node["id"])

    visited = 0
    while queue:
        curr = queue.popleft()
        visited += 1
        for neighbor in graph[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited == len(nodes)


@app.get("/")
def root():
    return {"status": "Backend running"}


@app.post("/pipelines/parse")
def parse_pipeline(data: PipelineRequest):
    return {
        "num_nodes": len(data.nodes),
        "num_edges": len(data.edges),
        "is_dag": is_dag(data.nodes, data.edges),
    }
