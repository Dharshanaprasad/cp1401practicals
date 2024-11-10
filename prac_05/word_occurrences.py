def main():
    # Get user input for the text
    text = input("Text: ")
    words = text.split()

    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    longest_word_length = max(len(word) for word in word_count)

    print("\nWord occurrences:")
    for word in sorted(word_count):
        print(f"{word:{longest_word_length}} : {word_count[word]}")


if __name__ == "__main__":
    main()
