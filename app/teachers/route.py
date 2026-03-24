from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.route import login_required
from app.services import teacher_service

teachers_bp = Blueprint('teachers', __name__)


@teachers_bp.route('/')
@login_required
def list_teachers():
    all_teachers = teacher_service.list_teachers()
    return render_template('teachers/list.html', teachers=all_teachers)


@teachers_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_teacher():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        speciality = request.form.get('speciality', '').strip()

        if not name or not email or not speciality:
            flash('Tous les champs sont obligatoires.', 'danger')
        else:
            teacher_service.add_teacher(name, email, speciality)
            flash(f'Enseignant "{name}" ajouté avec succès.', 'success')
            return redirect(url_for('teachers.list_teachers'))

    return render_template('teachers/create.html')


@teachers_bp.route('/edit/<int:teacher_id>', methods=['GET', 'POST'])
@login_required
def edit_teacher(teacher_id):
    teacher = teacher_service.get_teacher_by_id(teacher_id)
    if not teacher:
        flash('Enseignant introuvable.', 'danger')
        return redirect(url_for('teachers.list_teachers'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        speciality = request.form.get('speciality', '').strip()
        if not name or not email or not speciality:
            flash('Tous les champs sont obligatoires.', 'danger')
        else:
            teacher_service.update_teacher(teacher_id, name, email, speciality)
            flash(f'Enseignant "{name}" mis à jour.', 'success')
            return redirect(url_for('teachers.list_teachers'))

    return render_template('teachers/edit.html', teacher=teacher)


@teachers_bp.route('/delete/<int:teacher_id>')
@login_required
def delete_teacher(teacher_id):
    teacher = teacher_service.get_teacher_by_id(teacher_id)
    if teacher:
        teacher_service.delete_teacher(teacher_id)
        flash(f'Enseignant "{teacher["name"]}" supprimé.', 'success')
    else:
        flash('Enseignant introuvable.', 'danger')
    return redirect(url_for('teachers.list_teachers'))