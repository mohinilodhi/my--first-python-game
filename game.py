# Simple KBC Game in Python

print("🎉 Welcome to Kaun Banega Crorepati 🎉".upper())
print("You will be asked 3 questions. Let's begin!\n")

print("ques1= which language used for artifical intelligent?")
print("ques2= who is known as the father of computer?")

options = ["HTML","CSS","java","python"]
correct_answer = "python"

user = input("enter your answer  [HTML,CSS,java,python]:  ")

if user == correct_answer:
    print("you win")
    print("congratulation")
else:
    print("you lost")

print("thankyou so much for checking out my project . I hope you will like it.")