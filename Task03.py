file = open("name.txt", "r+", encoding="utf-8")
list_name_students = []
lines = file.readlines()
for line in lines:
    list_name_students.append(line.strip())
def rename_student(new_list_name_studenst):
    '''
    Увелечение шрифта, в случае оценки более 4
    '''
    file.seek(0)
    for i in range(len(new_list_name_studenst)):
        if int(str(new_list_name_studenst[i])[len(new_list_name_studenst[i]) - 1]) > 4: # отсекаем оценки ниже 4
            new_list_name_studenst[i] = str(new_list_name_studenst[i]).upper()
        file.write('\n' + str(list_name_students[i]))
    print(new_list_name_studenst)
    file.close()
rename_student(list_name_students)




