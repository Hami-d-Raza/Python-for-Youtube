import time as t
import matplotlib.pyplot as plt
time = []
mistakes = 0

print("This program helps you type faster. You will have to type the word 'programming' as fast as you can for five times.")
input("Press enter to continue.")

while len(time) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    time.append(time_elapsed)

    if word.lower() != "programming":
        mistakes += 1

print("You made", mistakes, "mistake(s).")
print("Now let's see your evolution.")
t.sleep(3)

x = [1, 2, 3, 4, 5]
y = time
plt.scatter(x, y)
plt.xlabel("Attempts")
plt.ylabel("Time in seconds")
plt.title("Your typing evolution")
plt.show()


print("Thanks for watching")