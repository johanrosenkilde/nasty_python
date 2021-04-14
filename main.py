"""
This module has utf-8 emojis everywhere and local classes.
Good luck!

Here are some emoji: 
\U0001F44B \U0001F44D \U0001F44E \U0001F44C

Here is "Hello, my friend is a stick" written in chinese: 
\U0001F64C \U0001F3F7 \U00002764 \U00002795 \U00002709 \U00002728 \U00002764
🤪
"""
def friendly_message():
    """Display an emoji-filled message"""
    print("Hello stranger")
    print("\U0001F646 \U0001F646 \U0001F646 \U0001F646")
    print("🤪")
 
def has_a_class_inside():
    """A function with a local class"""

    class MyClass:
        """A local class"""

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




 
