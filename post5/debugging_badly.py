def compute_nth_fibonacci_number_bad(n):
    try:
        if n > 15:
            return "Not supported"
        if n == 1:
            return 1
        if n == 2:
            return 1
        return compute_nth_fibonacci_number_bad(n - 1) + compute_nth_fibonacci_number_bad(n - 2)
    except Exception as e:
        return e


