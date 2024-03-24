import scalability.improve_social_app.after_optimization.user as usr


class SocialMediaPlatform:
    def __init__(self):  # initializes the list of users in the platform
        # self.users = []
        self.users = {}

    # adds a new user to the list, if the username is not already taken by someone else
    def register_user(self, username):
        # the time complexity for this function is O(number of users) because everytime we want to add a user to the
        # platform the function goes over all the existing users to check if the given username is already in use.
        # the new time complexity after optimizing is O(1) because it takes O(1) to check a key in a dictionary, and
        # now the users list is a dictionary.

        if username not in self.users.keys():
            user = usr.User(username)
            self.users[username] = user

    # checks if someone in the user list has the name 'username' if so return true otherwise return false
    def _is_username_taken(self, username):
        for name in self.users.keys():
            if name == username:
                return True
        return False

    # looks for the user with the the given username in the user list and if found return that user,
    # otherwise return None
    def get_user_by_username(self, username):
        for name in self.users.keys():
            if name == username:
                return self.users[name]
        return None

    # generates the timeline for the given user by going over the posts list and appending the ones who the given user
    # follows and then returns the timeline of generated posts
    def generate_timeline(self, username):
        # the time complexity of this function is O(x + y*b) when x is the length of the users list and y is the length
        # of the following list and b is the number of posts for each person.
        # the new time complexity after optimization is O(y*b) because now it only takes O(1) to get the user from the
        # users list because it is now a dictionary.
        user = self.users[username]
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in usr.posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline
