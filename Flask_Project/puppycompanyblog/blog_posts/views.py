from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm, UpdateForm


blog_posts = Blueprint('blog_posts', __name__)


# Create
@blog_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')

        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)


# BLOG POST (view)
# we must clarify that we are passing integer, because in db the id is declared as integer.
@blog_posts.route('/<int:blog_post_id>')
def view_blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title=blog_post.title, text=blog_post.text, date=blog_post.date, blog_post=blog_post)


# Update
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET', 'POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # we prevent a user to edit another user`s post
    if blog_post.author != current_user:
        abort(403)

    form = UpdateForm()

    if form.validate_on_submit():

        blog_post.title = form.title.data
        blog_post.text = form.text.data

        db.session.commit()
        flash('Blog Post Updated')

        return redirect(url_for('blog_posts.view_blog_post', blog_post_id=blog_post.id))

    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', form=form, title='Updating')


# Delete
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()

    flash('Blog Post Deleted')

    return redirect(url_for('core.index'))
