class User:
    def __init__(self, username, key, password):
        self.username = username   # display name, keeps the original capitalization
        self.key = key             # lowercase username, used as the unique ID
        self.password = password

        # This data lives on the User, NOT on the login session.
        # So logging out and back in gives you the same tweets and follows.
        self.tweets = []           # this user's Tweet objects
        self.following = set()     # keys of users this user follows
        self.followers = set()     # keys of users who follow this user

    # True if the password matches this user's password
    def check_password(self, password):
        return self.password == password

    def is_following(self, user_key):
        pass

    def tweets_newest_first(self):
        pass

    def get_follower_count(self):
        pass

    def get_following_count(self):
        pass