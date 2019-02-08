"""
nug.py - A simple (and silly) calculator that, given a height in feet and inches
Tells you how many chicken nuggets tall you are
Inspired by https://www.reddit.com/r/CasualConversation/comments/ao63rv/im_approximately_39_chicken_nuggets_tall/
on /r/CasualConversation

tgo93
"""

import re

def main():
    playAgain = True
    pattern = "^(?!$|.*\'[^\x22]+$)(?:([0-9]+)\')?(?:([0-9]+)\x22?)?$"
    prog = re.compile(pattern) 
    # Avg height of chicken nugget
    nugget = 1.969
    
    while True:
        # User inputs height in ft and inches
        while True:
            try:
                height = input("How tall are you? (ex. 5'10\"): ")
                if prog.match(height) != None:
                    break
            except ValueError:
                continue
        h = height.split("'")

        # Calculate feet/inches into inches
        feet = int(h[0])
        inches = h[1]
        if len(inches) == 3:
            inches = int(h[1][:2])
        elif len(h[1]) == 2:
            inches = int(h[1][:1])
        else:
            inches = 0
            
        totalInches = (feet * 12) + inches 
        totalInches = float(totalInches)

        # Calculate output
        heightNugs = round(totalInches / nugget)
        print("You are " + str(heightNugs) + " chicken nuggets tall!")
        
        again = input("Try again? Yes or No: ")
        if again.lower() not in ['y', 'yes']:
            break
        
if __name__ == "__main__":
    main()
    
