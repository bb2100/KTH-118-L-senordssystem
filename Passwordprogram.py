
class User:
    def __init__(self, username:str,password:str) -> None:
        self.username = username
        self.password = password
        self.logged_in = False
    
    def log_in(self):
        self.logged_in = True
    
    def log_out(self):
        self.logged_in = False

def init_users():
    # Läser in alla användare från fil,
    # skapar User-objekt av dem,
    # returnerar lista med Users
    passwords = []
    with open("users.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            user = line.split("/")
            passwords.append(User(user[0], user[1]))
    
    return passwords

def login(users):
    usernamelog = input("Skriv in ditt användarnamn:")
    passwordlog = input("Skriv in ditt lösenord:")
    current_user = ""
    for user in users:
        if user.username == usernamelog and user.password == passwordlog:
            current_user = user
            current_user.log_in()
            break
    else:
        print("Username or password was incorrect.")
    
    # TODO:
    # - lägg till log för login

    # vad returnas av login?

def register():
    username = input("Enter your new username: ")

    password = input("Enter your new password: ")


def main():
    users = init_users()
    choice = input("För att logga in: skriv 1\nFör att registrera dig: skriv 2")
    if (choice == "1"):
        login(users)


