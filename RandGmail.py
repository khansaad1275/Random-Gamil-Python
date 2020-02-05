import random
import string

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

gmail =  (randomString() + str(random.randint(1000,10000)) + "@gmail.com" )
print(gmail)
