#!/usr/bin/env python3

import sys
import time

args = sys.argv
print(args)
input_file_path = args[1]
output_file_path = args[2]
count = 0

with open(input_file_path, 'r') as input_file:
    with open(output_file_path, 'a+') as output_file:

        for line in input_file:
            output_file.write(line)
            count += 1
            time.sleep(0.0001)
            if count % 10000 == 0:
                print("Processed %s lines" % (count,))

print("Finished.")


