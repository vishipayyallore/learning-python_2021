#!/usr/bin/env python3

def show_banner(value: str, times: int):
    print(value * times)


def show_strings_demo1():
    first_name = "Mohd"
    last_name = 'Azim'
    person_description = """
                        My Name is 
                        Mohd Azim
                        """
    show_banner('=', 50)
    print("Strings Demo 1")
    show_banner('=', 50)
    print(first_name)
    print(last_name)
    print(person_description)
    show_banner('-', 50)


def show_strings_demo2():
    first_name = "Mohd"
    last_name = 'Azim'
    person_description = """
                        My Name is 
                        Mohd Azim
                        """
    show_banner('=', 50)
    print("Strings Demo 2")
    show_banner('=', 50)
    print(first_name, last_name, person_description, sep='\n')
    show_banner('-', 50)


def show_strings_demo3():
    first = "First's"
    last = 'Last"s'

    show_banner('=', 50)
    print("Strings Demo 3")
    show_banner('=', 50)
    print(first, last)
    print(first + " " + last)
    print(f"Contains both Single and Double Quotes {first} {last}")
    show_banner('-', 50)


def main():
    show_strings_demo1()
    show_strings_demo2()
    show_strings_demo3()


# Program Execution Starts here
main()
