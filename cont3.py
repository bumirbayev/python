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

def can_watch_movie(age, with_parents):
    if age >=17:
        return True
    else:
        if with_parents:
            return True
        else:
            return False

# check  the following 18, 16, 16, 2 , False, True
website_welcome("Beibarys", 27)

def can_watch(age, with_parents):
    if age >=17: # you can add "or with_parents, which will output same in different way
        return True
    elif age <17 and with_parents:
        return True
    else:
        return False
