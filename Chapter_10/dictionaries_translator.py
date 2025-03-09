dictionary = {}

print("=== Creating a dictionary ===")

while True:
    i_english = input("Enter english word(quit ends): ").strip()
    if i_english.lower() == "quit":
        break
    i_finnish = input("Enter finnish word(quit ends): ").strip()
    dictionary[i_english] = i_finnish
    
print("\n=== Using a dictionary ===")

while True:
    i_english_word_to_translate = input("Enter english word(quit ends): ").strip()
    if i_english_word_to_translate.lower() == "quit":
        break

    if i_english_word_to_translate.lower() in dictionary:
        print(dictionary[i_english_word_to_translate])
    else:
        print("Unknown word")