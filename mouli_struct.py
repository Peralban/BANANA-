##
## EPITECH PROJECT, 2023
## banana
## File description:
## stuct.py
##

from enum import Enum
import sys
from colorama import Fore, Style

ERROR = [
    ["C-G10", "Inline assembly must never be used. Programming in C must be done. . . in C."],
    ["C-O1", "The repository must not contain compiled (.o, .a, .so, . . . ), temporary or unnecessary files"],
    ["C-O2", "Sources in a C program must only have .c or .h extensions."],
    ["C-O3", "Too many Functions, You must have 10 functions (including at most 5 non-static functions) per file."],
    ["C-G4", "Global variables must be avoided as much as possible. Only global constants should be used."],
    ["C-G5", "include directives must only include C header (.h) files."],
    ["C-F3", "The length of a line must not exceed 80 columns."],
    ["C-F4", "The body of a function should must not exceed 20 lines."],
    ["C-F5", "A function must not have more than 4 parameters."],
    ["C-F6", "A function taking no parameters must take void as a parameter in the function declaration."],
    ["C-F7", "Structures must be passed to functions using a pointer, not by copy."],
    ["C-F9", "Nested functions are not allowed."],
    ["C-L1", "CODE LINE CONTENT"],
    ["C-L5", "VARIABLE DECLARATIONS"],
    ["C-V2", "Do not create trash structures"],
    ["C-C1", "A conditionnal block (while, for, if, else, . . . ) must not contain more than 3 branches."],
    ["C-C2", "Ternary operators are allowed as far as there are kept simple and readable"],
    ["C-C3", "the goto keyword is forbidden."],
    ["C-H1", "Header file content"],
    ["C-H2", "Headers must be protected from double inclusion."],
    ["C-H3", "Macros must match only one statement, and fit on a single line."],
    ["C-O4", "The name of the file must define the logical entity it represents."],
    ["C-G1", "FILE HEADER"],
    ["C-G2", "functions must be separated by one and only one empty line."],
    ["C-G3", "The preprocessor directives must be indented according to the level of indirection."],
    ["C-G6", "Line endings must be done in UNIX style (with \n)."],
    ["C-G7", "No trailing spaces must be present at the end of a line."],
    ["C-G8", "No more than 1 trailing empty line must be present."],
    ["C-G9", "Non-trivial constant values should be defined either as a global constant or as a macro."],
    ["C-F1", "A function should only do one thing, not mix different levels of abstraction"],
    ["C-F2", "The name of a function must define the task it executes and must contain a verb."],
    ["C-F8", "There must be no comment within a function."],
    ["C-L2", "Each indentation level must be done by using 4 spaces."],
    ["C-L3", "One and only one space character must be used. Add just one to separate"],
    ["C-L4", "CURLY BRACKETS"],
    ["C-L6", "No blank lines. Except between variable and remainder of the function"],
    ["C-V1", "NAMING IDENTIFIERS"],
    ["C-V3", "POINTERS"],
    ["C-A1", "CONSTANT POINTERS"],
    ["C-A2", "Prefer the most accurate types possible according to the use of the data."],
    ["C-A3", "Files must end with a line break."],
    ["C-A4", "Global variables and functions that are not used outside his file should be a static."],
    ["O1", "The repository must not contain compiled (.o, .a, .so, . . . ), temporary or unnecessary files"],
    ["O2", "Sources in a Haskell program should only have extension .hs."],
    ["O3", "A Haskell project must be organised in modules, each of which should match a logical entity, and group all the functions and data structures associated with that entity. Every haskell file (including Main) should declare a module."],
    ["O4", "The name of a file should match the name of its module. Therefore, files and modules must be named in UpperCamelCase and in English."],
    ["O5", "All modules should explicitly declare their exported definitions. Except the Main module, all modules are expected to export at least one definition."],
    ["G1", "Every haskell file should start with a standard Epitech header:"],
    ["E1", "All language extensions are forbidden except if the project's subject says otherwise."],
    ["T1", "All top level bindings must have an accompanying type signature."],
    ["M1", "Mutable variables are strictly forbidden."],
    ["M2", "Functions performing unsafe operations are strictly forbidden. This forbids the use of all functions labeled as unsafe, such as unsafePerformIO"],
    ["F1", "A function should only do one thing, not mix the different levels of abstraction and respect the principle of single responsibility (a function must only be changed for one reason)."],
    ["F2", "The name of a function should define the task it executes and should contain a verb."],
    ["F3", "A Line must be less than 80 characters long."],
    ["F4", "A Function body must be 10 lines or less"],
    ["V1", "All identifier names should be in English, according to the lowerCamelCase convention"],
    ["C4", "Nested If statements are stricly forbidden."],
    ["C5", "Guards and if statements which can be expressed as pattern matchings must be expressed as such"],
    ["D1", "The Do notation is forbidden unless it contains a generator (a statement with a left arrow)."]
]

class Severity(Enum):
    FATAL = 0
    MAJOR = 1
    MINOR = 2
    INFO = 3
    ALL = 4

class sortOrder(Enum):
    LINE = 0
    SEVERITY = 1

class Step(Enum):
    CODE = 0
    TYPE = 1
    LINE = 2
    FILE = 3
