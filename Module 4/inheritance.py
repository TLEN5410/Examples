class Dog():
    def walk(self):
        print "I can walk with 4 legs!"

    def bark(self):
        print "Woof"

    def bite(self):
        print "My bark is worse"

class FoxHound(Dog):
    def hunt(self):
        pass

    def howl(self):
        print "Hooooowwwwwllll!!"

class Chihuahua(Dog):
    def yap(self):
        print "Yap yap yap yap yap!!"

class FoxChi(FoxHound, Chihuahua):
    ''' Contains methods from Dog, FoxHound, and Chiuahua '''
    pass

fluffy = FoxHound()
fluffy.howl()
fluffy.bark()
buddy = Chihuahua()
buddy.yap()
buddy.bark()
duke = FoxChi()
duke.howl()
duke.yap()
duke.bark()

