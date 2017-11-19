from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import os
import sys, getopt
def convert1(pdfdic, rtfdic):
    if pdfdic == "" : pdfdic = os.getcwd() + "\\"
    for pdf in os.listdir(pdfdic):
        file1 = pfd.split(".")[-1]
        if file1 == "pdf":
            pdffile = pdfdic + pdf
            text = convert(pdffile)
            textfilename = rtfdic + pdf + ".rft"
            textfile = open(textfilename, "w")
            textfile.write(text)
pdfdic = "tailieu.pdf"
rtfdic = "convertPDF.rtf"
convert1(pdfdic, rtfdic)
