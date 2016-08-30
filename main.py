__author__ = 'vitkyk'


def multi_xor(numbers):
    total = 0
    for v in numbers:
        total ^= v
    return total


def find_answer(numbers):
    min_n = min(numbers)
    sum_n = sum(numbers)
    return sum_n - min_n


def calculate(numbers):
    if multi_xor(numbers) == 0:
        return find_answer(numbers)
    else:
        return "NO"


def read_from_file(file_name):
    cases = list()
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()
    except IOError:
        return False, list(), "File doesn't exist!"

    if int(lines[0]) > (len(lines)-1)/2:
        return False, list(), "File doesn't correct!"

    for i in range(1, len(lines), 2):
        try:
            length = int(lines[i])
        except ValueError:
            length = 0

        numbers = list()
        temp = lines[i+1].replace('\n', '')
        temp = temp.split(' ')

        for v in temp:
            try:
                number = int(v)
            except ValueError:
                number = 0
            if number > 10**6 or number < 1:
                return False, list(), "Ci doesn't correct!"
            numbers.append(number)

        if length > 100 or length < 1 or length != len(numbers):
            return False, list(), "T doesn't correct!"

        cases.append(numbers)

    return True, cases, None


def write_to_file(file_name, data):
    f = open(file_name, 'w')
    for i in range(len(data)):
        f.write(data[i])


def candy(input_file_name, output_file_name):
    is_correct, cases,  error_msg = read_from_file(input_file_name)
    if is_correct:
        answers = list()
        for i in range(len(cases)):
            answers.append("Case #" + str(i+1) + ": " + str(calculate(cases[i])) + '\n')
        write_to_file(output_file_name, answers)
        print "Cases completed successfully!"
    else:
        print error_msg

candy("in.txt", "out.txt")