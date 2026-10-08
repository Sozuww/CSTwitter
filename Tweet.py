class Tweet:
    def __init__(self, tweet_id, author, text, hashtags=None, timestamps=None):
        self.tweet_id = tweet_id
        self.author = author
        self.text = text
        self.hashtags = hashtags
        self.timestamps = timestamps

    def add_like(self, user_key):
        pass

    def get_like_count(self):
        pass

    def has_hashtag(self, tag):
        pass

    if __name__ == "__main__":
        pass


    
