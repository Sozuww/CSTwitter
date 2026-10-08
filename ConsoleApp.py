import Twitter

class ConsoleApp:
    def __init__(self):
       self.twitter = Twitter()
       self.running = True

# Shows the start menu over and over until the user quits
    def show_start_menu(self):
        while self.running:
            print("\n--- Start Menu ---")
            print("1. Create account")
            print("2. Login")
            print("3. Quit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.handle_create_account()
            elif choice == "2":
                self.handle_login()
            elif choice == "3":
                self.running = False  # stops the loop
            else:
                print("Please enter 1, 2, or 3.")
 
    def show_main_menu(self):
       pass
 
# Asks for a username and password, then tries to make the account
    def handle_create_account(self):
        username = input("Username: ")
        password = input("Password: ")

        # create_account gives back (worked or not, message to show)
        success, message = self.twitter.create_account(username, password)
        print(message)
        # We just return, so the start menu shows again
 
    def handle_login(self):
       pass
 
    def handle_logout(self):
       pass
 
    def handle_post_tweet(self):
       pass
 
    def handle_follow(self):
       pass
 
    def handle_unfollow(self):
       pass
 
    def handle_view_feed(self):
       pass
 
    def handle_friends_posts(self):
       pass
 
    def handle_search_user(self):
       pass
 
    def handle_search_hashtag(self):
       pass
 
    def display_tweets(self, tweets):
       pass
   
    def prompt_like(self, tweets):
       pass
