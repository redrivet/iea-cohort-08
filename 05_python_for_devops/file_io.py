# in_file_name = input('Please enter an input filename... ')
in_file_name = "poem.txt"
# out_file_name = input('Please enter an output filename... ')
out_file_name = "out_file.txt"

# Original Working Blocks
# with open(in_file_name, 'r') as f_in:
#     input_file = f_in.readlines()
#     input_file.reverse()

#     with open(out_file_name, 'w') as f_out:
#         output_file = f_out.writelines(input_file)


# Merged into single with block
# with open(in_file_name, 'r') as f_in, open (out_file_name, 'w') as f_out:
#     input_file = f_in.readlines()
#     input_file.reverse()
#     f_out.writelines(input_file)
#     f_out.close()

# EVEN SHORTER, PYTHONIC FTW
with open(in_file_name, "r") as f_in, open(out_file_name, "w") as f_out:
    f_out.writelines(reversed(f_in.readlines()))
