from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.route import login_required
from app.services import student_service

students_bp = Blueprint('students', __name__)


@students_bp.route('/')
@login_required
def list_students():
    all_students = student_service.list_students()
    return render_template('students/list.html', students=all_students)


@students_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_student():
    if request.method == 'POST':
        nom = request.form.get('nom', '').strip()
        prenom = request.form.get('prenom', '').strip()
        date_naissance = request.form.get('date_naissance', '').strip()
        classe = request.form.get('classe', '').strip()
        matricule = request.form.get('matricule', '').strip()

        if not nom or not prenom or not matricule or not classe:
            flash('Nom, prénom, classe et matricule sont obligatoires.', 'danger')
        elif student_service.matricule_exists(matricule):
            flash(f'Le matricule "{matricule}" est déjà utilisé.', 'danger')
        else:
            student_service.add_student(nom, prenom, date_naissance, classe, matricule)
            flash(f'Étudiant "{prenom} {nom}" ajouté avec succès.', 'success')
            return redirect(url_for('students.list_students'))

    return render_template('students/create.html')


@students_bp.route('/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = student_service.get_student_by_id(student_id)
    if not student:
        flash('Étudiant introuvable.', 'danger')
        return redirect(url_for('students.list_students'))

    if request.method == 'POST':
        nom = request.form.get('nom', '').strip()
        prenom = request.form.get('prenom', '').strip()
        date_naissance = request.form.get('date_naissance', '').strip()
        classe = request.form.get('classe', '').strip()
        matricule = request.form.get('matricule', '').strip()

        if not nom or not prenom or not matricule or not classe:
            flash('Nom, prénom, classe et matricule sont obligatoires.', 'danger')
        elif student_service.matricule_exists(matricule, exclude_id=student_id):
            flash(f'Le matricule "{matricule}" est déjà utilisé.', 'danger')
        else:
            student_service.update_student(student_id, nom, prenom, date_naissance, classe, matricule)
            flash(f'Étudiant "{prenom} {nom}" mis à jour.', 'success')
            return redirect(url_for('students.list_students'))

    return render_template('students/edit.html', student=student)


@students_bp.route('/delete/<int:student_id>')
@login_required
def delete_student(student_id):
    student = student_service.get_student_by_id(student_id)
    if student:
        student_service.delete_student(student_id)
        flash(f'Étudiant "{student["prenom"]} {student["nom"]}" supprimé.', 'success')
    else:
        flash('Étudiant introuvable.', 'danger')
    return redirect(url_for('students.list_students'))