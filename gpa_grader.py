import pandas as pd
import matplotlib.pyplot as plt
grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

grades_scale= []
for i in range(len(grades)):
   # round functionis used to round up to 2 decimals after the ".". This function to create the grades-Scale
    value= float(round(4.0-(i*(4.0/len(grades))), 2)) # its y= mx+b rule
    grades_scale.append(value)

# [-1] to count from the bottom to replace the last float in Grade_Scale table to zero.
grades_scale[-1] = 0.00
# To create a table from grade and grade-scale
df_grades = pd.DataFrame()
df_grades["x1"] = pd.Series(grades)
df_grades["x2"] = pd.Series(grades_scale)
df_grades.columns = ['Grade', 'Grade_scale']
print(df_grades)

reverse_grades = list(reversed(grades))
reverse_grades_float = list(reversed(grades_scale))
df_reversed = pd.DataFrame()
df_reversed['Grades'] = pd.Series(reverse_grades)
df_reversed['Grades_scale'] = pd.Series(reverse_grades_float)

# df_reversed.plot(x= 'Grades', y = 'Grades_scale', label = "Student Grade")

# Function to calculate the 4 years grade
def gpa(sample):
    f_list = []
    for item1 in range(len(df_grades)):
        for item2 in sample:
            col1 = df_grades['Grade']
            col2 = df_grades['Grade_scale']
            if col1[item1] == item2: # = is a variable but == to check if they are the same thing.
                f_list.append(col2[item1])
    return sum(list(f_list)) / len(f_list)

# This Variable to feed the program with 4 years grade  input to calculate total GPA.
student = ["A+", "C-", "B", "D-"]
gpa = gpa(student)

# Plot the grade chart based on scale
plt.bar(df_reversed['Grades'],df_reversed['Grades_scale'], color='orange', label = "Student Grade")
# insert Horizontial line for student score
plt.axhline(y = gpa, color = "red", linestyle = "-.")
# Add main title, insert text with data line , add labels for x and y-axis
plt.title("Grading Calculator", fontsize = 30, color = "green")
text = dict(ha='left', va='center', fontsize=15, color='black',bbox={'facecolor': 'green', 'alpha': 0.2, 'pad': 4})
plt.text(0.1, 4, "Student Score = {}".format(gpa), **text)
plt.xlabel("Grades",fontsize = 15)
plt.ylabel("Grade Scale", fontsize = 15, color = "blue")
plt.show()

print("Student Score = {}".format(gpa))