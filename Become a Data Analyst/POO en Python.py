#
#POO en Python

##Tuples

    book1 = ("1984", "Available", "George Orwell")
    book2 = ("The Hobbit", "Checked Out", "J.R.R. Tolkien")

    library = [book1, book2]

    for book in library:
        print("Title:", book[0], "| Status:", book[1], "| Author:", book[2])
    
    Output
    Title: 1984 | Status: Available | Author: George Orwell
    Title: The Hobbit | Status: Checked Out | Author: J.R.R. Tolkien
    
    
    ##Ejemplo
        def borrow_book_tuple(library, title):
        # Loop through the library (list of books), with `i` as the index and `book` as the tuple containing book details
        for i, book in enumerate(library):
            # Check if the title of the current book matches the requested title
            if book[0] == title:
                # If the book is found, check if it is available (book[1] represents the status)
                if book[1] == "Available":
                    # If the book is available, update its status to "Checked Out"
                    # A new tuple is created, as tuples are immutable
                    library[i] = (book[0], "Checked Out", book[2], book[3])
                    print(title, "borrowed successfully.")  # Print confirmation message
                else:
                    # If the book is already checked out (not available), print that it's already borrowed
                    print(title, "already borrowed.")
                return  # Exit the function once the book has been found and processed
        # If the book with the given title is not found in the library, print a message
        print(title, "not found in library.")
        
    ##Tuples are immutable in Python. This means that once a tuple is created, its elements cannot be changed or modified in place.
    ##In the borrow_book_tuple() function, we try to modify the second element of a tuple (the status of the book) from "Available" to "Checked Out", but we can’t directly modify an individual element of a tuple. This is a limitation of tuples.
    
    
##CLASS

    class Book:
        def __init__(self, title, status="Available"):
            self.title = title
            self.status = status
                
        ##__init__ method: This is a special method in Python known as the initializer or constructor. It is automatically called when a new instance of the class is created, and its main role is to set up the new object's initial state by assigning values to its attributes.
        ##self parameter: The parameter self represents the instance of the class that is being created or manipulated. It allows the method to access or modify attributes and call other methods on that specific object.
        ##Dot notation (self.title): The dot after self is used to access attributes or methods of the object. For example, self.title = title assigns the value of title to the attribute title of the current object.
            
        def display(self):
            print(self.title + " - " +  self.status)        
        
        ##Inside the method, self.title and self.status refer to the title and status attributes of the specific Book instance
        
        def borrow(self):
            if self.status == "Available":
                self.status = "Checked Out"
                print(self.title + " has been borrowed.")
            else:
                print(self.title + " is already checked out.")
        
        ##The method borrow(self) checks if the book is available. If so, it updates the status. If the book is already borrowed, it notifies the user.
        
    # Creating book objects
    book1 = Book("1984")
    book2 = Book("The Hobbit", "Checked Out")
    book3 = Book("Dune")  # Adding a new book
    
    ##Here, book1, book2, and book3 are objects (instances) of the Book class, each representing a different book.
    
    # Displaying the books
    book1.display()
    book2.display()
    book3.display()        
    
    ##This will output the title and status of each book.
    
    # Borrowing a book
    book3.borrow()
    book3.display()

    ##After borrowing, the status of "Dune" changes to "Checked Out". In OOP, this process is straightforward and error-free because the book3 object handles its own data.
    
    ###Procedural programming is like managing your library with sticky notes—prone to errors, disorganized, and hard to maintain. OOP gives you a proper system where each book knows its details and can handle its own behavior, making your code clean, organized, and scalable.
    
##class attribute

    # Se pueden clasificar en atributos de instancia, que son únicos para cada objeto, 
    # y atributos de clase (o estáticos), que son compartidos por todas las instancias de la clase. 
    # Un ejemplo común es usar atributos de clase para contar cuántos objetos de la clase se han creado. 
    
    class Book:
        total_books = 0 # Class attribute
        
        def __init__(self, title, status="Available"):
            self.title = title
            self.status = status
            Books.total_books += 1 # Adds total books to the Book class
            
