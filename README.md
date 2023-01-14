# Assembly-Language-Code-Generator
This is my own assembly code generator with interpreter. Its purpose is to generate code based on output examples.

This project is not finished. It has been made available so that someone can see it and try to help.

### More detailed explanation
The file named assembly.py is the language interpreter. It only has 9 instructions. (The code generator uses 8)

#### These are:
* **obx** - Prints the value of a variable to the screen
* **ostr** - Prints a string of characters to the screen
* **nl** - It prints a newline in the terminal because the *ostr* command does not have a newline function
* **lbx** - Loads a **_integer_** value given by the user into a variable
* **sbx** - Sets the value of a variable
* **ibx** - Increases the value of a variable
* **dbx** - Decrements the value of a variable
* **if** - Conditional statement
* **jmp** - Jumps to the selected instruction

It may be of interest to you that I refer to variables as boxes here. That's why it's *obx* and not ovr as you might expect. Additional information is the fact that **_boxes_** can only store numbers. Numbers range from -999999 to 999999.
