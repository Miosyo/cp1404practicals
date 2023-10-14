"""
A program that shows the hex value of colors
"""

COLOR_TO_HEX = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                "Aqua": "#00ffff", "Baker Miller Pink": "#ff91af", "Bittersweet Shimmer": "#bf4f51",
                "British Racing Green": "#004225"}


def main():
    """Asks user for a color and prints the hex code"""
    for color_name in COLOR_TO_HEX:
        print(f"{color_name}")

    color_name = input("Color Name: ")
    while color_name != "":
        try:
            print(f"{COLOR_TO_HEX[color_name.title()]}")
        except KeyError:
            print("Invalid Color Choice")
        color_name = input("Color Name: ")


if __name__ == '__main__':
    main()