##Class Methods
     
    # Is a method that is bound to the class itself, rather than to an instance of the class. 
    # This means it can be called on the class directly, without needing to create an object of that class first. 
     
    class A(object):
        
        @classmethod
        def function(cls, argument1, argument2, ...):
            # method logic here        
    
    ################
    
    class User:
        total_users = 0  # Class attribute to track number of users

        @classmethod
        def create_guest_user(cls):
            # Generates a guest user with a random username
            guest = cls(username="guest_123", display_name="Guest")
            return guest
            
##Static Methods

    # Is a method that belongs to a class but doesn't operate on an instance or the class itself. 
    # You define a static method using the @staticmethod decorator. 
    # Static methods don't receive an implicit self or cls argument.
    
    class C(object):
        @staticmethod
        def function(argument1, argument2, ...):

    #################
    
    class Post:  
        MAX_CONTENT_LENGTH = 280  

        @staticmethod  
        def validate_content_length(content):  
            # Checks if a post meets the platform's character limit  
            return len(content) <= Post.MAX_CONTENT_LENGTH  

##Encapsulation

    # This is the principle of bundling data and the methods that operate on that data into a single unit (the object). 
    # In our project, we want each object (such as a User or a Post) to manage its own data.
     


##Private Attributes

    # OOP emphasizes that, from the user’s perspective, only the external behavior of an object matters,
    # not its internal implementation details, such as data structures or algorithms. 
    # Making data members private helps enforce this abstraction.
    
    class User:
        
        def __init__(self, username, password):
            self.username = username
            self._password = password  # Correct: using a leading underscore to indicate privacy
            
        def check_password(self, input_password):
            return input_password == self._password
    
    # Attempt to print the password (should not be done in practice)
    print("Accessing password via convention (not recommended):", user1._password)
    
    # Using the provided methods to interact with the private password:
    print("Checking password 'secret123':", user1.check_password("secret123")) 
    
##Getters and Setters

    class Student:
        def __init__(self):
            # Private attribute
            self._rollNo = None

        # Setter
        def set_roll_no(self, roll_no):
            self._rollNo = roll_no

        # Getter
        def get_roll_no(self):
            return self._rollNo
            
##Inheritance 

    # Inheritance is an object-oriented programming principle where a new class (the subclass)
    # is derived from an existing class (the parent or base class).
    # The subclass automatically inherits all the attributes and methods of the parent 
    # but can also introduce new ones or modify existing behaviors.

    # It is “IS A” relationship between two classes as:

    # Car IS A Vehicle.
    # Python IS A Programming Language.
    # Circle IS A Shape.

#super() function
    
    # The use of super() comes into play when we implement inheritance. It is used in a child class to refer to the parent class without explicitly naming it. It makes the code more manageable, and there is no need to know the name of the parent class to access its attributes.
    # In the VerifiedUser class, line 4 is a super function that calls the __init__ method of the parent (User) class inherits all the attributes from it (User).

    class User:
        def __init__(self, username, display_name, password):
            self.username = username
            self._display_name = display_name  
            self._password = password 
        
    class VerifiedUser(User):
        def __init__(self, username, display_name, password):
            # Inherit all attributes from User
            super().__init__(username, display_name, password)
            # Add a new attribute specific to verified users
            self.verification_badge = True

        # New method to return verification status
        def get_verification_status(self):
            return "Verified ✅" if self.verification_badge else "Regular"
            
##Method Overriding
    
    # allows a subclass to provide its own implementation for a method already defined in its parent class. 
    # In other words, it is the process of redefining a parent class’s method in a subclass.

