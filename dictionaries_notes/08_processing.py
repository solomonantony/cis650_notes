#Processing dictionary data

"""Using a dictionary to represent an instructor's grade book."""
grade_book = {
    'Susan': [92, 85, 100],
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],
    'Pantipa': [97, 91, 92]
}
print(grade_book)
# Since a dictionary has key/value pairs, there are a few ways to visit items in the dictionary using for
sum_of_grades = 0
for student in grade_book.keys():
    print(student, grade_book[student], sum(grade_book[student]))
    sum_of_grades += sum(grade_book[student])
print(f'The average of student totals is {sum_of_grades/4}')
#modify thei code and compute average for each student
