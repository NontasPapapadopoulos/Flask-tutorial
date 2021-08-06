from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signUp.html')


@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    full_name = first + last

    hasLower = False
    hasUpper = False

    for letter in full_name:
        if letter.islower():
            hasLower = True
        if letter.isUpper():
            hasUpper = True

    if hasLower and hasUpper and full_name[-1].isdigit():
        return render_template('thankYou.html', first=first, last=last)
    else:
        page_not_found()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.route('/infos')
# def info():
#     return "<h1> puppies are cute </h1>"


# @app.route('/page/<name>')
# def other_page(name):
#     return "User: {}".format(name)


# @app.route('/latin/<name>')
# def convert_to_lation(name):
#     if name[-1] != 'y':
#         name = name + "y"
#     else:
#         name = name[0:-2] + "iful"

#     return "<h1> name in latin: {} </h1>".format(name)


# @app.route('/basic')
# def basic_page():
#     name = "Nondas"
#     return render_template("basic.html", name=name)


# @app.route('/name/<name>')
# def display_name(name):
#     return render_template("display.html", name=name)


# @app.route('/home')
# def home():
#     return render_template('home.html')


# @app.route('/puppy/<name>')
# def pup_name(name):
#     return render_template('puppy.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
