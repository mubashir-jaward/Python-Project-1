class User:
    def __init__(self, name, email):
        self.name = name
        if self._is_valid_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email format")
        self.accounts = []

    def _is_valid_email(self, email):
        """A basic email validation using regular expression."""
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance  # Assuming your Account class has a 'balance' attribute
        return total_balance

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account_to_remove):
        if account_to_remove in self.accounts:
            self.accounts.remove(account_to_remove)
            return f"Account {account_to_remove} removed successfully."
        else:
            return f"Account {account_to_remove} not found for user {self.name}."

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_account_count()} account(s), Total Balance: ${self.get_total_balance():.2f}"