
import random
import json # to import in json format
       
race = ['Human','Elf', 'Dwarf', 'Halfling']

Classes = ['Paladin', 'Fighter', 'Rogue', 'Bard', 'Wizard']

genders = ['Male','Female']

Human_male_names = ['Aaron','Brad','Liam','Zeke']
Human_female_names = ['Feli', 'Jahira', 'Neria','Katie']
Human_last_name = ['Smith','Grey','Brown','Valentine']

elf_and_half_male_names =['Ayred','Theoden','Illidan', 'Rhoden']
elf_and_half_female_names = ['Saria','Tisha','Ahshala','Analeria']
elf_and_half_last_name = ['Qiharice','Yinmaris', 'Enerion','Faemenor']

dwarf_male_names = ['Kurzan','Gimili','Damien','Lurgrulir']
dwarf_female_names = ['Fokrire','Jargebelle','Sirathra','Dimbranch']
dwarf_last_name = ['Warfury','Onyxgrip','Berylpike','Greatrock']

halfling_male_names = ['Frodo','Gollum','Sam','Mike']
halfling_female_names = ['Jillian','irabee','Senna','Callie']
halfling_last_names = ['Baggins','Gamgie','Took','Keep']


def Get_Random_Name(race, gender): # function to get random names
    name = ''
    
    if race == 'Human' and gender == 'Male':
        name = Human_male_names[random.randint(0,len(Human_male_names)-1)]
    if race == 'Human' and gender == 'Female':
        name = Human_female_names[random.randint(0,len(Human_female_names)-1)]
        
    if race == 'Elf' and gender == 'Male':
        name = elf_and_half_male_names[random.randint(0,len(elf_and_half_male_names)-1)]
    if  race == 'Elf' and gender == 'Female':
        name = elf_and_half_female_names[random.randint(0,len(elf_and_half_female_names)-1)]
    
    if race == 'Dwarf' and gender == 'Male':
        name = dwarf_male_names[random.randint(0,len(dwarf_male_names)-1)]
    if race == 'Dwarf' and gender == "Female":
        name = dwarf_female_names[random.randint(0,len(dwarf_female_names)-1)]
        
    if race == 'Halfling' and gender == 'Male':
        name = halfling_male_names[random.randint(0,len(halfling_male_names)-1)]
    if race == 'Halfling' and gender == 'Female':
        name = halfling_female_names[random.randint(0,len(halfling_female_names)-1)]
        
    match race:
        case 'Human':
                name+= f' {Human_last_name[random.randint(0,len(Human_last_name)-1)]}'
        case 'Elf':
            name+= f' {elf_and_half_last_name[random.randint(0,len(elf_and_half_last_name)-1)]}'
        case 'Dwarf':
            name+= f' {dwarf_last_name[random.randint(0,len(dwarf_last_name)-1)]}'
        case 'Halfling':
            name+= f' {halfling_last_names[random.randint(0,len(halfling_last_names)-1)]}'
    
    return name

def Get_Stats(Character_class): # to get scores for attributes
    scores = []
    
    for x in range(6): # outer loop to get scores for stats
        
        score = [] # inner loop to get one score for stats
        for x in range(4):
            
            score.append(random.randint(1, 6)) # first, get 4d6 roll
        score = sorted(score)
        score.pop(0) # then we remove the smallest roll
        scores.append(sum(score))
        
    scores=sorted(scores)
    Arranged_scores = {'STR':0, 'DEX':0, 'CON':0, 'INT':0 ,'WIS':0, 'CHA':0}
    
    match Character_class:
        case 'Paladin':
            Arranged_scores['STR'] = scores[5]
            Arranged_scores['CON'] = scores[3]
            Arranged_scores['CHA'] = scores[4]
            Arranged_scores['DEX'] = scores[2]
            Arranged_scores['WIS'] = scores[1]
            Arranged_scores['INT'] = scores[0]
        case 'Fighter':
            Arranged_scores['STR'] = scores[5]
            Arranged_scores['CON'] = scores[4]
            Arranged_scores['CHA'] = scores[3]
            Arranged_scores['DEX'] = scores[2]
            Arranged_scores['WIS'] = scores[1]
            Arranged_scores['INT'] = scores[0]
        case 'Rogue':
            Arranged_scores['STR'] = scores[3]
            Arranged_scores['CON'] = scores[2]
            Arranged_scores['CHA'] = scores[1]
            Arranged_scores['DEX'] = scores[5]
            Arranged_scores['WIS'] = scores[4]
            Arranged_scores['INT'] = scores[0]
        case 'Bard':
            Arranged_scores['STR'] = scores[0]
            Arranged_scores['CON'] = scores[1]
            Arranged_scores['CHA'] = scores[5]
            Arranged_scores['DEX'] = scores[2]
            Arranged_scores['WIS'] = scores[4]
            Arranged_scores['INT'] = scores[3]
        case 'Wizard':
            Arranged_scores['STR'] = scores[1]
            Arranged_scores['CON'] = scores[0]
            Arranged_scores['CHA'] = scores[2]
            Arranged_scores['DEX'] = scores[3]
            Arranged_scores['WIS'] = scores[5]
            Arranged_scores['INT'] = scores[4]

    return Arranged_scores
class Character_Sheet:
    def __init__(self):
        self.gender = genders[random.randint(0,len(genders)-1)]
        self.race = race[random.randint(0,len(race)-1)]
        self.Character_Name = Get_Random_Name(self.race, self.gender)
        self.Character_class = Classes[random.randint(0,len(Classes)-1)]
        self.stats = Get_Stats(self.Character_class)
                                                        
new_character = Character_Sheet()
print(vars(new_character))
