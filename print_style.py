import time


# Textanimation für Print
def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# Textanimation für Input
def slow_input(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()
