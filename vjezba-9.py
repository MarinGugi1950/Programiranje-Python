import random

broj = random.randint(1,10)

pogodi = int(input("Pogodi broj između 1 i 10: "))

if pogodi == broj:
    print("Bravo pogodio si traženi broj!")
else:
    print("Netočno, traženi broj je bio: " + str(broj))

