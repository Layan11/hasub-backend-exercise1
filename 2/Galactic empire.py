from random import randint


class AlienDelegation:
    def __init__(self, name, materials, suggestions, wanted_demands):
        self.name = name
        self.materials = materials
        self.suggestions = suggestions
        self.wanted_demands = wanted_demands


if __name__ == '__main__':
    materials = [i for i in range(21)]
    AD1 = AlienDelegation("AD1", [1, 2, 3], 1, [14, 4])
    AD2 = AlienDelegation("AD2", [4, 5], 11, [1])
    AD3 = AlienDelegation("AD3", [5, 2, 8], 2, [15,3,4])
    AD4 = AlienDelegation("AD4", [1, 11], 7, [2,3,4,5,6,7,8])
    AD = [AD1, AD2, AD3, AD4]
    convinced_aliens = []
    for ad in AD:
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
