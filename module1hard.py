grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
average_grades={}
for idx,student  in enumerate(sorted(students)):
 if idx < len(grades): average_grade = sum(grades[idx]) / len(grades[idx])
average_grades[student]=round(average_grade,2)
print(average_grades)