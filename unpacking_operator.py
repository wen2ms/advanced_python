numbers = range(10)

print(*numbers)

position1 = (10, 10)
position2 = (12, 15)

distance = abs(complex(*position1) - complex(*position2))
print(distance)

student_record = [10001, 34, 56, 78, 64, 23, 67, 88]

student_id, *_, student_mid_score, student_final_score = student_record
print(student_id, student_mid_score, student_final_score)

print_config = {"sep": ", ", "end": "#"}
print(1, 2, 3, **print_config)
