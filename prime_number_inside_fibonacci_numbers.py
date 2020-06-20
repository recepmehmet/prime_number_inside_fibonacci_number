def Fibonacci(desired_times_term):
    number_one = 0
    number_two = 1
    counter_of_fibonacci_terms = 0
    fibonacci_numbers = []

    if desired_times_term <= 0:
        print("Please, Enter a positive number")
    elif desired_times_term == 1:
        print("Fibonacci value : ", number_one)
    else:
        while counter_of_fibonacci_terms < desired_times_term:
            print(number_one)
            fibonacci_numbers.append(number_one)
            number_th = number_one + number_two
            number_one = number_two
            number_two = number_th
            counter_of_fibonacci_terms += 1

    return fibonacci_numbers

def is_prime_number(a_number):
    if a_number > 1:
        # check for factors
        for i in range(2, a_number):
            if (a_number % i) == 0:
                break
        else:
            return a_number


def prime_number_finder_inside_a_array(a_array):
    prime_number_keeper = []
    for array_counter in a_array:
        if is_prime_number(int(array_counter)) != None:
            prime_number_keeper.append(is_prime_number(int(array_counter)))

    return prime_number_keeper


taken_number_of_fibo = input("Please enter number time of fibonacci series")
fibonacci_numbers = Fibonacci(int(taken_number_of_fibo))
prime_numbers_in_fibonacci_desired_times_number = prime_number_finder_inside_a_array(fibonacci_numbers)
print(prime_numbers_in_fibonacci_desired_times_number)