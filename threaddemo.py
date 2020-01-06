from threading import Thread


class Person(Thread):
    def __init__(self):
        Thread.__init__(self)
        pass
    def run(self):
        print('hello')

if __name__ == '__main__':
    person = Person()
    person.start()