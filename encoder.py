encode_dictionary = {
    ">": "0",
    "<": "1",
    "+": "2",
    "-": "3",
    ".": "4",
    ",": "5",
    "[": "6",
    "]": "7"
}

decode_dictionary = {
    "0": ">",
    "1": "<",
    "2": "+",
    "3": "-",
    "4": ".",
    "5": ",",
    "6": "[",
    "7": "]"
}

def encode(code):
    x = ""
    for i in code:
        try:
            x += encode_dictionary[i]
        except:
            raise ValueError("invalid bf code")

    while True:
        data = hex(int(x,8))[2:]
        if len(data) % 2 == 1:
            x+=encode_dictionary["["]
        else: break

    data = bytes.fromhex(data)

    return data

def decode(code):
    o = oct(int(code, 16))[2:]

    while True:
        if o.endswith(encode_dictionary["["]): o = o[:-1]
        else: break

    out = ""
    for i in o:
        out += decode_dictionary[i]

    return out

if __name__ == "__main__":
    with open("hello world.bf", "rb") as file:
        print(decode(file.read().hex()))