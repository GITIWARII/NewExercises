d = {}
values = []
new_list = []
name = input("Enter name:")
for i in range(5):

    Subject = input("Enter Subject of student:")
    marks = int(input("Enter marks:"))
    d[Subject] = marks
    values.append(marks)
def func(name, values):
    new_list =[(list(d.keys())[list(d.values()).index(i)]) for i in values if i > 60]
    print("Name:", name, "-Subjects:", set(new_list))

func(name, values)