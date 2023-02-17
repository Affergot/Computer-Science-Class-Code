import random
import time
class Dog:

    disobedient_behaviors = ['barking at the door', 'chewing your slippers', 'biting the baby', 'running away']
    known_tricks = ['sit', 'roll over', 'play dead', 'shake hands', 'speak',]

    def __init__(self, name):
        self.name = name
        self.bad_behavior = random.choice(Dog.disobedient_behaviors)


    def sit(self):
        obedience = random.randint(0, 4)
        if obedience < 3:
            print(self.name, "is now sitting.")
        else:
            print(self.name, "is too preoccupied ", end="")
            print(self.bad_behavior)
    
    def roll_over(self):
        obedience = random.randint(0, 4)
        if obedience < 3:
            print(self.name, "rolled over!")
        else:
            print(self.name, "is too preoccupied ", end="")
            print(self.bad_behavior)

    def play_dead(self):
        obedience = random.randint(0, 4)
        if obedience < 3:
            print(self.name, "layed on their tummy with their tounge out")
        else:
            print(self.name, "is too preoccupied ", end="")
            print(self.bad_behavior)

    def shake_hands(self):
        obedience = random.randint(0, 4)
        if obedience < 3:
            print(self.name, "truly demonstrates how distingished they are!")
        else:
            print(self.name, "is too preoccupied ", end="")
            print(self.bad_behavior)

    def speak(self):
        obedience = random.randint(0, 4)
        if obedience < 3:
            print(self.name, "*ruff* *ruff*\nWell said little one, well said")
        else:
            print(self.name, "WOAH, WHERE DID YOU LEARN SUCH FOUL WORDS?!")

    def check_if_action_in_known_tricks(self, input):
        if input not in Dog.known_tricks:
            print(f"{self.name} doesn't know what you mean by that")
            return False
        else:
            return True



    def play_with_dog(self):
        print(f"Here are some tricks {self.name} knows:")
        print(Dog.known_tricks)
        dog_action = input("")
        return dog_action

    def play_dog_action(self, action):
        if action == "sit":
            self.sit()
        elif action == "roll over":
            self.roll_over()
        elif action == "play dead":
            self.play_dead()
        elif action == "shake hands":
            self.shake_hands()
        elif action == "speak":
            self.speak()

if __name__ == "__main__":
    running = True
    print("Welcome to the Compute Doges!")
    print("Congratulations on your new dog!\nWhat would you like to name them?")
    dog_name = input("").title()
    PlayersDog = Dog(dog_name)
    time.sleep(1)
    print(f"Great! Now let's play with {PlayersDog.name}!")
    dog_action = PlayersDog.play_with_dog().lower()

    while running == True:
        while PlayersDog.check_if_action_in_known_tricks(dog_action) == False:
            dog_action = PlayersDog.play_with_dog()
        PlayersDog.play_dog_action(dog_action)
        time.sleep(1.5)
        print("Would you like to do anything else with your dog?")
        print("Type 'yes' or 'no'")
        answer = input("")
        if answer == "yes":
            dog_action = PlayersDog.play_with_dog().lower()
        elif answer == "no":
            print("Thanks for playing!")
            print(f"{PlayersDog.name} is now tired and will go to sleep waiting for you to play with them again tomorrow!")
            running = False



    