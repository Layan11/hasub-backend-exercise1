import match
from unittest import case

# def temp_converter(from , to):

if __name__ == '__main__':
    conversion_type = '0'
    while conversion_type not in ['1. vars, logic, conditions', '2.  loops, lists, dictionaries', '3', '4', '5', '6', '7', '8', '9', '10']:
        conversion_type = str(input(print("Please choose json_funcs conversion type, 1. vars, logic, conditions: F->C, 2.  loops, lists, dictionaries: C->F, 3: MPH->KPH, 4:KPH->MPH,"
                                  "5: KG->stone, 6: stone->KG, 7: stone->lbs,8: lbs->stone,9: KG->lbs, 10: lbs->KG")))
    source_val = int(input(print("Please write the source value: ")))

    if conversion_type == '1. vars, logic, conditions':
        converted = (source_val - 32) * 5 / 9
    elif conversion_type == '2.  loops, lists, dictionaries':
        converted = (source_val * 9 / 5) + 32
    elif conversion_type == '3':
        converted = source_val * 1.609
    elif conversion_type == '4':
        converted = source_val / 1.609
    elif conversion_type == '5':
        converted = source_val / 6.35
    elif conversion_type == '6':
        converted = source_val * 6.35
    elif conversion_type == '7':
        converted = source_val * 14
    elif conversion_type == '8':
        converted = source_val / 14
    elif conversion_type == '9':
        converted = source_val * 2.205
    elif conversion_type == '10':
        converted = source_val / 2.205
    else:
        print("invalid input")
    print("The converted result is: " + str(converted))



