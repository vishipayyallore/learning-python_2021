student_list1 = ['Tim', 'Drake', 'Lary', 'John']

student_list2 = ['Andrew', 'John', 'Lary', 'Steven', 'Chris']

def checkStudent(students_list, search_name):

    index = 1
    for student in students_list:
    
        if student == search_name:
            print(search_name, ' was found in ', students_list, ' at ', index, ' location')
            return
    
        index += 1
    print(search_name, ' not available in ', students_list)

checkStudent(student_list1, 'Ashish') 

checkStudent(student_list2, 'Chris')