# control flow

def eat_fruit(num_of_apples):
    apples_remaining = num_of_apples
    while apples_remaining > 0:
        apples_remaining -= 1
        print("Thank you!")
    print("Done")
    return

def eat_apples(num_of_apples, on_diet):
    apples_remaining = num_of_apples
    while apples_remaining > 0 and not on_diet:
        apples_remaining -= 1
        print("Thank you!")
    print("Done")
    return

#check in py charm: eat_apples(8, true) - Done eat_apples(8, apples) - Thank you 8 times, False

# Functions, control statements is must have to do a lot of programming. With that computer can do a lot of thing
