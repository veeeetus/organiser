from organiser import app, db
from organiser.forms import LoginForm, RegistrationForm, EditProfileForm, AddTask, DelTask, MoveTask
from organiser.models import User, Task
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime, date

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = AddTask()

    ptasks = Task.query.filter_by(user_id = current_user.id).order_by(Task.deadline.asc()).limit(8)
    ad = (datetime.utcnow()).date()
    notifications = list()

    for x in ptasks:
        if not x.phase == "done" and (x.deadline.date() - ad).days > 0:
            notifications.append(f"{(x.deadline.date() - ad).days} days until deadline for: {x.title}")
    
    if form.validate_on_submit():

        id = current_user.id
        title = form.title.data
        title = title.lower()
        body = form.body.data
        date = form.deadline.data

        task = Task.query.filter_by(user_id = current_user.id, title=title).first()

        if task:
            flash("This title already exists")
        else:  
            task = Task(title=title, body=body, phase="todo", deadline=date, user_id = id)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('tasks'))    

    return render_template('index.html', addform=form, notifications=notifications)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have been registered")
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
    
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        if current_user.username != form.username.data:
            user = User.query.filter_by(username = form.username.data).first()
            if user:
                flash("This username is already taken :(")
                return redirect(url_for('edit_profile'))
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    else:
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@app.route('/tasks')
@login_required
def tasks():

    todo = current_user.todo()
    doing = current_user.doing()
    done = current_user.done()

    t = len(todo)
    di = len(doing)
    dd = len(done)

    lengtharr = [t, di, dd]
    length = max(lengtharr)
    
    return render_template('tasks.html', todo=todo, doing=doing, done=done, length=length)

@app.route('/move', methods=['GET', 'POST'])
@login_required
def move():
    form = MoveTask()

    if form.validate_on_submit():

        title = form.title.data

        test = Task.query.filter_by(user_id = current_user.id, title=title).first()
        if not test:
            flash("This task doesn't exist")
            return redirect(url_for('move'))

        choice = form.phase.data
        task = Task.query.filter_by(user_id = current_user.id, title=title).first()

        if task.phase == 'done' or choice == 'todo':
            flash('Told you not to!!')
        elif task.phase == choice:
            flash("It's the same phase")
        else:
            task.phase = choice
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('tasks'))
    
    return render_template('move.html', moveform=form)

@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DelTask()

    if form.validate_on_submit():
        title = form.title.data
        task = Task.query.filter_by(user_id = current_user.id, title=title).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('tasks'))
        else:
            flash("Task doesn't exist")
            return redirect(url_for('delete'))

    return render_template('delete.html', delform=form)