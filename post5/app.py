import json
from random import randint
from flask import Flask, request, Response, session
from loguru import logger
from debugging_badly import compute_nth_fibonacci_number_bad
from debugging_better import compute_nth_fibonacci_number_good

app = Flask(__name__)
app.secret_key = "abc" + str(randint(10, 1000))
app.run(debug=True)

with app.app_context():
    @app.route("/bad_debugging", methods=('GET', 'POST'))
    def nth_fibonacci_number_bad():
        if request.method == 'POST':
            session.clear()
            n = request.form['n']

            messages = {}

            if not n:
                print(f'n is required!')
            else:
                n = int(n)
                val = compute_nth_fibonacci_number_bad(n)
                messages['val'] = val
                print(f"{n}th fibonacci number = {val}")

            return Response(json.dumps({"value": val}), status=200, mimetype="application/json")


    @app.route("/good_debugging", methods=('GET', 'POST'))
    def nth_fibonacci_number():
        if request.method == 'POST':
            session.clear()
            n = request.form['n']

            messages = {}

            if not n:
                logger.info(f'n is required!')
            else:
                n = int(n)
                val = compute_nth_fibonacci_number_good(n)
                if isinstance(val, int) and val > 0:
                    logger.debug(f"Fibonacci method successful for {n}")
                messages['val'] = val
                logger.info(f"{n}th fibonacci number = {val}")

            return Response(json.dumps({"value": val}), status=200, mimetype="application/json")
