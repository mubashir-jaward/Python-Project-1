from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from bank_operator import bank_operator

console = Console()


def menu():
    while True:
        console.clear()

        table = Table(title="🏦 Bank System Menu", title_style="bold magenta")

        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        console.print(table)

        choice = Prompt.ask("👉 Choose option", choices=[str(i) for i in range(1, 8)], default="7")

        if choice == '1':
            bank_operator.create_user()
        elif choice == '2':
            bank_operator.list_users()
        elif choice == '3':
            bank_operator.create_account()
        elif choice == '4':
            bank_operator.deposit_money()
        elif choice == '5':
            bank_operator.withdraw_money()
        elif choice == '6':
            bank_operator.view_transactions()
        elif choice == '7':
            console.print("\n👋 Exiting... Thank you for using the Bank System!", style="bold green")
            break


if __name__ == "__main__":
    menu()
def is_valid_email(self, email):
        """A basic email validation using regular expression."""
        # This regex is a simplified version. For more robust validation,
        # you might consider more complex patterns or using a dedicated library.
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None
        class BankOperator:
    # ... (rest of your __init__, is_valid_email, create_user, list_users, get_user_by_index functions remain the same) ...

    def create_account(self):
        users = self.list_users()
        if users:
            user = self.get_user_by_index(users)
            if user:
                console.print(f"[green]Creating account for user: {user['name']} ({user['email']})[/green]")
                # ... your create_account logic ...
            else:
                console.print("[red]Invalid user selection.\n[/red]")
        else:
            console.print("[yellow]Please create a user first.[/yellow]")

    def deposit_money(self):
        users = self.list_users()
        if users:
            user = self.get_user_by_index(users)
            if user:
                console.print(f"[green]Depositing money for user: {user['name']} ({user['email']})[/green]")
                # ... your deposit logic ...
            else:
                console.print("[red]Invalid user selection.\n[/red]")
        else:
            console.print("[yellow]No users to deposit to.[/yellow]")

    def withdraw_money(self):
        users = self.list_users()
        if users:
            user = self.get_user_by_index(users)
            if user:
                console.print(f"[green]Withdrawing money for user: {user['name']} ({user['email']})[/green]")
                # ... your withdrawal logic ...
            else:
                console.print("[red]Invalid user selection.\n[/red]")
        else:
            console.print("[yellow]No users to withdraw from.[/yellow]")

    def view_transactions(self):
        users = self.list_users()
        if users:
            user = self.get_user_by_index(users)
            if user:
                console.print(f"[green]Viewing transactions for user: {user['name']} ({user['email']})[/green]")
                # ... your view transactions logic ...
            else:
                console.print("[red]Invalid user selection.\n[/red]")
        else:
            console.print("[yellow]No users to view transactions for.[/yellow]")

bank_operator = BankOperator()