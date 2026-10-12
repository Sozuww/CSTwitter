from Twitter import Twitter


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

    # Shows the main menu for as long as someone is logged in.
    # Logging out ends this loop, which sends you back to the start menu.
    def show_main_menu(self):
        while self.twitter.is_logged_in():
            print("\n--- Main Menu ---")
            print("1. Post a tweet")
            print("2. View feed")
            print("3. Follow someone")
            print("4. Unfollow someone")
            print("5. See a friend's posts")
            print("6. Search for a user")
            print("7. Search a hashtag")
            print("8. Log out")
            choice = input("Choose an option: ")

            if choice == "1":
                self.handle_post_tweet()
            elif choice == "2":
                self.handle_view_feed()
            elif choice == "3":
                self.handle_follow()
            elif choice == "4":
                self.handle_unfollow()
            elif choice == "5":
                self.handle_friends_posts()
            elif choice == "6":
                self.handle_search_user()
            elif choice == "7":
                self.handle_search_hashtag()
            elif choice == "8":
                self.handle_logout()
            else:
                print("Please enter a number from 1 to 8.")

    # Asks for a username and password, then tries to make the account
    def handle_create_account(self):
        username = input("Username: ")
        password = input("Password: ")

        # create_account gives back (worked or not, message to show)
        success, message = self.twitter.create_account(username, password)
        print(message)
        # We just return, so the start menu shows again

    # Asks for a username and password, then tries to log in.
    # If it works, the user goes to the main menu.
    def handle_login(self):
        username = input("Username: ")
        password = input("Password: ")

        if self.twitter.login(username, password):
            # Use the saved name so "kai" still shows as "Kai"
            print(f"Welcome back, {self.twitter.current_user.username}!")
            self.show_main_menu()
        else:
            print("Invalid username or password.")

    # Logs the user out. The main menu loop then stops,
    # so the user lands back on the start menu.
    def handle_logout(self):
        self.twitter.logout()
        print("You have been logged out.")

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


# Starts the program when you run this file
if __name__ == "__main__":
    app = ConsoleApp()
    app.show_start_menu()