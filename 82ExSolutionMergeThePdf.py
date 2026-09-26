from PyPDF2 import PdfWriter
import os 

merger  = PdfWriter()
files = [file for file in os.listdir() if file.endswith('.pdf')]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
# #with this code the two pdf in the directory got merged
# # i think this will be always nice for me to write code

# from PyPDF2 import PdfWriter
# import os 

# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith('.pdf')]

# for pdf in files:
#     merger.append(pdf)

# merger.write("mergedPDFs")
# merger.close()