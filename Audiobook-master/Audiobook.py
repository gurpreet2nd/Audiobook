import pyttsx3
import PyPDF2
book = open('The monk who sold his ferrari.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
welcome = "Hello, I am your reader. I was made by Gurpreet Singh kochar. Today i am going to read The monk who sold his ferrari"
speaker = pyttsx3.init()
speaker.say(welcome)
page = pdfReader.getPage(0)
