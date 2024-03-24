class User:
    # initialize user with user name and an empty list of the people he follows
    def __init__(self, username):
        self.username = username
        self.following = {}

    # follow the given user and add it to the following list, if not already following
    def follow(self, other_user):
        # the time complexity for this function is O(x) when x is the len of the list of following for the given user,
        # because each time the function is called, it goes over the list of following first to check if the
        # 'other_user' is already in the following list
        # the new time complexity is O(1) because now it takes O(1) to check if 'other_user' is already in the
        # following list because now the list is a dict.
        if other_user not in self.following.keys():
            self.following[other_user] = True

    # adds to the global list of posts a new post by the user with the given message
    def post_message(self, message):
        # the time complexity of this function is O(len(message)) because it copies the given message to a dictionary
        # before appending it to the posts list
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list
posts = []

