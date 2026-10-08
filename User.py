class User:
    def __init__(self, username, key, password):
        self.username = username   # display name, keeps the original capitalization
        self.key = key             # lowercase username, used as the unique ID
        self.password = password

    def check_password(self, password):
        pass

    def is_following(self, user_key):
        pass

    def tweets_newest_first(self):
        pass

    def get_follower_count(self):
        pass

    def get_following_count(self):
        pass