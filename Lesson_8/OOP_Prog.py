class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname


class Teacher(Person):
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def to_take(self, subj):
        self.knowledge.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subject = list(subjects)

    def my_list(self):
        return self.subject


s = Subject('math', 'physics')
t = Teacher('Ivan', 'Ivanov')
p_1 = Pupil('Sidr', 'Sidorov')
p_2 = Pupil('Petr', 'Petrov')
p_3 = Pupil('Abdrew', 'Andreev')

print(t, p_1, p_2, p_3)
t.to_teach(s, p_1, p_2, p_3)
t.to_teach(s, p_1, p_2, p_3)
print(p_1.knowledge[0].my_list())
