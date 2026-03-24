teachers = []
_next_id = 1


def add_teacher(name, email, speciality):
    global _next_id
    teacher = {
        'id': _next_id,
        'name': name,
        'email': email,
        'speciality': speciality
    }
    teachers.append(teacher)
    _next_id += 1
    return teacher


def delete_teacher(teacher_id):
    global teachers
    teachers = [t for t in teachers if t['id'] != teacher_id]


def list_teachers():
    return teachers


def get_teacher_by_id(teacher_id):
    for t in teachers:
        if t['id'] == teacher_id:
            return t
    return None


def update_teacher(teacher_id, name, email, speciality):
    for t in teachers:
        if t['id'] == teacher_id:
            t['name'] = name
            t['email'] = email
            t['speciality'] = speciality
            return t
    return None