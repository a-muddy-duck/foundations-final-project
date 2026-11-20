def import_madlib_skeleton():
    madlib_file = open("madlib_skeleton.txt")
    madlib = madlib_file.read()
    madlib_file.close()
    return madlib

def fill_in_blanks():
    profname = get_cap_input("Give me the name of your CSC110 professor: ")
    if profname == "Skip":
        from example_solution_autoinput import lazy_skip
        skipvals = lazy_skip()
        return skipvals
    temperature_adj, tech_adj, student_adj = input("Give me three adjectives separated by spaces: ").split()
    bev_noun = input("Give me a drinkable noun: ")
    move_verb = get_move_verb()
    smith_building_name = get_cap_input("Give me the name of your favorite campus building: ")
    tech_noun = get_cap_input("Give me a type of tech device (real or made up): ")
    onomatopoeia = input("Give me an onomatopoeia (a sound effect): ").upper() + "!"
    superlative = input("Give me a superlative (ex. best, pinkest, sleepiest, etc.): ")
    verb_sequence = input("Give me a short sentence starting with a verb (ex. drink a glass of orange juice): ")
    adverb = get_adverb()
    int_students = int(input("Give me a whole number: ")) + 1
    plural_noun = get_plural_noun()
    filled_blanks_dict = {"profname" : profname, "temperature_adj" : temperature_adj,
                     "tech_adj" : tech_adj, "student_adj" : student_adj,
                     "bev_noun" : bev_noun, "move_verb" : move_verb, "smith_building_name" : smith_building_name,
                     "tech_noun" : tech_noun, "onomatopoeia" : onomatopoeia, "superlative" : superlative,
                     "verb_sequence" : verb_sequence, "adverb" : adverb, "int_students" : int_students,
                     "plural_noun" : plural_noun}
    return(filled_blanks_dict)
    #return(profname, temperature_adj, tech_adj, student_adj, bev_noun, move_verb, smith_building_name,
    #      tech_noun, onomatopoeia, superlative, verb_sequence, adverb, int_students, plural_noun)
    
def get_adverb():
    adverb = input("Give me an adverb: ").lower()
    if adverb.endswith("ly"):
        pass
    else:
        print("Make sure your adverb ends in -ly.")
        get_adverb()
    return adverb.title()

def get_move_verb():
    mystery_number = int(input("Give me a number between 1 and 4: "))
    if mystery_number == 1:
        return "meander"
    elif mystery_number == 2:
        return "boogie"
    elif mystery_number == 3:
        return "cartwheel"
    elif mystery_number == 4:
        return "prance"
    else:
        print("Read the instructions again and only come back once you've thought about the consequences of your actions.")
        get_move_verb()
    
def get_plural_noun():
    plural_noun = input("Give me a plural noun: ").lower()
    if (plural_noun.endswith("s")):
        return plural_noun
    else:
        print("Try something more conventional? We love being fungis around here but fun guys are better (in a plural sense).")
        get_plural_noun()
        
def get_cap_input(prompt):
    return input(prompt).title()
    
def main():
    madlib = import_madlib_skeleton()
    filled_blanks_dict = fill_in_blanks()
#     print(type(filled_blanks_dict))
#     print(filled_blanks_dict)
    print(madlib.format_map(filled_blanks_dict)) #format_map wants a dictionary
if __name__ == "__main__":
    main()
