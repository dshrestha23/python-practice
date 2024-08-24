# Description: A simple program that arranges arithmetic problems vertically and horizontally. The program also has an option to show the answers to the problems.


# Function to arrange arithmetic problems vertically and horizontally
def arithmetic_arranger(problems, show_answers=False):
    # Initialize variables to store the lines of the arranged problems
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    arranged_problems = []  # List to store the arranged problems
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            problem_split = problem.split()
            first = problem_split[0]
            operator = problem_split[1]
            second = problem_split[2]
            if (
                operator == "*" or operator == "/"
            ):  # Check if the operator is not '+' or '-' and return an error
                return "Error: Operator must be '+' or '-'."
            if (
                len(first) > 4 or len(second) > 4
            ):  # Check if the numbers are more than four digits and return an error
                return "Error: Numbers cannot be more than four digits."
            if (
                not first.isdigit() or not second.isdigit()
            ):  # Check if the numbers are not digits and return an error
                return "Error: Numbers must only contain digits."
            max_value = max(
                len(first), len(second)
            )  # Get the maximum length of the two numbers
            upperbound = (
                max_value + 2
            )  # Calculate the upperbound for the width of each problem
            if operator == "+":
                solution = str(int(first) + int(second))
            if operator == "-":
                solution = str(int(first) - int(second))

            # Add the numbers to the lines
            line1 += (" " * (upperbound - len(first))) + first + "    "
            line2 += operator + (" " * (upperbound - len(second) - 1)) + second + "    "
            line3 += ("-" * upperbound) + "    "
            line4 += (" " * (upperbound - len(solution))) + solution + "    "
        # Remove the extra spaces at the end of each line
        line1 = line1.rstrip()
        line2 = line2.rstrip()
        line3 = line3.rstrip()
        line4 = line4.rstrip()
        # Check if the user wants to show the answers
        if show_answers == True:
            arranged_problems = arranged_problems = "\n".join(
                (line1, line2, line3, line4)
            )
        else:
            arranged_problems = "\n".join((line1, line2, line3))
    # Return the arranged problems
    return arranged_problems


print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
