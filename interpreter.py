#mostly stolen from https://github.com/pocmo/Python-Brainfuck

import sys

def evaluate(code, upper=float("inf"), lower=float("-inf"), user_input="", default=0, eof=0, wrapping_cell=True, wrapping_tape=True):
    bracemap = build_bracemap(code)

    user_input = iter(user_input)
    
    array = [0]
    cellPointer = 0
    instructionPointer = 0

    while instructionPointer < len(code):
        command = code[instructionPointer]

        if command == ">":
            cellPointer += 1
            if cellPointer == len(array): array.append(default)

        elif command == "<":
            if cellPointer > 0:
                cellPointer -= 1
            else:
                array.insert(0, default)

        elif command == "+":
            array[cellPointer] = array[cellPointer] + 1 if array[cellPointer] < upper else lower if wrapping_cell else array[cellPointer]

        elif command == "-":
            array[cellPointer] = array[cellPointer] - 1 if array[cellPointer] > lower else upper if wrapping_cell else array[cellPointer]

        elif command == ".":
            print(chr(array[cellPointer]), end="")

        elif command == ",":
            array[cellPointer] = ord(next(user_input, chr(eof)))

        elif command == "[" and array[cellPointer] == 0:
            instructionPointer = bracemap[instructionPointer]

        elif command == "]" and array[cellPointer] != 0:
            instructionPointer = bracemap[instructionPointer]

        instructionPointer += 1

def build_bracemap(code):
    temp_stack = []
    bracemap = {}

    for position, command in enumerate(code):
        if command == "[":
            temp_stack.append(position)
        if command == "]":
            start = temp_stack.pop()
            bracemap[start] = position
            bracemap[position] = start
    
    return bracemap