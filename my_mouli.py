#!/usr/bin/python3

from mouli_struct import *

def array_sort(array, order):
    sorted_array = []
    fatal = []
    major = []
    minor = []
    info = []
    if order == sortOrder.SEVERITY:
        for cel in array:
            if cel[Step.TYPE.value] == "FATAL":
                fatal.append(cel)
            if cel[Step.TYPE.value] == "MAJOR":
                major.append(cel)
            if cel[Step.TYPE.value] == "MINOR":
                minor.append(cel)
            if cel[Step.TYPE.value] == "INFO":
                info.append(cel)
    sorted_array = fatal + major + minor + info
    return sorted_array
                

def count_error(content):
    nb_error = [0, 0, 0, 0, 0]

    for cel in content:
        if cel[Step.TYPE.value] == "FATAL":
            nb_error[Severity.FATAL.value] += 1 
        if cel[Step.TYPE.value] == "MAJOR":
            nb_error[Severity.MAJOR.value] += 1 
        if cel[Step.TYPE.value] == "MINOR":
            nb_error[Severity.MINOR.value] += 1 
        if cel[Step.TYPE.value] == "INFO":
            nb_error[Severity.INFO.value] += 1 
        nb_error[Severity.ALL.value] += 1
    return nb_error

def read_file(file):
    fd = open(file, "r")
    content = fd.read()
    fd.close()
    return content

def parse_file(content):
    array = []
    cel = ["","","",""]
    index = 0
    for c in content:
        if c == ' ':
            continue
        if c == ':':
            index += 1
            continue
        if c == '\n':
            index = 0
            array.append(cel[::-1])
            cel = ["","","",""]
            continue
        cel[index] += c
    return array

def error_case():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print("Usage: ./my_mouli.py [line]\n\nOptions:\n\t-h\t\tShow this help message and exit\n\tline\t\tSort by line number\n\tseverity\tSort by severity [default]\n")
            exit(0)
        if len(sys.argv) == 1 or sys.argv[1] == "severity":
            sort_method = sortOrder.SEVERITY
        elif sys.argv[1] == "line":
            sort_method = sortOrder.LINE
        else:
            print("Usage: ./my_mouli.py [line]\n\nOptions:\n\t-h\t\tShow this help message and exit\n\tline\t\tSort by line number\n\tseverity\tSort by severity [default]\n")
            exit(84)
        return sort_method
    return sortOrder.SEVERITY

def get_desc(code):
    for cel in ERROR:
        if cel[0] == code:
            return cel[1]
    return "Unknown"

def display_all(array, nb_error, sort_method):
    print( Style.BRIGHT +"There are " + str(nb_error[Severity.ALL.value]) + " errors in total.    " + Fore.RED + str(nb_error[Severity.FATAL.value]) + " FATAL    " + Fore.LIGHTRED_EX + str(nb_error[Severity.MAJOR.value]) + " MAJOR    " + Fore.LIGHTYELLOW_EX + str(nb_error[Severity.MINOR.value]) + " MINOR    " + Fore.LIGHTCYAN_EX + str(nb_error[Severity.INFO.value]) + " INFO" + Style.RESET_ALL)
    step = [False, False, False, False]
    if sort_method == sortOrder.SEVERITY:
        for cel in array:
            if cel[Step.TYPE.value] == "FATAL" and step[Severity.FATAL.value] == False:
                print("\n" + Style.BRIGHT + Fore.RED + "FATAL:" + Style.RESET_ALL)
                step[Severity.FATAL.value] = True
            if cel[Step.TYPE.value] == "MAJOR" and step[Severity.MAJOR.value] == False:
                print("\n" + Style.BRIGHT + Fore.LIGHTRED_EX + "MAJOR:" + Style.RESET_ALL)
                step[Severity.MAJOR.value] = True
            if cel[Step.TYPE.value] == "MINOR" and step[Severity.MINOR.value] == False:
                print("\n" + Style.BRIGHT + Fore.LIGHTYELLOW_EX + "MINOR:" + Style.RESET_ALL)
                step[Severity.MINOR.value] = True
            if cel[Step.TYPE.value] == "INFO" and step[Severity.INFO.value] == False:
                print("\n" + Style.BRIGHT + Fore.LIGHTCYAN_EX + "INFO:" + Style.RESET_ALL)
                step[Severity.INFO.value] = True
            print("\t" + cel[Step.CODE.value] + " at " + Style.BRIGHT + cel[Step.LINE.value] + Style.RESET_ALL + " l in " + Style.BRIGHT + cel[Step.FILE.value].replace('./', '', 1) + Style.RESET_ALL + ": " + get_desc(cel[Step.CODE.value]))
    if sort_method == sortOrder.LINE:
        for cel in array:
            print("\t" + cel[Step.CODE.value] + " at " + Style.BRIGHT + cel[Step.LINE.value] + Style.RESET_ALL + " l in " + Style.BRIGHT + cel[Step.FILE.value].replace('./', '', 1) + Style.RESET_ALL + ": " + get_desc(cel[Step.CODE.value]))

                

def main():
    sort_method = error_case()
    content = read_file("/tmp/coding-style/coding-style-reports.log")
    array = parse_file(content)
    nb_error = count_error(array)
    sorted_array = array_sort(array, sort_method)
    display_all(sorted_array, nb_error, sort_method)

if __name__ == "__main__":
    main()