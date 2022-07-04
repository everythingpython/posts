from functools import partial

## Example 1

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(f"Decimal representation of '10010' is {basetwo('10010')}")


## Example 2

def salary_part(x, y):
    return x*y

base_salary = 30000
salary_add = partial(salary_part, base_salary)
da = salary_add(0.4)
lta = salary_add(0.2)

print(f"Net Salary = {base_salary+da+lta}")


# https://github.com/pandas-dev/pandas/blob/e2fedf1e994c4eea90a60e865a9c11b5c3696937/pandas/tests/window/test_rolling_quantile.py