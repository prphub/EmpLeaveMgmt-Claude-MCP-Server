# 🏗️ Employee Leave Management - MCP Server

A Claude-compatible **MCP Server** for managing employee leave data via natural language.

Built with:

* ✅ MCP (Model Context Protocol)
* ✅ Python + Typer
* ✅ CSV-based persistence (one source of truth)
* ✅ Claude-compatible tool definitions

---

## 📦 Features

| Tool                                    | Description                       |
| --------------------------------------- | --------------------------------- |
| `get_leave_balance(employee_id)`        | Check remaining leave days        |
| `get_leave_history(employee_id)`        | View historical leave dates       |
| `apply_leave(employee_id, leave_dates)` | Apply for one or more leave dates |

| Resource                                | Description                       |
| --------------------------------------- | --------------------------------- |
| `greeting://{name}`                     | Friendly onboarding message       |

---

### 📁 Folder Structure

```
EmpLeaveMgmt-Claude-MCP-Server/
├── data/
│   └── employee_leaves.csv      # Single CSV file for persistence
├── main.py                      # MCP tool definitions
├── .venv/                       # Virtual environment
├── pyproject.toml               # Project metadata (via `uv`)
├── uv.lock                      # Dependency lock file
└── README.md                    # You are here!
```

---

### ⚙️ Pre-requisites

* ✅ Python 3.10+
* ✅ [uv](https://github.com/astral-sh/uv) (`pip install uv`)
* ✅ Claude Desktop App with Developer mode enabled

---

### 🚀 Setup

#### 1. Clone the repo and navigate into it:

```bash
git clone https://github.com/prphub/EmpLeaveMgmt-Claude-MCP-Server.git
cd EmpLeaveMgmt-Claude-MCP-Server
```

#### 2. Create a virtual environment and activate it:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate  # Linux/macOS
```

#### 3. Install dependencies:

```bash
pip install uv mcp typer
uv add "mcp[cli]"
```

---

### 📄 CSV Format

Your `employee_leaves.csv` file should look like this:

```csv
employee_id,balance,history
E001,18,2024-12-25;2025-01-01
E002,20,
E003,15,2025-03-15;2025-03-16
```

* `employee_id`: Unique ID
* `balance`: Integer (leave days remaining)
* `history`: Semicolon-separated list of dates

---

### 🧠 Running with Claude (MCP Install)

Make sure `.venv` is activated, then run:

```bash
uv run mcp install main.py
```

Once tools are installed, Claude can invoke them using natural language, for example:

> 🗣️ "How many leave days does E002 have left?"
> 🗣️ "Apply for leave on 2025-07-01 and 2025-07-02 for E003"
> 🗣️ "Show the leave history of E001"

---

### 🧪 Local Development (Optional)

To test locally with a REST UI:

```bash
uv run mcp dev main.py
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🛠️ Notes

* Leave data is persisted to `employee_leaves.csv`
* Multiple leave dates must be passed as a list of ISO strings (e.g., `["2025-08-01", "2025-08-02"]`)
* The CSV is reloaded each time a tool is called (ensures freshness)
* Claude always sees up-to-date employee state
