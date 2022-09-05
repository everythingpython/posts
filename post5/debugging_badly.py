
import fastwsgi
from flask import Flask, request, flash, redirect, render_template, session
from random import randint

app = Flask(__name__)
app.secret_key = "abc" + str(randint(10, 1000))


def get_nth_fibonacci_num(n):
    try:
        if n > 15:
            return "Not supported"
        if n == 1:
            return 1
        if n == 2:
            return 1
        return get_nth_fibonacci_num(n - 1) + get_nth_fibonacci_num(n - 2)
    except Exception as e:
        return e


@app.route("/", methods=('GET', 'POST'))
def nth_fibonacci_number():
    if request.method == 'POST':
        session.clear()
        n = request.form['n']

        messages = {}

        if not n:
            flash(f'n is required!')
        else:
            n = int(n)
            val = get_nth_fibonacci_num(n)
            messages['val'] = val
            flash(f"{n}th fibonacci number = {val}")

        return redirect(request.referrer)

    return render_template('numbers.html')


if __name__ == "__main__":
    fastwsgi.run(wsgi_app=app, host="0.0.0.0", port=5000)
