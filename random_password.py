import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "0123456789"
symbol = "@#$%&()[]{};.-_~"

all= lower + upper + number + symbol
length = 9
password = "".join(random.sample(all,length))
print(" The Password you generated is :",password)