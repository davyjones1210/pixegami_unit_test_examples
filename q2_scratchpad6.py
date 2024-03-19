import mock


def yes_or_no():
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        print("Quitter!")
    elif answer == "no":
        print("Awesome!")
    else:
        print("BANG!")


def test_quitting():

    with mock.patch('builtins.input', return_value="yes"):
        assert yes_or_no() == "Quitter!"

    with mock.patch('builtins.input', return_value="no"):
        assert yes_or_no() == "Awesome!"