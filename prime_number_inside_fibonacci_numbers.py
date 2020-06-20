def fibonacci(amount):
    number_one = 1
    number_two = 1

    if amount <= 0:
        print("Please enter a positive number")
        return

    if amount == 1:
        print("Fibonacci value:", number_one)
        return

    for _ in range(0, amount):
        yield number_one
        number_one, number_two = number_two, number_one + number_two

def is_prime(number):
    return next((False for i in range(2, number) if number % i == 0), number)

def collect_primes_from(source):
    return [ item for item in source if is_prime(item) and item > 1 ]

amount = int(input("Please enter number time of fibonacci series: "))
fibonacci_generator = fibonacci(amount)
result = collect_primes_from(fibonacci_generator)
print(result)
