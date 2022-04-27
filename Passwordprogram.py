
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
            passwords.append(User(user[0], user[1].rstrip("\n")))
    
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
    
def log():
    pass

    # TODO:
    # - lägg till log för login

    # vad returnas av login?

def register():
    username = input("Enter your new username: ")
    password = input("Enter your new password: ")
    with open("users.txt", "a", encoding="utf-8") as write:
        write.write(f"{username}/{password}\n")
    print ("Account successfully created!")
    


def main():
    users = init_users()
    choice = input("För att logga in: skriv 1\nFör att registrera dig: skriv 2\nFör att avsluta: skriv något annat\nFör att kolla vilka som försökt logga in: skriv 3")
    if (choice == "1"):
        login(users)
        print ("Du är nu inloggad!")
    
    if (choice == "2"):
        register()
    
    if (choice == "3"):
        login(users)


    else:
        raise SystemExit("Programmet Avslutades")

if __name__ == "__main__":
    main()
