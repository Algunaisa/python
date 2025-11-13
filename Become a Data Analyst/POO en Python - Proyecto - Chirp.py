##Proyecto: Chirp

#social_network.py
class SocialNetwork:
    def __init__(self):
        self._users = [ ]   # Private list to store User objects
        self._posts = [ ]   # Private list to store Post objects

    def add_user(self, user):
        if self.search_user_by_username(user.username):
            print("\nUser with username", user.username, "already exists!\n")
        else:
            self._users.append(user)
            print(user.display_name, "has been added to Chirpy.")

    def add_post(self, post):
        self._posts.append(post)

    def search_user_by_username(self, username):
        for user in self._users:
            if user.username == username:
                return user
        return None

    def remove_user(self, username):
        user_to_remove = self.search_user_by_username(username)
        if user_to_remove:
            self._users.remove(user_to_remove)
            print("\n", user_to_remove.display_name, "has been removed from Chirpy.")
        else:
            print("\nUser with username", username, "not found!")

    def list_all_posts(self):
        if not self._posts:
            print("\nNo posts to display.")
        else:
            for post in self._posts:
                print(post.author.display_name + " posted: '" + post.content + "'")

#verified_user.py
from user import User
from post import Post

class VerifiedUser(User):
    def __init__(self, username, display_name, password):
        # Inherit attributes from User
        super().__init__(username, display_name, password)
        # Mark the user as verified
        self.verification_badge = True

    def get_verification_status(self):
        return "Verified ✅" if self.verification_badge else "Regular"

    # Overriding create_post() to add a "✅ " prefix to the content
    def create_post(self, content):
        # Add a special flair to posts created by verified users
        verified_content = "✅  "+  content
        post = Post(verified_content, self)
        self._posts.append(post)
        return post
        
#user.py
from post import Post  
import random

class User:
    total_users = 0  

    def __init__(self, username, display_name, password):
        self._username = username                    # Private attribute
        self._display_name = display_name            # Private attribute with controlled access
        self._password = password                    # Private attribute for security and abstraction
        self._posts = [ ]                             # Private attribute
        User.total_users += 1

    # Getter for username (read-only property)
    @property
    def username(self):
        return self._username

    # Getter for display_name
    @property
    def display_name(self):
        return self._display_name

    # Setter for display_name
    @display_name.setter
    def display_name(self, value):
        if not value:
            raise ValueError("Display name cannot be empty.")
        if len(value) > 20:
            raise ValueError("Display name cannot be longer than 20 characters.")
        self._display_name = value

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")

    def create_post(self, content):
        post = Post(content, self)
        self._posts.append(post)
        return post

    def like_post(self, post):
        post.like_post(self)

    @classmethod
    def create_guest_user(cls):
        random_number = random.randint(100, 999)
        username = "guest" + str(random_number)
        display_name = "Guest"  
        return cls(username, display_name, "guestpass")

    def change_password(self, new_password):
        if len(new_password) >= 6:
            self._password = new_password
            print("Password updated successfully!")
        else:
            print("Error: Password must be at least 6 characters long.")

    def check_password(self, input_password):
        return input_password == self._password
    
    # User-friendly representation of the User object
    def __str__(self):
        return "<User: %s (%s)>" % (self.display_name, self.username)
        
#comment.py
class Comment:
    def __init__(self, text, commenter):
        self._text = text              # The text content of the comment (private)
        self._commenter = commenter    # The User who made the comment (private)

    def display_comment(self):
        # Accessing the private attributes internally within the class
        print(self._commenter.display_name + " commented: '" + self._text + "'")

#post.py
from comment import Comment  

