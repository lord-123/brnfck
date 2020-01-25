import argparse
import interpreter
import encoder

def cleanup(code):
    return "".join(filter(lambda x: x in "><+-.,[]", code))

def interpret(args):
    with open(args.infile.name, args.infile.mode) as file:
        code = file.read()

    if args.non_encoded == False:
        code = encoder.decode(code.hex())
    else:
        code = cleanup(code.decode('cp1251'))

    arguments = {}

    if args.user_input != None:
        arguments["user_input"] = args.user_input

    if args.upper != None:
        arguments["upper"] = args.upper

    if args.lower != None:
        arguments["lower"] = args.lower

    if args.default != None:
        arguments["default"] = args.default

    if args.eof != None:
        arguments["eof"] = args.eof

    if args.non_wrapping == True:
        arguments["wrapping"] = False

    interpreter.evaluate(code, **arguments)

def encode(args):
    with open(args.infile.name, args.infile.mode) as file:
        code = cleanup(file.read())

    with open(args.outfile.name, args.outfile.mode) as file:
        data = encoder.encode(code)
        file.write(data)

def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=None)
    subparsers = parser.add_subparsers(help="sub-command help")

    interpret_parser = subparsers.add_parser("interpret", aliases=["i"], help="interpret help.")
    interpret_parser.add_argument("infile", type=argparse.FileType("rb"), help="The input file to be used.")
    interpret_parser.add_argument("-i", "--user-input", default="", help="The input for the program.")
    interpret_parser.add_argument("-u", "--upper", type=int, help="Maximum integer value to store in cell, default is 255.")
    interpret_parser.add_argument("-l", "--lower", type=int, help="Minimum integer value to store in cell, default is -255.")
    interpret_parser.add_argument("-d", "--default", type=int, help="The default starting value for cells to hold, default is 0.")
    interpret_parser.add_argument("-e", "--eof", type=int, help="The end-of-file to be used when there is no more input, defaults to not modifying the cell.")
    interpret_parser.add_argument("-w", "--non-wrapping", action="store_true", help="Disable wrapping of cells.")
    interpret_parser.add_argument("-c", "--non-encoded", action="store_true", help="Interpret non-encoded file.")
    interpret_parser.set_defaults(func=interpret)
    
    parser_encode = subparsers.add_parser("encode", aliases=["e"], help="encode help")
    parser_encode.add_argument("infile", type=argparse.FileType("r"), help="The file to encode.")
    parser_encode.add_argument("outfile", type=argparse.FileType("wb"), help="The outfile to write to.")
    parser_encode.set_defaults(func=encode)

    args = parser.parse_args()

    if args.func == None:
        parser.print_help()
        exit()

    args.func(args)

if __name__ == "__main__":
    main()