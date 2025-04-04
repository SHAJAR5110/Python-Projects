def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks below.")

    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")

    
    story = f"""
    One day, a {adjective} {animal} was walking through {place}.
    It saw a {noun} and got very excited.
    So, it {verb} all around happily!
    """

    
    print("\nHere is your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    mad_libs()
