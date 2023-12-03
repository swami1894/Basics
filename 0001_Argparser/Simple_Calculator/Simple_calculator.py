from argparse import ArgumentParser
from sys import stdout


def simple_calculator(a:int, b:int, oper:str):

    result = None

    match oper:
        case 'add':
            result = a + b
        case 'sub':
            result = a - b
        case 'mul':
            result = a * b
        case 'div':
            result = a // b
        case _:
            print("InvalidOperator: Please enter valid operator 'add', 'sub', 'mul' or 'div'.")

    return result


def main():

    parser = ArgumentParser()

    parser.add_argument('--number1', type=int,
                        help="Enter the first number",
                        required=True)
    parser.add_argument('--number2', type=int,
                        help="Enter the second number",
                        required=True)
    parser.add_argument( '--operator', type=str,
                        choices={"add", "sub", "mul", "div"},
                        help="Enter the operator",
                        required=True)
    
    args_provided = parser.parse_args()

    res = simple_calculator(args_provided.number1, 
                            args_provided.number2, 
                            args_provided.operator)
    
    stdout.write(f"{str(res)}\n")


if __name__ == "__main__":

    main()
