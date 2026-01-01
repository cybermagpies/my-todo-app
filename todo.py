import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_header():
    # Mimicking the soft aesthetic of the Dribbble design
    console.print(Panel("[bold magenta]✨ CYBERMAGPIES PRODUCTIVITY ✨[/bold magenta]", 
                  subtitle="Modern To-Do CLI", 
                  border_style="bright_blue"))

def show_tasks(tasks):
    if not tasks:
        console.print("[italic yellow]Your list is empty. Start by adding a task![/italic yellow]")
        return

    table = Table(show_header=True, header_style="bold cyan", border_style="bright_blue")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Task Description", min_width=20)
    table.add_column("Status", justify="right")

    for i, task in enumerate(tasks, 1):
        # Design touch: Use icons like the Dribbble design
        status = "[green]● Done[/green]" if task.get("done") else "[red]○ Pending[/red]"
        table.add_row(str(i), task["text"], status)
    
    console.print(table)

def main():
    tasks = load_tasks()
    
    while True:
        os.system('clear') # Keep the terminal clean
        display_header()
        show_tasks(tasks)
        
        console.print("\n[bold cyan]1.[/bold cyan] Add  [bold cyan]2.[/bold cyan] Complete  [bold cyan]3.[/bold cyan] Delete  [bold cyan]4.[/bold cyan] Exit")
        choice = Prompt.ask("Action", choices=["1", "2", "3", "4"])

        if choice == '1':
            text = Prompt.ask("What needs to be done?")
            tasks.append({"text": text, "done": False})
            save_tasks(tasks)
        
        elif choice == '2':
            num = int(Prompt.ask("Enter Task ID to complete"))
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
                save_tasks(tasks)
        
        elif choice == '3':
            num = int(Prompt.ask("Enter Task ID to delete"))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
        
        elif choice == '4':
            console.print("[bold green]Goodbye, Cybermagpie![/bold green]")
            break

if __name__ == "__main__":
    main()
