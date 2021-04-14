"""
This module has utf-8 emojis everywhere and local classes.
Good luck!

Here is a list of emoji as utf-8 characters:
🤪 🤫 🤬 🤭 🤮 🤯 🤰 🤱 🤲 🤳 🤴 🤵 🤶 🤷

Here is "Hello, my friend is a stick" written in chinese: 
🤪 🤪 🤪 🤪 🤪 🤪 🤪 🤪 🤪 🤪
"""
def friendly_message():
    """Display an emoji-filled message, e.g. 🤵 🤶 🤷.
    Or, 🤪 🤫 🤬.
    I start at byte 304, and end at byte 692.
    """
    print("Hello stranger")
    mes = "🤪 🤫 🤬 🤭 🤮 🤯 🤰 🤱 🤲 🤳 🤴 🤵 🤶 🤷"
    print(mes)
    print("The message was %s characters but %s bytes long." % (len(mes), len(bytes(mes, 'utf-8'))))
    
def multiply_by_3(x):
    """🤪 🤫 🤬 Multiply the input `x` by 3."""
    return x * 3
 
def has_a_class_inside():
    """A function with a local class"""

    class MyClass:
        """A local class. 🤬 🤭"""

        def __init__(self, name):
            """A local class"""
            self.name = name

        def say_hi(self):
            """Say hello, object"""
            print(f"Hi, I'm {self.name} 🤪")

    my_class = MyClass("Bob")
    my_class.say_hi()

if __name__ == "__main__":
    friendly_message()
    has_a_class_inside()
    # Print this module's docstring
    print(__doc__)




 
