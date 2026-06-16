import time

sentence = "Python is really fun to learn"

print("Type this sentence:")
print(sentence)

start = time.time()

typed = input()

end = time.time()

if typed == sentence:
    print("Correct!")
else:
    print("There were mistakes.")

print("Time taken:", round(end - start, 2), "seconds")
