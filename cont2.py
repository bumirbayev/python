# control flow

# we use control structures to alter control flow

def website_welcome(name, age):
    # we use boolean to control flow
    if(age >= 18):
        print("Welcome " + name + "!")
        print("You are very old:" + str(age))
    else:
        print("You are not welcome, you are too young")
        years_left = 18 - age
        print("Wait another " + str(years_left) + "years")

website_welcome("Beibarys", 27)
