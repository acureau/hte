import pdfkit
import imgkit

def output(directory, fileType, content):
    filename = str(input("File Name: "))
    if (fileType == "html"):
        outputFile = open(directory + "/" + filename + ".html", 'w')
        outputFile.write(content)
    elif (fileType == "pdf"):
        pdfkit.from_string(content, (directory + "/" + filename + ".pdf"), options={'quiet': ''})
    else: # png
        options = {
            'quiet': ''
        }
        imgkit.from_string(content, (directory + "/" + filename + ".png"), options=options)