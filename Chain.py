import sys

class Handler:
    def __init__(self):
        self._successor = None

    def setHandler(self, successor):
        self._successor = successor

    def handleRequest(self):
        if (self._successor is not None):
            self._successor.handleRequest();



class ConcreteHandler1(Handler):
    def __init__(self):
        Handler.__init__(self)
        self._can_handle = False

    def handleRequest(self):
        if (self._can_handle):
            print("Handled by Concrete Handler 1.")
        else:
            print("Cannot be handled by Handler 1.")
            super().handleRequest()


class ConcreteHandler2(Handler):
    def __init__(self):
        Handler.__init__(self)
        self._can_handle = True

    def handleRequest(self):
        if (self._can_handle):
            print("Handled by Concrete Handler 2.")
        else:
            print("Cannot be handled by Handler 2.")
            super().handleRequest()


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()

    handler1.setHandler(handler2)
    handler1.handleRequest()