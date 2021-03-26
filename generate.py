import os
import random

# Collect properly structured templates.
def getTemplates():
    templates = []
    possibleTemplates = (os.listdir("./templates"))
    for template in possibleTemplates:
        if (os.path.exists("./templates/" + str(template) + "/" + str(template) + ".config") and os.path.exists("./templates/" + str(template) + "/" + str(template) + ".html") and len(os.listdir("./templates/" + template)) == 2):
            templates.append(template)
    return(templates)

# Edit the requested template.
def editTemplate(template):
    def modifiers(string):
        # Modifier Toggles
        money = False
        math = False
        numbers = False
        lowercase = False
        uppercase = False
        if ("[$]" in string):
            money = True
            string = string.replace("[$]", "")
        if ("[M]" in string):
            math = True
            string = string.replace("[M]", "")
        if ("[#]" in string):
            numbers = True
        if ("[L]" in string):
            uppercase = True
        if ("[l]" in string):
            lowercase = True
        
        # Apply Modifiers
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if (numbers):
            count = string.count("[#]")
            string = string.replace("[#]", "{}")
            string = string.format(*(random.randint(0, 9) for _ in range(count)))
        if (lowercase):
            count = string.count("[l]")
            string = string.replace("[l]", "{}")
            string = string.format(*(random.choice(letters) for _ in range(count)))
        if (uppercase):
            count = string.count("[L]")
            string = string.replace("[L]", "{}")
            string = string.format(*(random.choice(letters).upper() for _ in range(count)))
        if (math):
            try:
                string = str(eval(string))
            except:
                string = string
        if (money):
            try:
                string = ("{:.2f}".format(float(string)))
            except:
                string = string
        return(string)

    templates = getTemplates()
    if (template in templates):
        # Load template files.
        html = open("./templates/" + str(template) + "/" + str(template) + ".html", 'r').read()
        rawConfig = open("./templates/" + str(template) + "/" + str(template) + ".config", 'r').read()
        config = {}

        # Parsing the config file.
        fields = rawConfig.split(',\n')
        for field in fields:
            field = field.replace('\n', '')
        for field in fields:
            if(':' in field):
                keyPair = field.split(':')
                config[keyPair[0]] = keyPair[1]
        
        # Replacing the values in HTML string.
        for key in config:
            if ('|' in str(config[key])):
                userInput = config[key].split('|')[1]
                userInput = modifiers(str(userInput))
                html = html.replace(str(config[key].split('|')[0]), userInput)
                print(str(key) + ": " + userInput)
            else:
                userInput = input(str(key) + ": ")
                userInput = modifiers(str(userInput))
                html = html.replace(str(config[key]), userInput)
        
        return(html)
    else:
        return("Invalid Template.")

def newTemplate(name):
    templates = getTemplates()
    if (name in templates):
        return("Already Exists.")
    else:
        os.mkdir("./templates/" + str(name))
        html = open("./templates/" + str(name) + "/" + str(name) + ".html", 'w')
        config = open("./templates/" + str(name) + "/" + str(name) + ".config", 'w')
        html.close()
        config.close()
        return("Created.")

def deleteTemplate(name):
    templates = getTemplates()
    if (name in templates):
        os.remove("./templates/" + str(name) + "/" + str(name) + ".html")
        os.remove("./templates/" + str(name) + "/" + str(name) + ".config")
        os.rmdir("./templates/" + str(name))
        return("Deleted.")
    else:
        return("Does not Exist.")