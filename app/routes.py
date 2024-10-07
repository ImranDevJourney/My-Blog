from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User, Post, Comment
from .forms import RegistrationForm, LoginForm, PostForm, CommentForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint

# Blueprint for main routes
main = Blueprint('main', __name__)


@main.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Log in the user after registration
        login_user(user)

        flash('Your account has been created! You are now logged in.', 'success')
        return redirect(url_for('main.home'))

    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        print("Form submitted successfully.")  # Debug statement
        user = User.query.filter_by(email=form.email.data).first()
        print(f"User found: {user}")  # Debug statement

        # Check if user exists and verify password
        if user:
            print(
                f"Password check: {'valid' if check_password_hash(user.password, form.password.data) else 'invalid'}")  # Debug statement
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('main.home'))
            else:
                flash('Login failed. Check your email and password.', 'danger')
        else:
            flash('Login failed. Check your email and password.', 'danger')

    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.home'))


@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # Create a new post with the submitted data
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))

    # Render the post template for creating a new post
    return render_template('post.html', form=form)  # Use post.html for creating posts
@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    # Attempt to retrieve the post; if not found, return a 404 error
    post = Post.query.get_or_404(post_id)
    comment_form = CommentForm()

    # Handle comment submission
    if comment_form.validate_on_submit():
        # Create a new comment and associate it with the post and current user
        comment = Comment(content=comment_form.content.data, post=post, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
        return redirect(url_for('main.post', post_id=post.id))  # Redirect to the same post after adding a comment

    # Retrieve all comments associated with the post
    comments = Comment.query.filter_by(post_id=post.id).all()

    # Render the post template with the post data, comment form, and comments
    return render_template('post.html', post=post, comment_form=comment_form, comments=comments)

@main.route('/comment/<int:comment_id>/like', methods=['POST'])
@login_required
def like_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    comment.likes += 1
    db.session.commit()
    flash('You liked this comment!', 'success')
    return redirect(url_for('main.post', post_id=comment.post_id))  # Closing parenthesis added here

@main.route('/comment/<int:comment_id>/dislike', methods=['POST'])
@login_required
def dislike_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    comment.dislikes += 1
    db.session.commit()
    flash('You disliked this comment!', 'warning')
    return redirect(url_for('main.post', post_id=comment.post_id))