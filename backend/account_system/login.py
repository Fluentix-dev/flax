class Account:
    def __init__(self, first_name: str, last_name: str, password: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
    
    def __repr__(self) -> str:
        return f"<Account><name>{self.first_name} {self.last_name}</></>"