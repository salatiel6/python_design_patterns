from src import message


def run_element_one():
    """Runs the default say() method, and then chages the message"""
    element_one = message
    print("ELEMENT ONE")
    element_one.say()
    element_one.change_message("Message changed")
