print("Exam Grade Calculator")

input("Name of exam: ")

max_possible_score = float(input("Max Possible Score: "))
your_score = float(input("Your Score: "))

score_percentage = round(float(your_score/max_possible_score) * 100, 2)



if score_percentage >= 90:
    print("You have got {0}% which is a A+".format(score_percentage))
elif score_percentage >= 80:
    print("You have got {0}% which is a A-".format(score_percentage))
elif score_percentage >= 70:
    print("You have got {0}% which is a B".format(score_percentage))
elif score_percentage >= 60:
    print("You have got {0}% which is a C".format(score_percentage))
elif score_percentage >= 50:
    print("You have got {0}% which is a D".format(score_percentage))
elif score_percentage >= 40:
    print("You have got {0}% which is a U".format(score_percentage))
else:
    print("You have got {0}% which is a F".format(score_percentage))
