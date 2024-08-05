import ollama
import openlit
import datetime
import importlib

openlit.init(
    otlp_endpoint="http://127.0.0.1:4318",
)
time_now = datetime.datetime.now().strftime("%m_%d_%Y_%H%M%S")

user_query = ("How to get the nth fibonacci number without encountering stack overflow issues?"
              " The final function to be executed should be named fibonacci")
message = [
    {"role": "system", "content": "You're a Python genius. Return Python code in response to the user's query. "
                                  "Return only code. No yapping"},
    {"role": "user", "content": f"{user_query} "}

]

response = ollama.chat(model='llama3.1:8b', messages=message)
output_file = f"code_{time_now}.py"
with open(output_file, 'w') as f:
    f.write(response['message']['content'])

module_name = f"code_{time_now}"
module = importlib.import_module(module_name)

n = 1000
print(f"The {n}th fibonacci number is {module.fibonacci(n)}")
