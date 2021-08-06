from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('username')

    hasLower = False
    hasUpper = False
    errors = []

    for letter in username:
        if letter.islower():
            hasLower = True
        if letter.isupper():
            hasUpper = True

    if hasUpper == False:
        errors.append("You did not use an uppercase character")
    if hasLower == False:
        errors.append("You did not use a lowercase character")
    if username[-1].isdigit() == False:
        errors.append("You don`t have a number at the end")

    if hasLower and hasUpper and username[-1].isdigit():
        return render_template('report.html')
    else:
        return render_template('error.html', errors=errors)


if __name__ == "__main__":
    app.run(debug=True)
