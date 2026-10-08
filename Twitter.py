class Twitter:
     
    def __init__(self):
         self.users = {}
         self.all_tweets = []
         self.current_user = None
         self.next_tweet_id = 1
 
    def find_user(self, username):
         return self.users.get(username)
 
    def validate_username(self, username):
         pass
 
    def validate_password(self, password):
         pass
 
    def create_account(self, username, password):
         pass
 
    def login(self, username, password):
     user = self.find_user(username)
     if user is None:
          return False
     if not user.check_password(password):
          return False
     self.current_user = user
     return True

    def logout(self):
          self.current_user = None
 
    def is_logged_in(self):
         return self.current_user is not None
 
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
 
