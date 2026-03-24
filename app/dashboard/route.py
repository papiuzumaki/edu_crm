from flask import Blueprint, render_template
from app.auth.route import login_required
from app.services import student_service, teacher_service, course_service

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def index():
    stats = {
        'nb_students': len(student_service.list_students()),
        'nb_teachers': len(teacher_service.list_teachers()),
        'nb_courses': len(course_service.list_courses()),
    }
    return render_template('dashboard/index.html', stats=stats)