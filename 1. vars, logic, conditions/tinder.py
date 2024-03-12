
class User:
    def __init__(self, name, gender, age, profession, tv_show, favorite_food):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        self. tv_show = tv_show
        self.favorite_food = favorite_food


def check_if_match(user1, user2):
    if user1.gender != user2.gender and abs(user1.age - user2.age) <= 5 and user1.favorite_food == user2.favorite_food:
        return True
    return False


if __name__ == '__main__':
    user1 = User('user1', 'male', 30, 'chef', 'the office', 'sushi')
    user2 = User('user2', 'male', 31, 'teacher', 'succession', 'shawarma')
    user3 = User('user3', 'female', 32, 'doctor', 'fargo', 'ice cream')
    user4 = User('user4', 'female', 33, 'lawyer', 'dexter', 'shawarma')
    users = [user1, user2, user3, user4]
    match = False

    while match is False:
        print('Enter user attributes: ')
        name = input(print('User name: '))
        gender = input(print('Gender: '))
        while gender != 'male' and gender != 'female':
            gender = input(print('Gender:'))
        age = int(input(print('Age: ')))
        profession = input(print('Profession: '))
        tv_show = input(print('Favorite tv show: '))
        favorite_food = input(print('Favorite food: '))
        input_user = User(name, gender, age, profession, tv_show, favorite_food)
        matches = []
        for user in users:
            if check_if_match(user, input_user):
                matches.append(user)
                match = True
    print('Matching users: ')
    for user in matches:
        print(user.name)

