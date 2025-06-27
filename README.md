### Commands used

pip intsall uv

uv init EmployeeLeave-MCP-Server
cd EmpLeaveMgmt-Claude-MCP-Server

python -m venv .venv
.venv\Scripts\activate

uv add "mcp[cli]"

pip install mcp
pip install --upgrade typer

uv run mcp install main.py


### Setup steps

1. Install Claude Desktop
2. Install uv by running : `pip install uv`
3. Run `uv init EmployeeLeave-MVP-Server` to create a project directory
4. Run `uv add "mcp[cli]"` to add mcp cli in your project
5. Few folks may get type errors for which you can run `pip install --upgrade typer` to upgrade typer library to its latest version
6. Write code in `main.py` for leave management server
7. Install this server inside Claude desktop by running `uv run mcp install main.py` in the project root directory
8. Kill any running instance of Claude from Task Manager. Restart Claude Desktop
9. In Claude desktop, now you will see tools from this server