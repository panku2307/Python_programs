import random
flip = int(input("No. of  flips "))
head=0
tail=0
for i in range(flip):
    number = random.random()
    if number > 0.5:
        head = head + 1

    if number < 0.5:
        tail = tail + 1

perc_head = head/flip
perc_tail = tail/flip

print(f"total no. of head is {perc_head} and total number of tail is {perc_tail}")