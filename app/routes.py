from flask import Blueprint, render_template, request, jsonify
from .forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data == "fail":
            return jsonify(status='error', message='Registration failed. Try again.')
        else:
            return jsonify(status='success', message='Registration successful!')
    return render_template('register.html', form=form)

@main.route('/validate', methods=['POST'])
def validate():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.username.data == "fail":
            return jsonify(status='error', message='Registration failed. Try again.')
        else:
            return jsonify(status='success', message='Registration successful!')
    return jsonify(status='error', message='Validation failed. Please correct the errors.', errors=form.errors)
