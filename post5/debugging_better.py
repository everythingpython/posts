from loguru import logger

import fastwsgi
from flask import Flask, request, flash, redirect, render_template, session
from random import randint
import sys

sys.tracebacklimit = -1

app = Flask(__name__)
app.secret_key = "abc" + str(randint(10, 1000))


def get_nth_fibonacci_num(n):
    try:
        if n <= 0:
            raise Exception("Number can't be negative")
        # assert(n > 0), "Number can't be negative"

        if n > 15:
            return "Not supported"
        if n == 1:
            return 1
        if n == 2:
            return 1
        return get_nth_fibonacci_num(n - 1) + get_nth_fibonacci_num(n - 2)
    except Exception as e:
        logger.exception(f"This isn't going to work - {e}")
        return None


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
            if isinstance(val, int) and val >0:
                logger.debug(f"Fibonacci method successful for {n}")
            messages['val'] = val
            flash(f"{n}th fibonacci number = {val}")

        return redirect(request.referrer)

    return render_template('numbers.html')


if __name__ == "__main__":
    fastwsgi.run(wsgi_app=app, host="0.0.0.0", port=5000)
