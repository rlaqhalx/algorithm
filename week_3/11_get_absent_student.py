all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# One way (N^2)
# for all_students in all_students:
#   for present_student in present_students:


def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array: #O(N)
        student_dict[key] = True # 공간복잡도도 O(N)
    for key in present_array: #O(N)
        del student_dict[key]
    for key in student_dict.keys():
        return key

    # 구현해보세요!
    return


print(get_absent_student(all_students, present_students))