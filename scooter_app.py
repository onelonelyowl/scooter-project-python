from scooter import Scooter
from user import User

class ScooterApp():
    
    stations = {"brentford": [], "ealing": [], "acton": []}
    registered_users = []
    rented_scooters = []
    
    def __init__(self) -> None:
        print("scooterApp created")
    
    def get_scooter(self, serial):
        try:
            for scootersAtStation in self.stations.values():
                foundMatch = [scooter for scooter in scootersAtStation if scooter.serial == serial]
                if len(foundMatch) > 0:
                    return foundMatch[0]  
            foundMatch = [scooter for scooter in self.rented_scooters if scooter.serial == serial]
            if len(foundMatch) > 0:
                    return foundMatch[0]
        except:
            print("could not find scooter anywhere")
    
    def get_user(self, username):
        try:
            foundUsers = [user for user in self.registered_users if user.username == username]
            return foundUsers[0]
        except:
            print("user could not be found by get_user() method")
                    
    def register_user(self, username, password, age):
        checkingDuplicateName = [user for user in self.registered_users if user.username == username]
        if len(checkingDuplicateName) != 0:
            raise Exception("A user already exists with that name") 
        if age < 18:
            raise Exception("You cannot register under the age of eighteen")
        if type(username) is not str or type(password) is not str:
            raise Exception("Username/password is not a string") 
        self.registered_users.append(User(username, password, age))
    
    def login_user(self, username, password):
        user = [user for user in self.registered_users if user.username == username]
        print(user)
        if user[0].password == password:
            try:
                user[0].login(password)
            except:
                print("login failed on the user.login() function somewhere")

    def logout_user(self, username):
        foundUser = [user for user in self.registered_users if user.username == username]
        if foundUser.loggedIn == False:
            raise ValueError("user is already logged out")
        else: foundUser.logout
   
    def create_scooter(self, station):
        if station not in ScooterApp.stations.keys():
            raise ValueError("Station not found in stations dict")
        self.stations[station].append(Scooter(station))
        print(f"Scooter created at {station}")
   
    def dock_scooter(self, scooter, station):
        if not isinstance(scooter, Scooter):
            raise TypeError("Scooter is a scooter object")
        if station not in self.stations.keys():
            raise ValueError("station not found in stations dict (docking)")
        try:
            scooter.dock(station)
            self.stations[station].append(scooter)
        except:
            f"there was an error docking scooter #{scooter.serial} at {station}"
        #maybe check if serial exists at station already, not sure if necessary
        
    def rent_scooter(self, scooter_serial, username):
        foundUser = self.get_user(username)
        if not isinstance(foundUser, User): # this correctly finds user
            raise LookupError("Couldn't find the passed user in the registered users")
        if foundUser.logged_in == False:
            raise Exception("User must be logged in to rent a scooter")
        try:
            foundScooter = None
            for scootersAtStation in self.stations.values():
                foundMatch = [scooter for scooter in scootersAtStation if scooter.serial == scooter_serial]
                if len(foundMatch) > 0:
                    foundScooter = foundMatch[0]
                    foundStation = scootersAtStation
            if foundScooter is not None: # this correctly finds scooter
                    foundStation.remove(foundScooter)
                    self.rented_scooters.append(foundScooter)
                    foundScooter.rent(foundUser) 
        except:
            raise Exception("Could not find the scooter at the station")
    