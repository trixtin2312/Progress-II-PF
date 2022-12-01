from abc import ABC, abstractmethod

class PlayerDecorator(ABC):
    @abstractmethod
    def movement(self, c):
        pass

class BasePlayer:
    def __init__(self):
        pass
    
    def movement(self, c):
        if   c=='w':
            print('moving forward')
        elif c == 'a':
            print('moving left')
        elif c == 's':
            print('moving back')
        elif c == 'd':
            print('moving right')
        elif c == 'e':
            print('attacking ')
        elif c == ' ':
            print('jumping')
        else:
            print('undefined command')
            
class player1(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee
        
    def movement(self, c):
        if c == 'e':
            print('using fire ', end='')
        
        self.wrapee.movement(c)
        
class player2(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee
        
    def movement(self, c):
        if c == 'e':
            print('with arrows ', end='')
            
        self.wrapee.movement(c)
        
class player3(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee
        
    def movement(self, c):
        if c == ' ':
            print('double jump')
        else:
            self.wrapee.movement(c)

print("Base Player")
player = BasePlayer()
player.movement('e')
player.movement(' ')

print("Player 1")
player = player1(player)
player.movement('e')
player.movement(' ')

print("Player 3")
player = player3(player)
player.movement('e')
player.movement(' ')

#decorator
print("Player 2")
player = player2(player)
player.movement('e')
player.movement(' ')