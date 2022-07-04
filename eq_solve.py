#!/usr/bin/python3
import sys
import argparse 

def arg_parse_foo():
    linear_parse=argparse.ArgumentParser(description="this script takes a file\
            as an argument from command line in which in ideal shold be an\
            linear equality and creates another file containing the solutionn\
            of the given equality and as a feedback compares the got solution\
            with right solution")
    linear_parse.add_argument('-f', "--file", required = True)
    arguments = linear_parse.parse_args()
    return arguments.file

def read_from_file():
    try:
        with open(arg_parse_foo()) as my_file:
            equat_str = my_file.read()
        return equat_str
    except :
        print("File not exist")
        sys.exit()

def test_the_solution(arg_num_str):
    try:
        with open("golden.txt") as golden_num_f:
            golden_num_str = golden_num_f.read()
        if float(arg_num_str) == float(golden_num_str):
            print(f"{float(arg_num_str)} solution is right!\n")
        else:
            print(f"solution is wroong!!!  should be {golden_num_str} \n")
    except IOError:
        print("Golden file not exist")
        sys.exit()

def solve(equation):
    try:
        s1 = equation.replace('x', 'j')
        s2 = s1.replace('=', '-(')
        s = s2+')'
        z = eval(s, {'j': 1j})
        real, imag = z.real, -z.imag
        if imag:
            return "%f" % (real/imag)
        else:
            if real:
                return "No solution"
            else:
                return "Infinite solutions"
    except TypeError:
        print ("File input is not correct")

def create_output_file(solution):
    solution_str = str(float(solution))
    with open('output.txt', 'w') as output_f:
        output_f.write(solution_str)


def main() -> None:
    try:
        equat_str = read_from_file()
        solution = solve(equat_str)
        test_the_solution(solution)
        create_output_file(solution)
    except TypeError:
        print("File arguments are not correct ")

if __name__ == '__main__':
    main()
