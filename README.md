# brnfck
A compressed [brainfuck](https://esolangs.org/wiki/Brainfuck) interpreter for use in code golf.

## How?
1. Each command in the program is converted to a respective octal digit.
2. This octal is padded with enough of the `[` digit to represent a hex number with an even number of digits. The `[` characters can just be removed later, as an `[` will never be at the end of a program.
3. This hex is the new data and is read from or written to a file.

# How to use
To encode a standard brainfuck file:

`python brnfck.py encode infile.bf outfile.bk`

The brnfck interpreter comes with a lot of different options to choose from, but to execute a file with the default settings invoke:

`python brnfuck.py interpret file.bk`

## Arguments
flag | meaning
- | -
`[-i | --user-input] USER_INPUT` | the input for the program
`[-u | --upper] UPPER` | the upper bound for the value the cells can hold; default is unbounded
`[-l | --lower] LOWER` | the lower bound for the value the cells can hold; default is unbounded (negatively)
`[-d | --default] DEFAULT` | the default value that cells hold; `0` by default
`[-e | --eof] EOF` | the value to use when no more input can be taken
`[-w | --non-wrapping]` | disables the wrapping of data values in cells
`[-c | --non-encoded]` | interprets a non-encoded file

# Effectiveness
Please let me know of any other programs / dialects that I can compare here
## Comparison
### Cat - 5 bytes
`.[.,]`

language | bytes output
- | -
brnfck | 2
CompressedFuck | 4

### Hello, World! - 72 bytes
`+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+.`

language | bytes output
- | -
brnfck | 40
CompressedFck | 42

### Sierpinski Triangle - 211 bytes
`>++++[<++++++++>-]>++++++++[>++++<-]>>++>>>+>>>+<<<<<<<<<<[-[->+<]>[-<+>>>.<<]>>>[[->++++++++[>++++<-]>.<<[->+<]+>[->++++++++++<<+>]>.[-]>]]+<<<[-[->+<]+>[-<+>>>-[->+<]++>[-<->]<<<]<<<<]++++++++++.+++.[-]<]+++++`

language | bytes output
- | -
brnfck | 79
CompressedFck | 108

# Contributing
Please feel free to contribute to this project (create issues/fixes etc.) especially if you can compress the files more.