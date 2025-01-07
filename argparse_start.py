import sys
import argparse

def sys_argv_parse():
    try:
        input_number1 = int(sys.argv[1])
        input_number2 = int(sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} number1 number2")
    else: 
        output_number = input_number1 * input_number2
        print(f"{input_number1} * {input_number2} = {output_number}")

def use_argparse():
    parser = argparse.ArgumentParser()

    # positional arguments
    parser.add_argument('methed', type=str, help='Method')
 
    # optional arguments
    parser.add_argument('-num1', '--number1', type=int, default=0, help='Operator1')
    parser.add_argument('-num2', '--number2', type=int, default=0, help='Operator2')

    parser.add_argument('--verbose', action='store_true', help='Print Message')

    args = parser.parse_args()

    output_number = args.number1 * args.number2
    if not args.verbose:
        print(f"{args.number1} * {args.number2} = {output_number}")

if __name__ == "__main__":
    use_argparse()