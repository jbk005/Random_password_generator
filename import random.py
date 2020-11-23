import random
import string
j = int(input("length of the password: ")) #length of password
#this will join alpha+num in both upper and lowercases  in the range of j or lenght of password
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(j))
#finally printing x as output " no limit for length"
print(x)