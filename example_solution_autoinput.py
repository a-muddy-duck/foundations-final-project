def import_madlib_skeleton():
#     madlib_file = open("madlib_skeleton.txt")
#     madlib = madlib_file.read()
#     madlib_file.close()
    madlib = "A day in the life of my CSC110 professor, {profname}/nFirst, {profname} wakes up and makes a {temperature_adj} cup of {bev_noun}. After getting to work, they {move_verb} to {smith_building_name}. They turn on their i{tech_noun} but right away it looks like it is {tech_adj}. They make a loud {onomatopoeia} noise and decide the {superlative} way to fix it is to {verb_sequence}. {adverb}, it doesn't work. {profname} goes to teach their {int_students} {student_adj} students about {plural_noun}. The end!"
    return madlib
def lazy_skip():
    profname = "Jordan"
    temperature_adj = "flat"
    tech_adj = "steampunk"
    student_adj = "brilliant"
    bev_noun = "cocoa"
    move_verb = "boogie"
    smith_building_name = "McConnell"
    tech_noun = "Tablet"
    onomatopoeia = "BOOM!"
    superlative = "crunchiest"
    verb_sequence = "run a marathon"
    adverb = "Scandalously"
    int_students = 9
    plural_noun = "heirloom apples"
    
    filled_blanks = {"profname" : profname, "temperature_adj" : temperature_adj,
                     "tech_adj" : tech_adj, "student_adj" : student_adj,
                     "bev_noun" : bev_noun, "move_verb" : move_verb, "smith_building_name" : smith_building_name,
                     "tech_noun" : tech_noun, "onomatopoeia" : onomatopoeia, "superlative" : superlative,
                     "verb_sequence" : verb_sequence, "adverb" : adverb, "int_students" : int_students,
                     "plural_noun" : plural_noun}
    return(filled_blanks)


def main():
    madlib = import_madlib_skeleton()
    profname = "Jordan"
    temperature_adj = "flat"
    tech_adj = "steampunk"
    student_adj = "brilliant"
    bev_noun = "cocoa"
    move_verb = "boogie"
    smith_building_name = "McConnell"
    tech_noun = "Tablet"
    onomatopoeia = "BOOM!"
    superlative = "crunchiest"
    verb_sequence = "run a marathon"
    adverb = "Scandalously"
    int_students = 9
    plural_noun = "heirloom apples"
    
    filled_blanks = {"profname" : profname, "temperature_adj" : temperature_adj,
                     "tech_adj" : tech_adj, "student_adj" : student_adj,
                     "bev_noun" : bev_noun, "move_verb" : move_verb, "smith_building_name" : smith_building_name,
                     "tech_noun" : tech_noun, "onomatopoeia" : onomatopoeia, "superlative" : superlative,
                     "verb_sequence" : verb_sequence, "adverb" : adverb, "int_students" : int_students,
                     "plural_noun" : plural_noun}
    print(filled_blanks)
    
    blanks_list = [profname, temperature_adj, tech_adj, student_adj, bev_noun, move_verb,
                  smith_building_name, tech_noun, onomatopoeia, superlative, verb_sequence, adverb, int_students, plural_noun]
    #print(blanks_list)
    print(madlib.format_map(blanks_list))
    
    
    print(madlib.format(profname = "Jordan",
    temperature_adj = "flat",
    tech_adj = "steampunk",
    student_adj = "brilliant",
    bev_noun = "cocoa",
    move_verb = "boogie",
    smith_building_name = "McConnell",
    tech_noun = "Tablet",
    onomatopoeia = "BOOM!",
    superlative = "crunchiest",
    verb_sequence = "run a marathon",
    adverb = "Scandalously",
    int_students = 9,
    plural_noun = "heirloom apples"))
    
    
    start = ""
    for k, v in filled_blanks.items():
        start += f"{k} = '{v}', "
    print(start)
    print(madlib.format(start)) # this does not work but if you paste the contents of start it does
    ### these ones work:
    #print(f"A day in the life of my CSC110 professor, {profname}\n\nFirst, {profname} wakes up and makes a {temperature_adj} cup of {bev_noun}. After getting to work, they {move_verb} to {smith_building_name}. They turn on their i{tech_noun} but right away it looks like it is {tech_adj}. They make a loud {onomatopoeia} noise and decide the {superlative} way to fix it is to {verb_sequence}. {adverb}, it doesn't work. {profname} goes to teach their {int_students} {student_adj} students about {plural_noun}. The end!".format(profname, temperature_adj, tech_adj, student_adj, bev_noun, move_verb, smith_building_name,tech_noun, onomatopoeia, superlative, verb_sequence, adverb, int_students, plural_noun))

if __name__ == "__main__":
    main()

