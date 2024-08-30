def requiredFormat(answer):
    punctuations = ['.', '-', ',', ' ', '\'']
    for punctuation in punctuations:
        answer = answer.replace(punctuation, '')
    return answer.lower()


print("WELCOME TO MY SUPER QUIZ")

while True:
    start = input("Do you want to play? (Y/N): ")
    if requiredFormat(start) == "n" or requiredFormat(start) == "no":
        print("Goodbye then! You will be missing the GREATEST QUIZ!!!")
        quit()
    elif requiredFormat(start) == "y" or requiredFormat(start) == "yes":
        print("Okay! Let's Play!!!")
        break
    else:
        print("Kindly input the correct option.")

score = 0

quiz = {"What is full name of USA? "                 : "unitedstatesofamerica",
        "How many bits does a byte have? "           : "8",
        "What is the capital of Pakistan? "          : "islamabad",
        "Apple falls down due to? "                  : "gravity",
        "What's the national animal of Australia? "  : "kangaroo"}

for ques, ans in quiz.items():
    userAnswer = input(f'{ques}')
    if requiredFormat(userAnswer) == ans:
        print('Correct Answer!!\nYou get one point!!!')
        score = score + 1
    else:
        print('Wrong Answer! No Point :(')

print(f'Yahoo! You completed the quiz.\nYour final score is {score}/5')
