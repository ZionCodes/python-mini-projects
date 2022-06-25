print("Hello, Welcone to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does GMT stand for? ").lower()
if answer == "greenwich mean time":
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input("What does UTC stand for? ").lower()
if answer == "coordinated universal time":
    print('correct!')
    score +=1
else:
    print('incorrect!')

answer = input("What does EST stand for? ").lower()
if answer == "eastern standard time":
    print('correct!')
    score += 1
else:
    print('incorrect!')

print('You have come to the end of this quiz! your score is '+ str(score) + ' questions correct')

