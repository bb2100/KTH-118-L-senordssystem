from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Skriv klart passwd-metoden i User
# Kontrollera att användaren i passwords från init_users har blivit ändrad



class User:
    def __init__(self, username:str,password:str) -> None:
        self.username = username
        self.password = password
        self.logged_in = False
    
    def log_in(self):
        self.logged_in = True
    
    def log_out(self):
        self.logged_in = False
    
    def passwd(self):
        # Be om nuvarande lösenord
        # Be om nytt lösenord
        # Be om nytt lösenord igen
        # sätt self.password = nya lösenordet om ovan stämmer
        # LOGGA
        current = input("Skriv in ditt nuvarande lösenord: ")
        if current == self.password:
            new = input("Enter your new passord: ")
            newcheck = input("Enter your new password again: ")
            if new == newcheck:
                self.password = new
                print("Your password was successfully changed!")

                with open("log.txt", "a", encoding="utf-8") as chalog:
                    chalog.write(f"\nA user successfully changed password for {self.username} at {current_time}\n")

                loggedin()

            else:
                print("The passwords does not match")

                with open("log.txt", "a", encoding="utf-8") as chalogr:
                    chalogr.write(f"\nA user tried to change password for {self.username} at {current_time}\n")

                loggedin()

        else:
            print("The current password is incorrect")
            loggedin()
        

def init_users(): #loads all users from file, creates object "user" of them and returns a list of users
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

            with open("log.txt", "a", encoding="utf-8") as loglogr:
                loglogr.write(f"\nA user successfully logged into {usernamelog} at {current_time}\n")

            return current_user
    else:
        print("Username or password was incorrect.")

        with open("log.txt", "a", encoding="utf-8") as loglogw:
            loglogw.write(f"\nA user tried to log in to {usernamelog} at {current_time} but had the wrong password\n")
    return None
    
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

    with open("log.txt", "a", encoding="utf-8") as reglog:
        reglog.write(f"\nA user created the account {username} at {current_time}\n")
    
def loggedin(current_user):
    alternatives = input("Vad vill du göra?\n1: Kolla vilka som försökt logga in\npasswd: Byta lösenord\n3: Logga ut\n För att avsluta skriv något annat\n")
    if (alternatives == "1"):
        pass

    if (alternatives == "passwd"):
        current_user.passwd()

    if (alternatives == "3"):
        pass

    
def main():
    users = init_users()
    choice = input("Vad vill du göra?\n1: Logga in\n2: Registrera dig\nFör att avsluta skriv något annat\n")
    if (choice == "1"):
        current_user = login(users)
        if isinstance(current_user, User):
            print ("Du är nu inloggad!")
            loggedin(current_user)
        else:
            pass
    

    if (choice == "2"):
        register()
    
    for password in users:
        print(password.password)
    else:
        raise SystemExit("Programmet Avslutades")

if __name__ == "__main__":
    main()
