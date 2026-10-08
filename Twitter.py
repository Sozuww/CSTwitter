import User


class Twitter:
     
    def __init__(self):
        self.users = {}  # lowercase username -> User object
        self.all_tweets = []
        self.current_user = None
        self.next_tweet_id = 1

 # Looks up a user by name. Lowercase so "Kai" and "kai" match.
    # Returns the User, or None if not found.
    def find_user(self, username):
        return self.users.get(username.lower())
 
# Checks a username. Returns an error message, or None if it's fine.
    def validate_username(self, username):
        if username == "":
            return "Username cannot be empty."
        if " " in username:
            return "Username cannot contain spaces."
        if len(username) < 4:
            return "Username must be 4 characters or more."
        if len(username) > 20:
            return "Username must be 20 characters or less."
        if self.find_user(username) is not None:
            return "That username is taken."
        return None  # no problems
 
    # Checks a password. Returns an error message, or None if it's fine.
    def validate_password(self, password):
        if password == "":
            return "Password cannot be empty."
        if len(password) < 4:
            return "Password must be 4 characters or more."
        if len(password) > 20:
            return "Password must be 20 characters or less."
        return None  # no problems

    # Makes a new account if the username and password are valid.
    # Returns (True/False, message to show the user).
    def create_account(self, username, password):
        # Check the username first, then the password
        error = self.validate_username(username)
        if error:
            return False, error

        error = self.validate_password(password)
        if error:
            return False, error

        # Everything is good, so save the user.
        # The lowercase username is the key, which keeps names unique.
        key = username.lower()
        self.users[key] = User(username, key, password)
        return True, "Account created!"
 
    def login(self, username, password):
         pass
 
    def logout(self):
         pass
 
    def is_logged_in(self):
         pass
 
    def parse_hashtags(self, text):
         pass
 
    def post_tweet(self, text):
         pass
 
    def like_tweet(self, tweet):
         pass
 
    def follow(self, username):
         pass
 
    def unfollow(self, username):
         pass
 
    def get_feed(self):
         pass
 
    def get_friend_posts(self, username):
         pass
 
    def search_hashtag(self, tag):
         pass
 