#Polymorphism
    # Refers to the same object exhibiting different forms and behaviors.
    # For example, take the Shape class. The exact shape you choose can be anything. 
    # It can be a rectangle, a circle, or a hexagon. While these are all shapes, 
    # their properties are different. This is called polymorphism.
 
 
    #post.py
    from comment import Comment  

    class Post:
        total_posts = 0

        def __init__(self, content, author):
            self._content = content   # Store content privately
            self.author = author    
            self.comments = [ ]   

        def add_comment(self, text, commenter):
            comment = Comment(text, commenter)
            self.comments.append(comment)
            print(comment.commenter.display_name, "added a comment on", self.author.display_name + "'s post.")
            return comment
        
    #user.py
    from post import Post  
    import random

    class User:

        def __init__(self, username, display_name, password):
            self.username = username
            self._display_name = display_name  # Store display_name privately for controlled access
            self._password = password         
            self.posts = [ ]

        def create_post(self, content):
            post = Post(content, self)
            self.posts.append(post)
            return post

            
    #verified_user.py
    from user import User

    class VerifiedUser(User):
        def __init__(self, username, display_name, password):
            # Inherit all attributes from User
            super().__init__(username, display_name, password)
            # Add a new attribute specific to verified users
            self.verification_badge = True

        # New method to return verification status
        def get_verification_status(self):
            return "Verified ✅" if self.verification_badge else "Regular"
            
        # Overriding create_post() to add a "✅ " prefix to the content
        def create_post(self, content):
            # Add a special flair to posts created by verified users
            verified_content = "✅ "   + content
            post = Post(verified_content, self)
            self.posts.append(post)
            return post
            
    #main.py            
    from user import User
    from verified_user import VerifiedUser
    from social_network import SocialNetwork

    # Create a SocialNetwork instance
    chirpy_network = SocialNetwork()

    # Create a regular user and a verified user
    user1 = User("alex123", "Alex", "secret123")
    v_user = VerifiedUser("verified123", "VerifiedAlex", "secret456")

    # Add both users to the network
    chirpy_network.add_user(user1)
    chirpy_network.add_user(v_user)

    # Regular user creates a post
    post1 = user1.create_post("Hello world! This is my first chirp.")
    chirpy_network.add_post(post1)

    # Verified user creates a post with special flair
    post2 = v_user.create_post("I am here to share my thoughts!")
    chirpy_network.add_post(post2)

    # List all posts; note how posts from different user types appear differently.
    print("\nChirpy Posts:")
    chirpy_network.list_all_posts()            
    
    
##__str__ Vs. __repr__

    # In Python, the __str__ method is used to provide a readable, user-friendly string representation of an object. 
    # When you call print() on an object, Python uses the __str__ method if it’s defined. 
    
    # In contrast, __repr__ is intended for developers: it returns an unambiguous string representation that, ideally, 
    # could be used to recreate the object.

    # The __str__ and __repr__ methods are part of a special category in Python called dunder (double underscore) methods, also known as magic methods. These methods allow objects to interact with built-in Python behavior, such as printing, addition, comparison, and more.
    # Dunder methods are named with double underscores before and after (e.g., __init__, __len__, __add__), and they define how objects should behave in certain situations.
    # For example:
    # __init__: Defines how an object is initialized.
    # __len__: Returns the length of an object (used with len() function).
    # __add__: Allows objects to use the + operator.
    
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return "Point at ({}, {})".format(self.x, self.y)

        def __repr__(self):
            return "Point({}, {})".format(self.x, self.y)
            
    p = Point(3, 4)    
    
    ------------------------
    Output
    Point at (3, 4)
    Point(3, 4)
    
    ## Code explanation

    # The above example defines a Point class representing a 2D point with coordinates x and y. 
    # The __init__ method initializes the point with the given values. 
    # The __str__ method uses the .format() function to return a user-friendly string, such as "Point at (3, 4)", when the object is printed. 
    # Similarly, __repr__ returns a debugging-friendly string, such as "Point(3, 4)".
    
    # The .format() function replaces the {} placeholders with the values of self.x and self.y, making it easy to compose strings dynamically and readably.
    
    print(p)
    # When we create a point and call print(p), it outputs the result of __str__, 
    
    print(repr(p))
    # while print(repr(p)) outputs the result of __repr__.

    # The __str__ method is meant for end users, offering a clear and friendly representation of the object.
    # Python falls back to using the __repr__ method if __str__ is not defined.
    # This unambiguous output is especially useful during debugging or when logging objects.
    
