

class Fruit:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        print("Getting name.")
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name



if __name__ == '__main__':
    fruit = Fruit('Banana')
    fruit.set_name('Orange')
    print(fruit.get_name())

