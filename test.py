class Teacher():

    def teach(self):
        print("преподаватель учит")

#Создаем класс School с функцией init, внутри которой будет еще одна функция — start_lesson (начать урок).

class School():

    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

# При агрегации объект создается не внутри функции, а отдельно.
# 3. Создаем объект my_teacher, чтобы объект сохранялся в переменную:

my_teacher = Teacher()

my_school = School(my_teacher)


print(my_teacher.teach())

print(my_school.start_lesson())
