
def yes_or_no():
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        print("Quitter!")
    elif answer == "no":
        print("Awesome!")
    else:
        print("BANG!")

if __name__ == '__main__':
    yes_or_no()


# Running from cmd prompt: python -c "from q2_scratchpad4 import *; yes_or_no()"

