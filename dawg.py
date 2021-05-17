import random

Chinese = ["General Tso", "Dumplings", "Sweet and Sour Chicken"]
Mexico = ["Taco", "Enchillada", "Gyro"]
Ohio = ["Maxican Food", "A Hot Dog", "BEANS"]
Kentucky = ["Popeyes", "Fried Chicken", "KFC"]
def what_to_eat():
    place = input("What would you like to eat?" + "\n" + "1) Chinese" + "\n" + "2) Mexican" + "\n" + "3) Ohio" + "\n" + "4) Kentucky" + "\n" + "5) Im Feeling Lucky" + "\n" + "Enter 1-5: ")
    if place == "1":
        print("\n" + "Ight Get this Dawg Something to eat")
        print("You should eat: " + random.choice (Chinese))
    elif place == "2":
        print("\n" + "Ight Get this Dawg Something to eat")
        print("You should eat: " + random.choice (Mexico))
    elif place == "3":
        print("\n" + "Ight Get this Dawg Something to eat")
        print("You should eat: " + random.choice (Ohio))
    elif place == "4":
        print("\n" + "Ight Get this Dawg Something to eat")
        print("You should eat: " + random.choice (Kentucky))
    elif place == "5":
        random_number = random.randint(1,4)
        #print("Number generated: " + str(random_number))
        print("\n" + "Feeling Lucky is see... you should eat: ")
        if random_number == 1:
            print("You should eat: " + random.choice (Chinese))
        elif random_number == 2:
            print("You should eat: " + random.choice (Mexico))
        elif random_number == 3:
            print("You should eat: " + random.choice (Ohio))
        elif random_number == 4:
            print("You should eat: " + random.choice (Kentucky))
    else:
        print("Please input 1 through 5 only")

what_to_eat()