#   @memecian
#   toRegional.py
#   Turns text into Discord Emojis, specifically regional indicators.
#   GUI VERSION

inputString = input("Input Letters: ")

for c in inputString:
    if c.isalpha():
        print(":regional_indicator_" + c + ":", end = "")
    else:
        print(c, end = "")

input("\nPress Enter to quit")