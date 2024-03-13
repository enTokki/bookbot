import sys


def main():
    location = sys.argv[1]
    book = open_book(location)
    character_list = character_alpha_list_sorted(book)

    print(f'--- Begin report of "{location}" ---')
    print(f"{word_count(book)} words found in the document")
    print("")
    for character in character_list:
        print(
            f"The '{character['char']}' character was found {character['count']} times"
        )
    print("--- End Report ---")


def open_book(file):
    with open(file) as f:
        file_contents = f.read()

        return file_contents


def word_count(book):
    return len(book.split())


def character_dictionary(book):
    characters = [*book.lower()]
    character_dictionary = {}

    for character in characters:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary


def character_alpha_list_sorted(book):
    character_list = []
    dictionary = character_dictionary(book)

    def sort_on(dictionary):
        return dictionary["count"]

    for character in dictionary:
        if character.isalpha():
            character_list.append({"char": character, "count": dictionary[character]})

    character_list.sort(reverse=True, key=sort_on)

    return character_list


if __name__ == "__main__":
    main()
