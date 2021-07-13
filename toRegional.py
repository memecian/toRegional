#   @memecian
#   toRegional.py
#   Turns text into Discord Emojis, specifically regional indicators.

inputString = input("Input Letters: ")
outputString = "\n"
for c in inputString:
    if c.isalpha():
        outputString.append(":regional_indicator" + c + ": ")
    else:
        outputString.append(c + " ")
print(outputString)
input("Press Enter to quit")