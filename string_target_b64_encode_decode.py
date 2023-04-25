import re
import sys
import base64


FILE = sys.argv[1]
CHAR = sys.argv[2]

def string_select(FILE, CHAR):

    with open(FILE, 'r') as logsfile:
        reader = logsfile.read()
        patern = CHAR

        i_target_charcounter = 500 #500 char for take all b64 value in the text, could change with html file value
        l_position_endpatern = []
        l_command_in_base64 = []
        l_temp = []

        for match in re.finditer(patern, reader):
            l_position_endpatern.append(match.end())

        for i in l_position_endpatern:
            l_temp.append(reader[i:(i+i_target_charcounter)])


        for y in l_temp:
            counter = 0

            for z in y:
                counter +=1
                if z == " ":
                    l_command_in_base64.append(y[0:counter])
                    break
        return l_command_in_base64


def decode_b64(data):
    base64_string = data
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    return sample_string



"""def encode_b64(data):           #not used in this script
    sample_string = data
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    print(f"Encoded string: {base64_string}")"""

def main():

    list_of_b64_value = string_select(FILE, CHAR)

    for i in list_of_b64_value:

        print(decode_b64(i))

main()
