#1.1 and 1.2
"""
word = str(input())
listword = list(word.lower())

vowels = 'aeiou'
consonants = 'qwrtyplkjmnhgbvfdcxs'

repeat = []
count=1
count1=2

for i in listword:
    if i not in repeat:
     if count not in repeat:
           repeat.append((i,count))


list_vow = []
list_cons = []
list_symb = []

for char, count in repeat:
    if char in vowels:
        list_vow.append((char,count))
    elif char in consonants:
        list_cons.append((char,count))
    else:
        list_symb.append((char,count))



print(repeat)

print('vowels', list_vow)
print('cons:', list_cons)
print('symbols', list_symb)
"""

'2.1-2.4'

"2.1"
studentname = input("Enter student name: ")
assignments = list(map(int, input("Enter scores for assignments with spaces(at least 4): ").split()))
labs = list(map(float, input("Enter scores for labs separated with spaces(2): ").split()))
tests = list(map(int, input("Enter scores for tests separated with spaces(2): ").split()))

studentname2 = input("Enter second student name: ")
assignments2 = list(map(int, input("Enter scores for assignments with spaces(at least 4): ").split()))
labs2 = list(map(float, input("Enter scores for labs separated with spaces(2): ").split()))
tests2 = list(map(int, input("Enter scores for tests separated with spaces(2): ").split()))


student = {
    'name': studentname,
    'assignment': assignments,
    'test': tests,
    'lab': labs
}
student2 = {
    'name': studentname2,
    'assignment': assignments2,
    'test': tests2,
    'lab': labs2
}

print(student)

"2.2"

expected_activities = {
    'assignment': 4,
    'test': 2,
    'lab': 2
}

submission_count = sum(len(student[key]) for key in expected_activities)
submission_rate = {student['name']: submission_count}

print(submission_rate)

"2.3"

name = student['name']
if submission_rate.get(name, 0) >= 4:
    assignment_avg = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
    lab_avg = sum(student['lab']) / len(student['lab']) if student['lab'] else 0
    test_avg = sum(student['test']) / len(student['test']) if student['test'] else 0

    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
else:
    final_grade = 0

student['final_grade'] = final_grade

"2.4"

students = {
    student['name']: student,
    student2['name']: student2
}

print(students)

