import json
import time
__ActiveSave = 0


def titleScreen():
        print("Select your save file")
        try:
            with open('save1.json', 'r') as file:
                save1 = json.load(file)
        except FileNotFoundError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save1.json', 'w') as fp:
                json.dump(database, fp)
        except KeyError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save1.json', 'w') as fp:
                json.dump(database, fp)
        print(f"1. {save1['SaveFile']}")
            

        try:
            with open('save2.json', 'r') as file:
                save2 = json.load(file)
        except FileNotFoundError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save2.json', 'w') as fp:
                json.dump(database, fp)
        except KeyError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save2.json', 'w') as fp:
                json.dump(database, fp)
        print(f"2. {save2['SaveFile']}")
        
        try:
            with open('save3.json', 'r') as file:
                save3 = json.load(file)
        except FileNotFoundError or KeyError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save3.json', 'w') as fp:
                json.dump(database, fp)
        except KeyError:
            database = {}
            database["SaveFile"] = "Empty Save"
            with open('save3.json', 'w') as fp:
                json.dump(database, fp)
        print(f"3. {save3['SaveFile']}")

        choice = input("Enter your choice: ")
        global __ActiveSave
        if choice == "1":
            __ActiveSave = 1
        elif choice == "2":
            __ActiveSave = 2
        elif choice == "3":
            __ActiveSave = 3
        else:
            print("That is not a valid choice")
            time.sleep(1)
            titleScreen()

def saveToFile(database):
    if __ActiveSave == 1:
        with open('save1.json', 'w') as fp:
            json.dump(database, fp)
    elif __ActiveSave == 2:
        with open('save2.json', 'w') as fp:
            json.dump(database, fp)
    elif __ActiveSave == 3:
        with open('save3.json', 'w') as fp:
            json.dump(database, fp)

def loadFromFile():
    if __ActiveSave == 1:
        with open('save1.json', 'r') as file:
            database = json.load(file)
            return database
    elif __ActiveSave == 2:
        with open('save2.json', 'r') as file:
            database = json.load(file)
            return database
    elif __ActiveSave == 3:
        with open('save3.json', 'r') as file:
            database = json.load(file)
            return database

def newFile():
        database = loadFromFile()
        print("You have no save file")
        time.sleep(1)
        print("...Creating new save file...")
        time.sleep(1)
        print("What do you want your name to be?")
        name = input("Enter your name: ")
        database["SaveFile"] = name
        database["Money"] = "15.00"
        database["Eggs"] = 3
        database["Chicken Feed"] = 10
        database["Chickens"] = 0
        database["CalanderDay"] = 1
        saveToFile(database)

def introduction():
    database = loadFromFile()
    print(f"Welcome to the Chicken Farm {database['SaveFile']}!")
    time.sleep(1)
    print("I hear you're the new farmer around here.")
    time.sleep(1)
    print("Your old man really took care of this place.")
    time.sleep(1)
    print("I'm sure you'll do just as good of a job.")
    time.sleep(1)
    print("I know he wasn't able to leave you a whole lot so I took the liberty of "
        "giving you some money and eggs to start things back up again.")
    time.sleep(2)

def openStore():
    print('Welcome to the store!')
    time.sleep(1)
    print('What brings you by today?')
    print('1. Buy items')
    print('2. Sell items')
    print('3. Leave the store')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        time.sleep(1)
        buyStore()
    elif choice == 2:
        time.sleep(1)
        sellStore()
    elif choice == 3:
        time.sleep(1)
        hub()
    else:
        print('That is not a valid choice.')
        time.sleep(1)
        openStore()

