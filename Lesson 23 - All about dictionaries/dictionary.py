student_data = {'id1' : '1'  , 'name' : 'Anayah' , 'grade' : '6'}
print('The student details are ' , student_data)
student_data ['Country'] = 'United Kingdom'
print(student_data . get('name' , 'not found'))
print('The student details are ' , student_data)
print(len(student_data))
