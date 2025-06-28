from flask import Blueprint, render_template, request, redirect, url_for
from .models import Member
from . import db

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    members = Member.query.all()
    return render_template('index.html', members=members)


@routes.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    role = request.form['role']
    member = Member(name=name, email=email, role=role)
    db.session.add(member)
    db.session.commit()
    return redirect(url_for('routes.index'))


@routes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    member = Member.query.get(id)
    if request.method == 'POST':
        member.name = request.form['name']
        member.email = request.form['email']
        member.role = request.form['role']
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('form.html', member=member)


@routes.route('/delete/<int:id>')
def delete(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('routes.index'))