def hub():
    print("What would you like to do?")
    print("1. Go to the Store")
    print("2. Go to the Farm")
    print("3. Save and Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        time.sleep(1)
        openStore()
    elif choice == 2:
        time.sleep(1)
        farm()
    elif choice == 3:
        time.sleep(1)
        database = loadFromFile()
        print("Saving...")
        time.sleep(1)
        print("Goodbye!")
        time.sleep(1)
        saveToFile(database)
        exit()
    else:
        print("That is not a valid choice.")
        time.sleep(1)
        hub()

def buyStore():
    database = loadFromFile()
    print('1. Buy Eggs')
    print('2. Buy Chicken Feed')
    print('3. Buy a Chicken')
    print('4. Back to main menu')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('Eggs cost $1.00 each.')
        print(f'You have ${database["Money"]}')
        print(f'You have {database["Eggs"]} eggs')
        print('How many eggs do you want to buy?')
        while True:
            try:
                eggs = int(input('Enter number of eggs: '))
                break
            except ValueError:
                print('That is not a valid choice.')
        if eggs < 0:
            print('You cannot buy a negative number of eggs.')
            buyStore()
        if eggs == 0:
            buyStore()
        if eggs * 1.00 > float(database["Money"]):
            print("You don't have enough money.")
            buyStore()
        else:
            priceOfEggs = eggs * 1.00
            print(f'{eggs} eggs will cost ${priceOfEggs:.2f}')
            choice = input('Are you sure you want to buy these? (y/n): ')
            if choice == 'y':
                newWallet = float(database["Money"]) - priceOfEggs
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Eggs"] += eggs
                print(f'You now have {database["Eggs"]} eggs')
                print(f'You now have ${database["Money"]}')
                saveToFile(database)
                buyStore()
            elif choice == 'n':
                buyStore()
            else:
                print('That is not a valid choice.')
                buyStore()
    elif choice == 2:
        print('Chicken Feed costs $0.25 per bag.')
        print(f'You have ${database["Money"]}')
        print(f'You have {database["Chicken Feed"]} bags of chicken feed')
        print('How many bags of chicken feed do you want to buy?')
        while True:
            try:
                feed = int(input('Enter number of bags: '))
                break
            except ValueError:
                print('That is not a valid choice.')
        if feed < 0:
            print('You cannot buy a negative number of bags of chicken feed.')
            buyStore()
        if feed == 0:
            buyStore()
        if feed * 0.25 > float(database["Money"]):
            print("You don't have enough money.")
            buyStore()
        else:
            priceOfChickenFeed = feed * 0.25
            print(f'{feed} bags of chicken feed will cost ${priceOfChickenFeed:.2f}')
            choice = input('Are you sure you want to buy these? (y/n): ')
            if choice == 'y':
                newWallet = float(database["Money"]) - priceOfChickenFeed
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Chicken Feed"] += feed
                print(f'You now have {database["Chicken Feed"]} bags of chicken feed')
                print(f'You now have ${database["Money"]}')
                saveToFile(database)
                buyStore()
            elif choice == 'n':
                buyStore()
            else:
                print('That is not a valid choice.')
                buyStore()
    elif choice == 3:
        print('A chicken costs $5.00')
        print(f'You have ${database["Money"]}')
        print(f'You have {database["Chickens"]} chickens')
        print('How many chickens do you want to buy?')
        while True:
            try:
                chicken = int(input('Enter number of chickens: '))
                break
            except ValueError:
                print('That is not a valid choice.')
        if chicken < 0:
            print('You cannot buy a negative number of chickens.')
            buyStore()
        if chicken == 0:
            buyStore()
        if chicken * 5.00 > float(database["Money"]):
            print("You don't have enough money.")
            buyStore()
        else:
            priceOfChickens = chicken * 5.00
            print(f'{chicken} chickens will cost ${priceOfChickens:.2f}')
            choice = input('Are you sure you want to buy these? (y/n): ')
            if choice == 'y':
                newWallet = float(database["Money"]) - chicken * 5.00
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Chickens"] += chicken
                print(f'You now have {database["Chickens"]} chickens')
                print(f'You now have ${database["Money"]}')
                saveToFile(database)
                buyStore()
            elif choice == 'n':
                buyStore()
            else:
                print('That is not a valid choice.')
                buyStore()
    elif choice == 4:
        openStore()
    else:
        print('That is not a valid choice.')
        buyStore()
        
def sellStore():
    database = loadFromFile()
    print("What would you like to sell?")
    print("1. Sell Eggs")
    print("2. Sell Chicken Feed")
    print("3. Sell a Chicken")
    print("4. Go back to menu")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Eggs sell for $0.50 each.")
        print(f"You have {database['Eggs']} eggs")
        print("How many eggs do you want to sell?")
        while True:
            try:
                eggs = int(input("Enter number of eggs: "))
                break
            except ValueError:
                print("That is not a valid choice.")
        if eggs < 0:
            print("You cannot sell a negative number of eggs.")
            sellStore()
        if eggs == 0:
            sellStore()
        if eggs > database["Eggs"]:
            print("You don't have enough eggs.")
            sellStore()
        else:
            eggSellPrice = eggs * 0.50
            print(f"{eggs} eggs will sell for ${eggSellPrice:.2f}")
            choice = input("Are you sure you want to sell these? (y/n): ")
            if choice == 'y':
                newWallet = float(database["Money"]) + eggSellPrice
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Eggs"] -= eggs
                print(f"You now have {database['Eggs']} eggs")
                print(f"You now have ${database['Money']}")
                saveToFile(database)
                sellStore()
            elif choice == 'n':
                sellStore()
            else:
                print("That is not a valid choice.")
                sellStore()
    elif choice == 2:
        print("Chicken Feed sells for $0.10 per bag.")
        print(f"You have {database['Chicken Feed']} bags of chicken feed")
        print("How many bags of chicken feed do you want to sell?")
        while True:
            try:
                feed = int(input("Enter number of bags: "))
                break
            except ValueError:
                print("That is not a valid choice.")
        if feed < 0:
            print("You cannot sell a negative number of bags of chicken feed.")
            sellStore()
        if feed == 0:
            sellStore()
        if feed > database["Chicken Feed"]:
            print("You don't have enough bags of chicken feed.")
            sellStore()
        else:
            feedSellPrice = feed * 0.10
            print(f"{feed} bags of chicken feed will sell for ${feedSellPrice:.2f}")
            choice = input("Are you sure you want to sell these? (y/n): ")
            if choice == 'y':
                newWallet = float(database["Money"]) + feedSellPrice
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Chicken Feed"] -= feed
                print(f"You now have {database['Chicken Feed']} bags of chicken feed")
                print(f"You now have ${(database['Money'])}")
                saveToFile(database)
                sellStore()
            elif choice == 'n':
                sellStore()
            else:
                print("That is not a valid choice.")
                sellStore()
    elif choice == 3:
        print("Chickens sell for $2.50 each.")
        print(f"You have {database['Chickens']} chickens")
        print("How many chickens do you want to sell?")
        while True:
            try:
                chicken = int(input("Enter number of chickens: "))
                break
            except ValueError:
                print("That is not a valid choice.")
        if chicken < 0:
            print("You cannot sell a negative number of chickens.")
            sellStore()
        if chicken == 0:
            sellStore()
        if chicken > database["Chickens"]:
            print("You don't have enough chickens.")
            sellStore()
        else:
            chickenSellPrice = chicken * 2.50
            print(f"{chicken} chickens will sell for ${chickenSellPrice:.2f}")
            choice = input("Are you sure you want to sell these? (y/n): ")
            if choice == 'y':
                newWallet = float(database["Money"]) + chickenSellPrice
                database["Money"] = str(newWallet.__format__('.2f'))
                database["Chickens"] -= chicken
                print(f"You now have {database['Chickens']} chickens")
                print(f"You now have ${database['Money']}")
                saveToFile(database)
                sellStore()
            elif choice == 'n':
                sellStore()
            else:
                print("That is not a valid choice.")
                sellStore()
    elif choice == 4:
        openStore()
    else:
        print("That is not a valid choice.")
        sellStore()

def farm():
    print("What would you like to do?")
    print("1. Visit the Chicken Coop")
    print("2. Go to the Store")
    print("3. Go to sleep for the day")
    print("4. Back to main menu")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        chickenCoop()
    elif choice == 2:
        openStore()
    elif choice == 3:
        sleep()
    elif choice == 4:
        hub()
    else:
        print("That is not a valid choice.")
        farm()

def sleep():
    database = loadFromFile()
    print("You go to sleep for the day.")
    time.sleep(1)
    print("You wake up the next morning.")
    database["CalanderDay"] = database["CalanderDay"] + 1
    saveToFile(database)
    time.sleep(1)
    print("It is now day", str(database['CalanderDay']) + ".")
    time.sleep(1)
    farm()

def chickenCoop():
    print("What would you like to do?")
    time.sleep(1)
    print("1. Feed the chickens")
    print("2. Collect eggs")
    print("3. Check on the incubator")
    print("4. Back to farm")
    choice = int(input("Enter your choice: "))
    time.sleep(1)
    if choice == 1:
        #feedChickens()
        pass
    elif choice == 2:
        #collectEggs()
        pass
    elif choice == 3:
        #incubator()
        pass
    elif choice == 4:
        farm()
    else:
        print("That is not a valid choice.")
        chickenCoop()

def exit():
    pass

def main():
    titleScreen() #Changes Active Save
    playersave = loadFromFile() #Loads the save selected from 1-3
    if playersave["SaveFile"] == "Empty Save":
        newFile()
        introduction()
    else:
        print(f'Welcome back {playersave["SaveFile"]}')
    time.sleep(1)
    hub()



#Show user options from store and give their current money amount
if __name__ == '__main__':
    main()
