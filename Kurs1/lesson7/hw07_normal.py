# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Shcool:
    def __init__(self, name, surname, patronymic):
                
        self.name = name 
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())


class Student(Shcool):
    def __init__(self, name, surname, patronymic, mom, dad, class_room):
        Shcool.__init__(self, name, surname, patronymic)
        self.mom = mom
        self.dad = dad
        self.class_room = class_room


class Teacher(Shcool):
    def __init__(self, name, surname, patronymic, subject):
        Shcool.__init__(self, name, surname, patronymic)
        self.subject = subject


class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
         
if __name__ == "__main__":
    teachers = [Teacher("Алексей", "Сорокин", "Сергеевич", "Литература"),
                Teacher("Владимир", "Иванов", "Владимирович", "Русский"),
                Teacher("Сергей", "Смирнов", "Александрович", "Математика"),
                Teacher("Николай", "Петров", "Артемович", "Химия"),
                Teacher("Светана", "Семёнова", "Дмитриевна", "Физика"),
                Teacher("Ирина","Степанова","Игоревна", "Биология")]   
    classes = [Class_rooms("9 A", [teachers[2], teachers[3],teachers[0]]),
               Class_rooms("10 Б", [teachers[1], teachers[0],teachers[5]]),
               Class_rooms("11 B", [teachers[3], teachers[4],teachers[5]])]
    parents = [Student("Алексей", "Иванов", "Дмитриевич"),
               Student("Марина", "Иванова", "Николаевна"),
               Student("Роман", "Павлов", "Сергеевич"),
               Student("Светлана", "Павлова", "Алексеевна"),
               Student("Александр", "Степанов", "Петрович"),
               Student("Виктория", "Степанова", "Михайловна")]
    students = [Student("Михаил", "Иванов", "Алексеевич", parents[0], parents[1], classes[0]),
                Student("Екатерина", "Павлова", "Романовна", parents[2], parents[3], classes[1]),
                Student("Игорь", "Степанов", "Александрович", parents[4], parents[5], classes[2])]  

#print("Список классов в школе: ")

#for f in classes:
   # print(f.class_room)

#for f in classes:
 #   print('Учителя, преподающие в {} классе:'.format(f.class_room))
  #  for teacher in classes[0].teachersdict.values():
        #print(teacher.get_full_name())
    
#for f in classes:
#    print("Ученики в классе {}:".format(f.class_room))
 #   for st in students:
  #      print(st.get_short_name())          

#for f in students[0]:
 #   print(f.get_full_name)

for f in parents:
    print(f.mom())
   

   

             





         



