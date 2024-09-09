class Student:
    def __init__(self, name, id, subjects=None):
        self.name = name
        self.id = id
        self.subjects = subjects or {}

    def add_subject(self, subject_name, note):
        self.subjects[subject_name] = note

    def remove_subject(self, subject_name):
        if subject_name in self.subjects:
            del self.subjects[subject_name]

    def calculate_average(self):
        total_score = sum(self.subjects.values())
        num_subjects = len(self.subjects)
        return total_score / num_subjects if num_subjects > 0 else 0


class StudentSystem:
    def __init__(self):
        self.students = {}

    def generate_new_id(self):
        max_id = max([int(student.id) for student in self.students.values()], default=0)
        return str(max_id + 1).zfill(4)

    def add_student(self, name):
        if name in self.students:
            print('Der Student existiert bereits.')
            return
        new_id = self.generate_new_id()
        self.students[name] = Student(name, new_id)
        print(f'Der Student {name} wurde mit der ID {new_id} hinzugefügt.')

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f'Der Student {name} wurde entfernt.')
        else:
            print('Der Student existiert nicht.')

    def update_subject(self, name, subject_name, note):
        if name in self.students:
            student = self.students[name]
            student.add_subject(subject_name, note)
            print(f'Das Fach {subject_name} mit der Note {note} wurde dem Studenten {name} hinzugefügt.')
        else:
            print('Der Student existiert nicht.')

    def remove_subject(self, name, subject_name):
        if name in self.students:
            student = self.students[name]
            student.remove_subject(subject_name)
            print(f'Das Fach {subject_name} wurde entfernt.')
        else:
            print('Der Student existiert nicht.')

    def get_best_student(self):
        best_student = None
        best_avg_score = float('inf')
        for student in self.students.values():
            avg_score = student.calculate_average()
            if avg_score < best_avg_score:
                best_avg_score = avg_score
                best_student = student
        return best_student

    def print_anonymous_results(self):
        for student in self.students.values():
            avg_score = student.calculate_average()
            print(f'ID: {student.id}, Durchschnittsnote: {avg_score:.2f}')

    def print_all_students(self):
        for name, student in self.students.items():
            print(f'Name: {name}, ID: {student.id}')


# Beispiel für die Verwendung des Systems
system = StudentSystem()
system.add_student('Tobi')
system.update_subject('Tobi', 'Deutsch', 3)
system.update_subject('Tobi', 'Mathematik', 3)
system.update_subject('Tobi', 'Python', 2)

system.add_student('Rüdiger')
system.update_subject('Rüdiger', 'Deutsch', 1)
system.update_subject('Rüdiger', 'Mathematik', 3)
system.update_subject('Rüdiger', 'Python', 2)

system.print_all_students()
system.print_anonymous_results()
system.get_best_student()

#system.remove_student('Tobi')