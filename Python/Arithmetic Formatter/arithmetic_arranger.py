def arithmetic_arranger(problems, show=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    line1 = ''
    line2 = ''
    line3 = ''
    summation = ''
    for problem in problems:
        tokens = problem.split(' ')
        first_num, operator, second_num = tokens
        if tokens[1] != '+' and tokens[1] != '-':
            print(problem)
            return "Error: Operator must be '+' or '-'."
        try:
            if int(tokens[0]) // 10 ** 4 != 0 or int(tokens[2]) // 10 ** 4 != 0:
                return "Error: Numbers cannot be more than four digits."
        except ValueError:
            return "Error: Numbers must only contain digits."
        length = max(len(first_num), len(second_num)) + 2
        line1 += ' ' * (length - len(tokens[0])) + tokens[0] + ('    ' if problem != problems[-1] else '')
        line2 += tokens[1] + ' ' * (length - len(tokens[2]) - 1)
        line2 += tokens[2] + ('    ' if problem != problems[-1] else '')
        line3 += '-' * length + ('    ' if problem != problems[-1] else '')
        solution = str(int(first_num) + ((1 if tokens[1] == '+' else -1) * int(second_num)))
        summation += ' ' * (length - len(solution)) + solution + ('    ' if problem != problems[-1] else '')
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + ('\n' + summation if show else '')
    return arranged_problems