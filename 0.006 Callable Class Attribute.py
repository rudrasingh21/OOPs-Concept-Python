'''
class has either be DATA ATTRIBUTE or FUNCTION ATTRIBUTE
'''
class Program:
    language = 'Python'             #DATA ATTRIBUTE

    def say_hello(self=None):       #FUNCTION ATTRIBUTE
        print(f'Hello From {Program.language}')

print(Program.__dict__)
#{'__module__': '__main__', 'language': 'Python', 'say_hello': <function Program.say_hello at 0x00000185BA2C1D90>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}

print(Program.say_hello)
#<function Program.say_hello at 0x000001671EF71D90>

Program.say_hello()
#Hello From Python

getattr(Program,'say_hello')()
#Hello From Python

Program.__dict__['say_hello']()
#Hello From Python