class User:
    def __init__(self, user_id, user_name):
        """create the starting value for an attribute
        this is called everytime a new object is created"""
        """ Attributes are what an object has. It is a variables associated to an object"""
        """ User_id and user_name are stating values of attributes id and username"""
        # create attributes in the function:
        self.id = user_id
        self.username = user_name
        #setting default value to an attribute
        self.follower = 0
        self.following = 0


        # Create method in the Class
        """ Method is what object does"""
    def follow(self, user):
        user.follower += 1
        self.following += 1

# user_1 = User()
# user_1.id = "012"
# user_1.username = "fiona"

# print(user_1)

# user_2 = User()


user_1 = User("012", "Fiona")

user_2 = User("013", "Kris")

user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)

