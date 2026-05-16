#DAY = 1
print("======= 📱 DIGITAL CALCULATOR 📱=======")

num1 = int(input("enter your num1: "))
num2 = int(input("enter your num2: "))

option = input("Enter your (+,-,*,/): ")

if option == "+":
    print("Result =", num1 + num2)
elif option == "-":
    print("Result =", num1 - num2)
elif option == "*":
    print("Result =", num1 * num2)
elif option == "/":
    if num2 != 0:
     print("Result =", num1 / num2)
    else:
        print("cannot divide by Zero")
else:
    print("Invalid operation")

print("Thankyou")





#DAY = 2
print("========🧮🧮TABLE GENRATOR🧮🧮=======")

start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))

for n in range(start_num,end_num+1):
  
  print("\nTable of",n)
  
  for i in range(1,11):
       
       print(n, "x", n, "=", n*i)




#DAY = 3

print("🔢🔢....MINI NUMBER ANALAYZER....🔢🔢")

try:
    num = int(input("enter your number🔢: "))
    print(num)
    
    if num%2 == 0:
        print("Even 👊")
    else:
        print("Odd")
     
    if num > 1:
        print("positive")
    else:
        print("negeative")

    if num == 0:
        print("this number is zero")
    else:
        print("this is number")

    if num%5 == 0:
        print("this is divisible by 5")
    else:
        print("this is not divisible by 5")

except ValueError:
    print("enter valid input")

finally:
    print("thank you!!!🎉🎉")



#day = 4
print("~~~~~ 1️⃣ LARGEST OF 3 NUMBER FINDER 3️⃣~~~~~~~")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2

else:
    largest = num3


print("\n✅ Largest Number is:", largest)

# Even or Odd
if largest % 2 == 0:
    print(" It is Even")
else:
    print(" It is Odd")

# Divisible by 5
if largest % 5 == 0:
    print(" Divisible by 5")
else:
    print(" Not divisible by 5")

print("\nthankyou🎉🎉")





#DAY 5

print(" ======== !!🏆🎯Average Marks Calculator🎯🏆 ")

#student name
student_name = input("Enter your name: ").title()
print(student_name)

#student marks
English_marks = int(input("Enter english marks: "))
Maths_marks = int(input("Enter maths marks: "))
Sst_marks = int(input("Enter sst marks: "))
Science_marks = int(input("Enter science marks: "))
Bce_marks = int(input("Enter bce marks: "))


#total marks
Total_marks = English_marks + Maths_marks + Sst_marks + Science_marks + Bce_marks
print("total_marks",Total_marks)

#averge marks
Average = Total_marks / 5
print(Average)

# percentage marks

percentage = (Total_marks / 500) * 100 
print( percentage)
# Grade System

if percentage >= 90:
    grade = "A+ 🥇"
    remark = "Excellent Performance 🎉"

elif percentage >= 75:
    grade = "A "
    remark = "Very Good "

elif percentage >= 60:
    grade = "B "
    remark = "Good Job "

elif percentage >= 40:
    grade = "C "
    remark = "Needs Improvement 📚"

else:
    grade = "Fail ❌"
    remark = "Work hard"


# Top Subject
highest_marks = max(
    English_marks,
    Maths_marks,
    Sst_marks,
    Science_marks,
    Bce_marks
)

# Weakest Subject
lowest_marks = min(
     English_marks,
    Maths_marks,
    Sst_marks,
    Science_marks,
    Bce_marks
)



print("====== REPORT CARD ======")


print("Name:", student_name)
print("Total Marks:", Total_marks, "/500")
print("Average Marks:", Average)
print("Percentage:", percentage, "%")

print("Grade:", grade)
print("Remark:", remark)

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print("======================================")
print("Thank You 🎉")






#day 6
print("*\*\*\*\*\* PASSWORD STRENGTH CHECKER */*/*/*/*/*")

password = input("Enter password: ")

number_count  = 0
digit_count =0
letter_upper = 0
specialcharacter_count = 0


len_password = len(password)
if len_password >= 8:


    print("valid password")
else:
    print("invalid")

for digit in password:
    if digit.isdigit():
        digit_count += 1

for letter in password :
    if letter.isupper():
        letter_upper += 1

for specialcharacter in password :
    if specialcharacter in "@!%$":
        specialcharacter_count +=  1


if len_password >= 8 and digit_count > 0 and letter_upper > 0 and specialcharacter_count > 0:
    print("Strong password💯")

elif len_password >= 8 or digit_count > 0 and letter_upper > 0:
    print("Medium password🆗")
else:
    print("Weak password")