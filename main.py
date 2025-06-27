import csv
from typing import List
from mcp.server.fastmcp import FastMCP
from pathlib import Path



# CSV path constant
CSV_PATH = Path(__file__).parent / "data/employee_leaves.csv"
print("Resolved CSV path:", CSV_PATH.resolve())

# Load employee leave data from CSV
def load_employee_leaves():
    """Load the employee leaves from CSV"""
    employee_data = {}
    if not CSV_PATH.exists():
        print(f"CSV not found: {CSV_PATH}")
        return employee_data

    with CSV_PATH.open(mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            emp_id = row['employee_id'].strip()
            try:
                balance = int(row['balance'].strip())
                history = [h.strip() for h in row['history'].split(';')] if row['history'] else []
                employee_data[emp_id] = {"balance": balance, "history": history}
            except Exception as e:
                print(f"⚠️ Error loading row for {emp_id}: {e}")
    return employee_data

# Save employee leave data to CSV
def save_employee_leaves(data):
    """Save the updated employee leaves to CSV"""
    with CSV_PATH.open(mode='w', newline='') as file:
        fieldnames = ['employee_id', 'balance', 'history']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for emp_id, details in data.items():
            history_str = ';'.join(details['history'])
            writer.writerow({
                'employee_id': emp_id,
                'balance': details['balance'],
                'history': history_str
            })



# Initialize the MCP server
mcp = FastMCP("LeaveManager")



# Tool: Check Leave Balance
@mcp.tool()
def get_leave_balance(employee_id: str) -> str:
    """Check how many leave days are left for the employee"""
    employee_leaves = load_employee_leaves()
    data = employee_leaves.get(employee_id.strip())
    if data:
        return f"{employee_id} has {data['balance']} leave days remaining."
    return "Employee ID not found."

# Tool: Apply for Leave
@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]) -> str:
    """
    Apply leave for specific dates (e.g., ["2025-04-17", "2025-05-01"])
    """
    employee_leaves = load_employee_leaves()
    employee_id = employee_id.strip()

    if employee_id not in employee_leaves:
        return "Employee ID not found."

    requested_days = len(leave_dates)
    available_balance = employee_leaves[employee_id]["balance"]

    if available_balance < requested_days:
        return f"Insufficient leave balance. You requested {requested_days} day(s) but have only {available_balance}."

    # Deduct and update history
    employee_leaves[employee_id]["balance"] -= requested_days
    employee_leaves[employee_id]["history"].extend(leave_dates)
    save_employee_leaves(employee_leaves)

    return f"Leave applied for {requested_days} day(s). Remaining balance: {employee_leaves[employee_id]['balance']}."

# Tool: Get Leave History
@mcp.tool()
def get_leave_history(employee_id: str) -> str:
    """Get leave history for the employee"""
    employee_leaves = load_employee_leaves()
    data = employee_leaves.get(employee_id.strip())
    if data:
        history = ', '.join(data['history']) if data['history'] else "No leaves taken."
        return f"Leave history for {employee_id}: {history}"
    return "Employee ID not found."

# Resource: Greeting
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Personalized greeting"""
    return f"Hello, {name}! How can I assist you with leave management today?"



# Run the MCP server
if __name__ == "__main__":
    mcp.run()
