students = []
_next_id = 1


def matricule_exists(matricule, exclude_id=None):
    for s in students:
        if s['matricule'] == matricule and s['id'] != exclude_id:
            return True
    return False


def add_student(nom, prenom, date_naissance, classe, matricule):
    global _next_id
    student = {
        'id': _next_id,
        'nom': nom,
        'prenom': prenom,
        'date_naissance': date_naissance,
        'classe': classe,
        'matricule': matricule
    }
    students.append(student)
    _next_id += 1
    return student


def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]


def list_students():
    return students


def get_student_by_id(student_id):
    for s in students:
        if s['id'] == student_id:
            return s
    return None


def update_student(student_id, nom, prenom, date_naissance, classe, matricule):
    for s in students:
        if s['id'] == student_id:
            s['nom'] = nom
            s['prenom'] = prenom
            s['date_naissance'] = date_naissance
            s['classe'] = classe
            s['matricule'] = matricule
            return s
    return None