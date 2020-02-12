import random

coin = 0
heads1 = 0
tails1 = 0


numFlips = int(input("How many coin flips? "))

for i in range(numFlips):
    coin = random.randint(1,2)
    if (coin == 1):
        heads1 += 1
    else:
        tails1 += 1
print(f"heads: {heads1}, tails:{tails1}")
