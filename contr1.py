# Control flow
# Eat all apples and display Thank you for each apple you eat

 def eat_apples(num_of_apples):
    apples_remaining = num_of_apples

    # Eat an apple
    apples_remaining = apples_remaining - 1

    # Say thank you
    print("Thank you!")

    # Loop
    while apples_remaining > 0:
        apples_remaining -= 1
        print("Thank you!")

    print("Done")
    print(apples_remaining)
    return
