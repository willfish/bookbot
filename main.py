def count_words(contents: str):
    return len(contents.split())


def count_characters(contents: str):
    def sort_on(dict):
        return dict["count"]

    acc = {}
    for char in contents.lower():
        if not char.isalpha():
            continue

        if char in acc:
            acc[char] += 1
        else:
            acc[char] = 1

    characters: list[dict[str, int]] = []

    for key, value in acc.items():
        character = {"char": key, "count": value}
        characters.append(character)

    characters.sort(reverse=True, key=sort_on)

    return characters


book = "books/frankenstein.txt"
with open(book) as f:
    book_contents = f.read()
    words_count = count_words(book_contents)
    characters = count_characters(book_contents)
    print(f"--- Begin report of {book} ---")
    print(f"{words_count} words found in the document")
    print()
    for character in characters:
        print(f"The '{character['char']}' was found {character['count']} times")
    print(f"--- End report ---")
