from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from pdf2image import convert_from_path

def pdf2ImgConverter():
    pass


def SourceFileName():
    entry.configure(state='normal')
    entry.delete(0, END)
    src = askopenfilename(
        title="Choose a File",
        filetypes=[('PDF Files', '.pdf')])
    entry.insert(0, src)
    entry.configure(state='disabled')


def DestinationFileName():
    srcDest = askdirectory()
    entrySave.insert(0, srcDest)


mainWindow = Tk()
mainWindow.title("PDF2IMG CONVERTER")
# mainWindow.geometry("400x500")
mainWindow.resizable(width=False, height=False)

titleHeading = Label(mainWindow, text="PDF2IMG CONVERTER", font=("New Times Roman", 20, "italic"))
titleHeading.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

label = Label(mainWindow, text="Choose File").grid(row=1, column=0)

entry = Entry(mainWindow, width=30)
# entry.configure(state='readonly')
entry.grid(row=1, column=1)

btnOpenFile = Button(mainWindow, text="Browse", command=lambda: SourceFileName())
btnOpenFile.grid(row=1, column=2)
# openFile = askopenfilename()

entrySave = Entry(mainWindow, width=30)
# entrySave.configure(state='readonly')
entrySave.grid(row=2, column=1)

btnDestination = Button(mainWindow, text="Browse", command=lambda: DestinationFileName())
btnDestination.grid(row=2, column=2)

btn = Button(mainWindow, text="CONVERT", command=pdf2ImgConverter, font=("New Times Roman", 12, "bold"))
btn.grid(row=3, column=1, padx=5, pady=5)

mainWindow.mainloop()


