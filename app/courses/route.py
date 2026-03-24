from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.route import login_required
from app.services import course_service, teacher_service, student_service

courses_bp = Blueprint('courses', __name__)


@courses_bp.route('/')
@login_required
def list_courses():
    all_courses = course_service.list_courses()
    all_teachers = {t['id']: t for t in teacher_service.list_teachers()}
    all_students = {s['id']: s for s in student_service.list_students()}
    return render_template('courses/list.html',
                           courses=all_courses,
                           teachers=all_teachers,
                           students=all_students)


@courses_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_course():
    all_teachers = teacher_service.list_teachers()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        teacher_id = request.form.get('teacher_id', '').strip()

        if not title or not teacher_id:
            flash('Titre et enseignant sont obligatoires.', 'danger')
        else:
            course_service.add_course(title, int(teacher_id))
            flash(f'Cours "{title}" créé avec succès.', 'success')
            return redirect(url_for('courses.list_courses'))

    return render_template('courses/create.html', teachers=all_teachers)


@courses_bp.route('/edit/<int:course_id>', methods=['GET', 'POST'])
@login_required
def edit_course(course_id):
    course = course_service.get_course_by_id(course_id)
    if not course:
        flash('Cours introuvable.', 'danger')
        return redirect(url_for('courses.list_courses'))

    all_teachers = teacher_service.list_teachers()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        teacher_id = request.form.get('teacher_id', '').strip()
        if not title or not teacher_id:
            flash('Titre et enseignant sont obligatoires.', 'danger')
        else:
            course_service.update_course(course_id, title, int(teacher_id))
            flash(f'Cours "{title}" mis à jour.', 'success')
            return redirect(url_for('courses.list_courses'))

    return render_template('courses/edit.html', course=course, teachers=all_teachers)


@courses_bp.route('/delete/<int:course_id>')
@login_required
def delete_course(course_id):
    course = course_service.get_course_by_id(course_id)
    if course:
        course_service.delete_course(course_id)
        flash(f'Cours "{course["title"]}" supprimé.', 'success')
    else:
        flash('Cours introuvable.', 'danger')
    return redirect(url_for('courses.list_courses'))


@courses_bp.route('/<int:course_id>/assign', methods=['GET', 'POST'])
@login_required
def assign_student(course_id):
    course = course_service.get_course_by_id(course_id)
    if not course:
        flash('Cours introuvable.', 'danger')
        return redirect(url_for('courses.list_courses'))

    all_students = student_service.list_students()

    if request.method == 'POST':
        student_id = request.form.get('student_id', '').strip()
        if student_id:
            course_service.assign_student_to_course(course_id, int(student_id))
            flash('Étudiant inscrit au cours.', 'success')
            return redirect(url_for('courses.list_courses'))

    return render_template('courses/assign.html', course=course, students=all_students)


@courses_bp.route('/<int:course_id>/unassign/<int:student_id>')
@login_required
def unassign_student(course_id, student_id):
    course = course_service.get_course_by_id(course_id)
    if not course:
        flash('Cours introuvable.', 'danger')
        return redirect(url_for('courses.list_courses'))
    course_service.unassign_student_from_course(course_id, student_id)
    flash('Étudiant désinscrit du cours.', 'success')
    return redirect(url_for('courses.list_courses'))