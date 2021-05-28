import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Task
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/task', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.form.get('task')

        if len(task) < 1:
            flash('Task is too short!', category='error')
        else:
            try:
                new_task = Task(data_t=task, user_id=current_user.id)
                db.session.add(new_task)
                db.session.commit()
                flash('Task added!', category='success')
            except AttributeError:
                flash('Only logged in users can add tasks!', category='error')
    return render_template("task.html", user=current_user)


@views.route('/task/delete-task', methods=['POST'])
def delete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return jsonify({})
