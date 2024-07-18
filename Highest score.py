#Highest score program

highest_score = input("Input the scores : ").split()
for n in range(0, len(highest_score)):
    highest_score[n] = int(highest_score[n])
print(highest_score)

max = 0
for score in highest_score:
    if score > max:
        max = score
print("Highest score: ", max)