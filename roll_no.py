roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12: 'Judy', 30: 'Shane', 23: 'Aaron'}
print("Completed Applications:", set(student_details.keys()))
print("Pending Applications:", roll_numbers - set(student_details.keys()))
