#!./venv/bin/python

import assembly

# Settings
index = 0
commands = ('obx', 'nl', 'lbx', 'sbx', 'ibx', 'dbx', 'if', 'jmp')

# Generate the code
def generate_code():
    pass

# Check if the code works with an example
def check_code():
    pass

# Display welcome information
print(input("Welcome to the Assembly Language Code Generator!\nPress enter to start!"))

# Generate code to the effect
while True:
    generate_code()

    
# Save the code in file
with open('program.asm', 'w') as f:
    f.write(code)

# Display information about the completion of the process
print("The code has been generated! Please refer to the \"program.asm\" file. If the code does not meet all requirements, please add more examples.")
