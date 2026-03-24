courses = []
_next_id = 1


def add_course(title, teacher_id):
    global _next_id
    course = {
        'id': _next_id,
        'title': title,
        'teacher_id': teacher_id,
        'student_ids': []
    }
    courses.append(course)
    _next_id += 1
    return course


def assign_student_to_course(course_id, student_id):
    for course in courses:
        if course['id'] == course_id:
            if student_id not in course['student_ids']:
                course['student_ids'].append(student_id)
            return course
    return None


def delete_course(course_id):
    global courses
    courses = [c for c in courses if c['id'] != course_id]


def list_courses():
    return courses


def get_course_by_id(course_id):
    for c in courses:
        if c['id'] == course_id:
            return c
    return None


def update_course(course_id, title, teacher_id):
    for c in courses:
        if c['id'] == course_id:
            c['title'] = title
            c['teacher_id'] = teacher_id
            return c
    return None


def unassign_student_from_course(course_id, student_id):
    for course in courses:
        if course['id'] == course_id:
            if student_id in course['student_ids']:
                course['student_ids'].remove(student_id)
            return course
    return None