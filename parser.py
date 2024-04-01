import pypandoc


# Example file:
def parse:

	docxFilename = 'file.docx'
	outputFilename = 'index.html'
	output = pypandoc.convert_file(docxFilename, 'html', outputfile=outputFilename)
