"""
Wimbledon
Estimate: 30 minutes
Actual: 50 minutes
"""
import csv
from collections import Counter

FILENAME = "wimbledon.csv"


def main():
    """This program reads wimbledon winning statistics from a file and displays the winners"""
    wimbledon_data = get_wimbledon_data()
    champions_to_wins = get_champions(wimbledon_data)
    print_champions(champions_to_wins)
    print_winning_countries(wimbledon_data)


def print_winning_countries(wimbledon_data):
    """Prints the countries that have win wimbledon"""
    wimbledon_winning_countries = set(country for country in [row[1] for row in wimbledon_data])
    print(f"These {len(wimbledon_winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(wimbledon_winning_countries)))


def get_champions(wimbledon_data):
    """Returns a dict of wimbledon champions and their win count"""
    return Counter(([row[2] for row in wimbledon_data]))


def print_champions(champions_to_wins):
    """Prints the wimbledon champions"""
    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion} {wins}")


def get_wimbledon_data():
    """Reads wimbledon.csv and returns a list of lists"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # remove and discard the first line as it contains no data
        csv_reader = csv.reader(in_file)
        wimbledon_data = list(csv_reader)
    return wimbledon_data


if __name__ == '__main__':
    main()
