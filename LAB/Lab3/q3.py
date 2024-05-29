# Write a program that generates a quiz and uses two files- Questions.txt and Answers.txt. The program opens
# Questions.txt, reads a question, and displays the question with options on the screen. The program then opens the Answers.txt file and displays the correct answers.


question = open("LAB/Lab3/Questions.txt", "r")
answer = open("LAB/Lab3/Answers.txt", "r")

# Display the question and user should enter the answer and it should check with the answer in the file

for line in question:
    print(line)
    ans = input("Enter the answer: ")
    ans=ans+"\n"
    a=answer.readline()
    if ans == a:
        print("Correct answer")
    else:
        print("Wrong answer")






