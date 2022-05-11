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
        current = input("\nEnter your current password: ")
        if current == self.password:
            new = input("Enter your new passord: ")
            newcheck = input("Enter your new password again: ")
            if new == newcheck:
                self.password = new
                print("Your password was successfully changed!")

                with open("log.txt", "a", encoding="utf-8") as chalog:
                    chalog.write(f"\nA user successfully changed password for {self.username} at {current_time}\n")

                #loggedin(self)

            else:
                print("The passwords does not match")

                with open("log.txt", "a", encoding="utf-8") as chalogr:
                    chalogr.write(f"\nA user tried to change password for {self.username} at {current_time}\n")

                

        else:
            print("The current password is incorrect")

            with open("log.txt", "a", encoding="utf-8") as chalogr:
                    chalogr.write(f"\nA user tried to change password for {self.username} at {current_time}\n")
            
    
    def save(self):
        return f"{self.username}/{self.password}\n"
        

def init_users(): #loads all users from file, creates object "user" of them and returns a list of users
    passwords = []
    with open("users.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            user = line.split("/")
            passwords.append(User(user[0], user[1].rstrip("\n")))
    
    return passwords

def login(users):
    usernamelog = input("\nEnter your username: ")
    passwordlog = input("Enter your password: ")
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
    username = input("\nEnter your new username: ")
    password = input("Enter your new password: ")
    with open("users.txt", "a", encoding="utf-8") as write:
        write.write(f"{username}/{password}\n")
    print ("Account successfully created!")

    with open("log.txt", "a", encoding="utf-8") as reglog:
        reglog.write(f"\nA user created the account {username} at {current_time}\n")
    
    raise SystemExit("The program ended.")

    
    
def loggedin(current_user : User):
    alternatives = input("What do you want to do?\nlog: See account activity \npasswd: Change password\nlogout: log out \n To end, write anything else. \nWrite the command in the beginning of the alternatives: ")
    if (alternatives == "log"):
        with open ("log.txt", "r", encoding="utf-8") as readlog:
            for i in readlog.readlines():
                print(i)
        print("Closing software, please log in again!")

    elif (alternatives == "passwd"):
        current_user.passwd()

    elif (alternatives == "logout"):
        pass

    else: 
        raise SystemExit("The program ended.")

def save_users(users : list[User]):

    with open("users.txt", "w", encoding="utf-8") as f:
        for user in users:
            f.write(user.save())
    
def main():
    users = init_users()
    choice = input("What do you want to do?\nlogin: Log in\nreg: Register\n To end, write anything else. \nWrite the command in the beginning of the alternatives: ")
    if (choice == "login"):
        current_user = login(users)
        if isinstance(current_user, User):
            print ("You're now logged in!\n")
            loggedin(current_user)
        
    
    elif (choice == "reg"):
        register()

    else:
        save_users(users)
        raise SystemExit("The program ended.")

    save_users(users)

if __name__ == "__main__":
    main()
