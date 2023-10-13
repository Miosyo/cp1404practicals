"""
Word Occurrences
Estimate: 8 minutes
Actual:   10 minutes
"""


def main():
    """A program to count the occurrences of words in a sentence"""
    sentence = input("Words: ")
    word_to_count = {}
    for word in sentence.split():
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    print_words(word_to_count)


def print_words(word_to_count):
    """Formats and prints dictionary"""
    longest_word_length = max((len(word) for word in word_to_count))
    sorted_word_to_count = dict(sorted(word_to_count.items()))
    for word, count in sorted_word_to_count.items():
        print(f"{word:{longest_word_length}} : {count}")


if __name__ == '__main__':
    main()