class Post:
    total_posts = 0

    def __init__(self, content, author):
        self._content = content                  # Private attribute to store content
        self._author = author                    # Private attribute to store author
        self._likes = [ ]                         # Private attribute to store likes
        self._like_count = 0                     # Private attribute for counting likes
        self._comments = [ ]                      # Private attribute to store comments
        Post.total_posts += 1

    # Getter for content
    @property
    def content(self):
        return self._content

    # Setter for content with validation
    @content.setter
    def content(self, new_content):
        if len(new_content) > 280:
            raise ValueError("Chirp content cannot exceed 280 characters.")
        self._content = new_content

    # Getter for author (read-only)
    @property
    def author(self):
        return self._author

    # Method to handle liking a post
    def like_post(self, user):
        if user not in self._likes:
            self._likes.append(user)
            self._like_count += 1
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")

    # Getter for like count
    def get_like_count(self):
        return self._like_count

    # Method to add a comment
    def add_comment(self, text, commenter):
        comment = Comment(text, commenter)
        self._comments.append(comment)
        print(comment.commenter.display_name, "added a comment on", self.author.display_name + "'s post.")
        return comment

    # Getter for comments
    @property
    def comments(self):
        return self._comments.copy()  # returns a copy to maintain encapsulation

    # Static method to validate content length without needing an instance
    @staticmethod
    def validate_content_length(content):
        return len(content) <= 280

    # Debugging-friendly representation of a Post object
    def __repr__(self):
        snippet = self._content if len(self._content) <= 30 else self._content[:27] + "..."
        return "<Post by %s: '%s', Likes: %d>" % (self._author.username, snippet, self._like_count)
        
#main.py
from social_network import SocialNetwork
from user import User
from verified_user import VerifiedUser

# Initialize the Chirpy Social Network
_chirpy_network = SocialNetwork()

def display_menu():
    print("\n Chirpy Social Media Platform")
    print("========================================")
    print("1. Create New Account")
    print("2. Post a Chirp")
    print("3. View All Chirps")
    print("4. Like a Chirp")
    print("5. Comment on a Chirp")
    print("6. View Profile")
    print("7. List All Users")
    print("8. Exit")

def create_account():
    username = input("Enter username: ")
    display_name = input("Enter display name: ")
    password = input("Enter password: ")
    verified = input("Do you want a verified account? (yes/no): ").strip().lower()
    if verified == "yes":
        user = VerifiedUser(username, display_name, password)
    else:
        user = User(username, display_name, password)
    _chirpy_network.add_user(user, verified)
    print(f"Account created successfully for {display_name}!")

def post_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        content = input("Enter your chirp: ")
        post = user.create_post(content)
        _chirpy_network.add_post(post)
    else:
        print("User not found.")

def view_chirps():
    _chirpy_network.list_all_posts()

def like_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to like: "))
            if 0 <= post_index < len(_chirpy_network._posts):
                user.like_post(_chirpy_network._posts[post_index])
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")

def comment_on_chirp():
    username = input("Enter your username: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        _chirpy_network.list_all_posts()
        try:
            post_index = int(input("Enter post index to comment on: "))
            if 0 <= post_index < len(_chirpy_network._posts):
                comment = input("Enter your comment: ")
                _chirpy_network._posts[post_index].add_comment(comment, user)
            else:
                print("Invalid post index.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("User not found.")

def view_profile():
    username = input("Enter username to view profile: ")
    user = _chirpy_network.search_user_by_username(username)
    if user:
        user.show_profile()
    else:
        print("User not found.")

def list_users():
    if _chirpy_network._users:
        print("\nRegistered Users:")
        for user in _chirpy_network._users:
            print(user)
    else:
        print("No users registered yet.")

while True:
    display_menu()
    choice = input("Choose an option (1-8): ")
    
    if choice == "1":
        create_account()
    elif choice == "2":
        post_chirp()
    elif choice == "3":
        view_chirps()
    elif choice == "4":
        like_chirp()
    elif choice == "5":
        comment_on_chirp()
    elif choice == "6":
        view_profile()
    elif choice == "7":
        list_users()
    elif choice == "8":
        print("Exiting Chirpy. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")