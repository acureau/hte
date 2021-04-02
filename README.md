# HTML TEMPLATE EDITOR
HTE is a python script for creating HTML templates, which can be modified and output with user input.
Core features include the following.

  - HTML Template Configs (Designed for sharing.)
  - Input Mutators. Generate random characters, evaluate an expression, and format as currency. Filled labels are accessable from input.
  - Multiple Output Formats.

## Usage
To get started, run the following in the 'hte' directory.

    python hte.py help

__List of Commands__

        help - Display this menu.

        list - Display existing templates.

        gen - Generate HTML from a template.
            Options:
            name - Name of the template. (REQUIRED)
            -d dir - The output directory. (OPTIONAL)
            -o format - The output format. (OPTIONAL)
                (png, html, pdf)

        test - Test a template for misconfigurations, and pre-filled labels.
            Options:
            name - Name of the template. (REQUIRED)

        new - Create a new empty template.
            Options:
            name - Name of the template. (REQUIRED)

        clone - Clones the template speficied.
            Options:
            name - Name of the template. (REQUIRED)

        del - Delete a template.
            Options:
            name - Name of the template. (REQUIRED)


        Input Mutators (OPTIONAL)
        ---------------
        (To be put before a input of your desired label.)
        Ex.
            Money: [$][M]5/2 -> 2.50

        [M] - Compute an expression.
        [$] - Output as a dollar amount.
        [#] - Replace character with random digit 0-9.
        [L] - Replace character with random uppercase letter.
        [l] - Replace character with random lowercase letter.
        [*] - Access a previous label from another. If 'F' = 0, [*F] = 0.


        Misc Info
        ---------
         - Prefilled labels are displayed as '(content)' after the label,
           pressing enter will use this value. Or you can choose not to.
        
## Configs
Configs must be named and structured very precisely. A new directory __name__ should be created in __./templates__ and inside of it two files placed, '__name__.html' and '__name__.config'. The easiest way to do this is by using the _new_ command.
 
    python hte.py new name
    
Now navigate to __./templates/name__ and open both files in your chosen editor. Insert your HTML into the generated HTML file. In the config file we will begin writing our input fields. 

Each line will contain a minimum of two arguments. The first is the label followed by the separator ':' and the placeholder. The label is the field that will be shown to the user when being asked for input. The argument separator is the character that is used to determine which part of the line corresponds to which argument. This will always be ':'. There is currently no way to change the argument separator short of modifying the source. The placeholder is the string in the HTML template which will be replaced with user input.

    example
    |
    |    _example.html-
    |
    |       <p>You Typed: (PLACEHOLDER)</p>
    |
    |   _example.config-
    |
    |        Label:(PLACEHOLDER)
 
__Multiple Inputs__  
The input separator is ','. New lines via '\n' are supported, so you are free to categorize your inputs.

    _example.config-

         Label:(PLACEHOLDER),
         LabelTwo:(YOUGETIT)
         
__Specified Input__  
If you'd like to specify an input field, you can do so with the '|' key. This is a flag that the input will be pre-filled, and whatever is typed after it will be used as input. Mutators can be used.

    _example.config-

         Label:(PLACEHOLDER),
         LabelTwo:(YOUGETIT),
         LabelThree:(PHONE)|([#][#][#]) [#][#][#][#]-[#][#][#][#]
