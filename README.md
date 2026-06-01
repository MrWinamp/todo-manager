# todo-manager

Simple REST API for managing TODO tasks built with FastAPI.

## Stack

- **Python** >= 3.10
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **Hatch** — build & environment management

## Quick start
Create venv and run.

```sh
pip install -e .
todo-manager
```

Server starts at `http://127.0.0.1:8000` with hot-reload enabled.

## API

All endpoints are prefixed with `/api/v1`.

| Method | Path               | Description      |
|--------|--------------------|------------------|
| GET    | `/api/v1`          | Health check     |
| GET    | `/api/v1/tasks`    | List all tasks   |
| POST   | `/api/v1/tasks`    | Create a task    |
| DELETE | `/api/v1/tasks?id=N` | Delete a task  |
| PATCH  | `/api/v1/tasks`    | Update a task    |

### Task model

```json
{
  "id": 1,
  "name": "buy milk",
  "description": "",
  "status": "process"
}
```

- `status` — `"process"` (default) or `"done"`
- `description` — optional, defaults to `""`

### Example

```sh
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"name": "buy milk", "description": "go to the store"}'
```

## Development

```sh
# Run from source
python src/todo_manager/main.py

# Type checking
hatch run types:check
```

## Status

Early-stage project. Data is stored **in memory** (lost on restart). No tests yet.
