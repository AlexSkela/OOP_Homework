class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grade_lector(self, lector, course, grade):
        if isinstance(lector, Lectors) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grade_of_student:
                lector.grade_of_student[course] += [grade]
            else:
                lector.grade_of_student[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self, grades):
        sum_hm = 0
        for course in grades:
            sum_hm += sum(grades[course]) / len(grades[course])
        return round(sum_hm / len(grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        else:
            res = self.average_grade(self.grades) < other.average_grade(other.grades)
            if res == False:
                res_1 = f'{self.name} {self.surname} учится лучше, чем {other.name} {other.surname}'
                return res_1
            elif res == True:
                res_2 = f'{self.name} {self.surname} учится хуже, чем {other.name} {other.surname}'
                return res_2

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.average_grade(self.grades)} \n' \
              f'Курсы в процессе обучения: {" ".join(self.courses_in_progress)} \n' \
              f'Завершенные курсы: {" ".join(self.finished_courses)} \n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectors(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_of_student = {}

    def average_grade(self, grades):
        sum_hm = 0
        for course in grades:
            sum_hm += sum(grades[course]) / len(grades[course])
        return round(sum_hm / len(grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Lectors):
            print('Такого лектора нет')
            return
        else:
            res = self.average_grade(self.grade_of_student) < other.average_grade(other.grade_of_student)
            if res == False:
                res_1 = f'Лектор {self.surname} преподает лучше, чем лектор {other.surname}'
                return res_1
            elif res == True:
                res_2 = f'Лектор {self.surname} преподает хуже, чем лектор {other.surname}'
                return res_2

    def __str__(self):
        res_1 = f'Имя: {self.name} \n'  \
                f'Фамилия: {self.surname} \n' \
                f'Средняя оценка за лекции: {self.average_grade(self.grade_of_student)} \n'
        return res_1


class Reviewers(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res_1 = f'Имя: {self.name} \n'  \
                f'Фамилия: {self.surname}'
        return res_1


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Java']

next_student = Student('Vova', 'Shman', 'm')
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']
next_student.courses_in_progress += ['Java']

cool_mentor = Reviewers('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Git', 20)

cool_mentor.rate_hw(next_student, 'Python', 8)
cool_mentor.rate_hw(next_student, 'Python', 9)
cool_mentor.rate_hw(next_student, 'Python', 3)
cool_mentor.rate_hw(next_student, 'Git', 5)
cool_mentor.rate_hw(next_student, 'Git', 2)

main_mentor = Lectors('Ivan', 'Petrov')
main_mentor.courses_attached += ['Python']
main_mentor.courses_attached += ['Git']

next_mentor = Lectors('Slava', 'Kotov')
next_mentor.courses_attached += ['Python']
next_mentor.courses_attached += ['Java']

best_student.grade_lector(main_mentor, 'Git', 4)
best_student.grade_lector(main_mentor, 'Python', 10)

next_student.grade_lector(next_mentor, 'Java', 10)
next_student.grade_lector(next_mentor, 'Python', 10)


print(best_student.grades)
print(next_student.grades)

print(best_student)
print(next_student)

print(best_student < next_student)

print(main_mentor < next_mentor)


