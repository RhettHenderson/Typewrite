import sys 
 
import time 

def slowPrint(message, delay=0.2):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

def help():
        print("Syntax: slowPrint(message, (optional)delay)")





