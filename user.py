class User():
    def __init__(self, username, password, age) -> None:
        self.username = username
        self.password = password
        self.age = age
        self.logged_in = False
    def __str__(self):
        return f"username: {self.username}, password: {self.password}, age: {self.age}, logged_in: {self.logged_in}"
    def __repr__(self):
        return f"username: {self.username}, password: {self.password}, age: {self.age}, logged_in: {self.logged_in}"
    def login(self, passed_password):
        if passed_password == self.password:
            self.logged_in = True
        else:
            raise ValueError("Given password does not match")
    def logout(self):
        self.logged_in = False
        