# Task Tracker CLI

A simple command-line tool to manage tasks, storing them in a JSON file.

## Installation
- Requires Python 3.6+.
- Clone this repository: `git clone <repo-url>`
- Navigate to the project directory: `cd task-tracker-cli`

## Usage
Run commands using: `python task_cli.py <command> [args]`

### Commands
- Add a task: `python task_cli.py add "Task description"`
- Update a task: `python task_cli.py update <id> "New description"`
- Delete a task: `python task_cli.py delete <id>`
- Mark task as in-progress: `python task_cli.py mark-in-progress <id>`
- Mark task as done: `python task_cli.py mark-done <id>`
- List all tasks: `python task_cli.py list`
- List tasks by status: `python task_cli.py list [done|todo|in-progress]`

## Example
```bash
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
python task_cli.py list
# Output: ID: 1, Description: Buy groceries, Status: todo, Created: ..., Updated: ...
