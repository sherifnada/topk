import fileinput
import re
from itertools import islice

def pretty_print_first_n(sorted_dict, n):
   first_n = list(islice(final.items(), n)) 
   for el in first_n:
       print('"' + el[0] + '"', "used " + str(el[1]) + " times")

out = {}
# aggregate commands
for line in fileinput.input():
    split_line = re.split("\s+", line.strip().lstrip())[1:] #first item is line number
    for i in range(1, len(split_line)):
        command = " ".join(split_line[:i])
        if command not in out:
            out[command] = 0
        out[command] += 1

# sort by usage
final = {k:v for k, v in sorted(out.items(), key=lambda item:item[1], reverse=True)}

pretty_print_first_n(final,10)


