# 🚀 Visual Pipeline Builder

A full-stack drag-and-drop application for building and validating AI/data processing pipelines with DAG (Directed Acyclic Graph) validation.

**Tech Stack:** React + React Flow + FastAPI + Python

---

## 📋 Overview

Build visual pipelines by dragging nodes (Input, Text, LLM, Output) onto a canvas and connecting them. The backend validates the pipeline structure to ensure it's a valid DAG without circular dependencies.

**Key Capabilities:**
- 🎨 Drag-and-drop node editor with React Flow
- 🔗 Visual connection of nodes with automatic edge tracking
- ✅ Backend DAG validation using cycle detection
- 📊 Real-time feedback on pipeline structure validity
- 🧩 Reusable BaseNode abstraction for clean code

---

## ⚙️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React, React Flow, Zustand, JavaScript (ES6), HTML/CSS |
| **Backend** | Python 3.13+, FastAPI, Pydantic, Uvicorn, NetworkX |
| **Architecture** | REST API, Component-based UI, Graph algorithms |

---

## 📁 Project Structure

```
visual-pipeline-builder/
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── store.js (Zustand)
│   │   ├── ui.js
│   │   ├── toolbar.js
│   │   ├── submit.js
│   │   └── nodes/
│   │       ├── BaseNode.jsx
│   │       ├── inputNode.js
│   │       ├── textNode.js
│   │       ├── llmNode.js
│   │       └── outputNode.js
│   └── package.json
│
└── backend/
    ├── main.py
    └── requirements.txt
```

---

## 🚀 Quick Start

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn pydantic networkx python-multipart
python -m uvicorn main:app --reload
```

**Backend:** http://127.0.0.1:8000

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

**Frontend:** http://localhost:3000

---

## 💡 How to Use

1. **Drag nodes** from the toolbar: Input → Text → LLM → Output
2. **Connect nodes** by clicking handles and dragging connections
3. **Edit text node** with template variables (e.g., `{{input_1}}`)
4. **Click Submit** to validate pipeline
5. **View results:** Node count, edge count, and DAG validity

**Valid Pipeline Flow:**
```
Input → Text → LLM → Output
```

---

## 🧩 Features

### Frontend Features
✅ Drag-and-drop canvas with React Flow  
✅ 4 custom node types with reusable BaseNode abstraction  
✅ Real-time edge connections with handles  
✅ Auto-resizing text inputs  
✅ Zustand state management  
✅ Clean, responsive UI design  

### Backend Features
✅ REST API endpoint: `POST /pipelines/parse`  
✅ Node and edge counting  
✅ DAG validation using DFS cycle detection  
✅ Structured JSON response  
✅ Pydantic input validation  
✅ CORS support  

---

## 📤 API Response

**Request:**
```json
{
  "nodes": [{"id": "1", "type": "input"}, ...],
  "edges": [{"source": "1", "target": "2"}, ...]
}
```

**Response:**
```json
{
  "num_nodes": 4,
  "num_edges": 3,
  "is_dag": true
}
```

---

## 🧠 Architecture

```
Frontend (React + React Flow)
         ↓
    Zustand Store (State)
         ↓
    Canvas UI + Toolbar
         ↓
    POST /pipelines/parse
         ↓
Backend (FastAPI)
    - Parse & validate input
    - Build graph structure
    - Count nodes/edges
    - Check for cycles (DFS)
    - Return validation result
```

---

## 🔍 DAG Validation Logic

Uses **Depth-First Search (DFS)** to detect cycles:
- If a cycle exists → `is_dag: false`
- If no cycles → `is_dag: true` (valid pipeline)

**Time Complexity:** O(V + E) where V = nodes, E = edges

---

## 📦 Download & Run

**Option 1: Clone from GitHub**
```bash
git clone https://github.com/deepakrathod19/visual-pipeline-builder.git
cd visual-pipeline-builder
```

**Option 2: Download ZIP**
📥 [Google Drive - Project ZIP](https://drive.google.com/drive/folders/1G4_sV62wMqs2D01I9IgnzNK0Nr8M4dSY?usp=sharing)

---

## 🎯 Key Learnings

- **Frontend:** Reusable UI abstractions, complex state management with Zustand, React Flow integration
- **Backend:** REST API design, Pydantic validation, graph algorithms (cycle detection)
- **Full-Stack:** API integration, CORS handling, async requests, error handling
- **System Design:** Scalable architecture, algorithm optimization, UI/UX problem solving

---

## 🚀 Future Enhancements

- [ ] Save/load pipelines from database
- [ ] Pipeline execution engine with logging
- [ ] Node configuration panels
- [ ] Undo/redo functionality
- [ ] Conditional branching nodes (if/else)
- [ ] Loop/iteration nodes
- [ ] User authentication and sharing
- [ ] Advanced monitoring and analytics

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend won't start | Check Python 3.13+, run `pip install -r requirements.txt` |
| Frontend blank | Ensure backend is running on http://127.0.0.1:8000 |
| Nodes won't connect | Drag from right handle to left handle, check console |
| CORS error | Verify FastAPI has CORS enabled |
| Port in use | Backend: `--port 8001`, Frontend: `PORT=3001 npm start` |

---

## 👨‍💻 Author

**Deepak Rathod**

- 🔗 GitHub: [@deepakrathod19](https://github.com/deepakrathod19)
- 💼 LinkedIn: [@deeprathod1](https://linkedin.com/in/deeprathod1)
- 📧 Email: rad82377@gmail.com

---

## 📄 License

MIT License - Open source and free to use

---

## ⭐ Project Highlights

✅ Full-stack React + FastAPI integration  
✅ Graph algorithm implementation (DAG validation)  
✅ Complex UI state management  
✅ Production-ready code structure  
✅ Comprehensive documentation  

**Built to demonstrate:** Full-stack engineering, system design thinking, and problem-solving abilities.

---

*Last Updated: January 2026 | Version 1.0.0*
