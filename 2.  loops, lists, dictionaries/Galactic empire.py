from random import randint


class AlienDelegation:
    def __init__(self, name, suggestions, wanted_demands):
        self.name = name
        self.suggestions = suggestions
        self.wanted_demands = wanted_demands

### why add this line?
if __name__ == '__main__':
    materials = [i for i in range(21)] ### good for placeholder, where are the materials?
    ### DRY
    AD1 = AlienDelegation("AD1", 1, [14, 4])
    AD2 = AlienDelegation("AD2", 11, [1])
    AD3 = AlienDelegation("AD3", 2, [15,3,4])
    AD4 = AlienDelegation("AD4", 7, [2,3,4,5,6,7,8])
    ### what if it was 500 delegations?
    AD = [AD1, AD2, AD3, AD4]
    convinced_aliens = []
    for ad in AD: ### is this name clear? what is ad? what is AD? think you read it after a month.
        accepted = False
        while not accepted and ad.suggestions > 0:
            given_material = randint(1, 21)
            print("Suggested material for " + ad.name + " is: " + str(given_material) + ".")
            if given_material in ad.wanted_demands:
                convinced_aliens.append(ad)
                print(ad.name + " accepted the suggestion.")
                accepted = True
            else:
                print(ad.name + " rejected the suggestion.")

            ad.suggestions -= 1
    acceptance_percentage = len(convinced_aliens) / 4 * 100
    print(str(acceptance_percentage) + "% alien delegations were convinced.")
    if acceptance_percentage < 70:
        print("Fail.")
    else:
        print("Success!")
