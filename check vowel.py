char = input("Enter a single alphabet: ").strip()

if len(char) == 1 and char.isalpha():
    if char.lower() in "aeiou":
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
else:
    print("Invalid input. Please enter a single letter.")
