from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from pdf2image import convert_from_path


def pdf2img_converter():
    try:
        # convert_from_path will get the PDF file from the entry widget we created in GUI.
        imgs = convert_from_path(str(entry.get()))
        for i in range(len(imgs)):
            # Saves the images as JPEG File format using .save function
            imgs[i].save('page'+str(i)+'.jpg', 'JPEG')

    # If error or exception is found then it will show the error message box.
    except Exception as e:
        # Prints the exception in console.
        print(e)
        # Shows the result message box saying "No PDF Found"
        messagebox.showinfo("Result", "NO PDF Found")
    else:
        # else if no error found, then it show success message box.
        messagebox.showinfo("Result", "Converted to Image Successfully")


# Function which will browse for pdf file.
def source_filename():
    # configures the state of entry to normal
    entry.configure(state='normal')
    # clears the input in the entry
    entry.delete(0, END)
    # ask for file open with file types only PDF.
    src = askopenfilename(
        title="Choose a File",
        filetypes=[('PDF Files', '.pdf')])
    # Inserts the path of PDF file in the entry
    entry.insert(0, src)
    # again configures the state of entry to disabled.
    entry.configure(state='disabled')


# Creating GUI Window
mainWindow = Tk()
# Title for Window
mainWindow.title("PDF2IMG CONVERTER")
# This will prevent program window to resize.
mainWindow.resizable(width=False, height=False)

# Title Heading for Program Name
titleHeading = Label(mainWindow, text="PDF2IMG CONVERTER", font=("New Times Roman", 20, "italic"))
# .grid is used to place widgets in grid, column and row. We just have to mention row and column value.
titleHeading.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Label (Text) for Choosing File.
chooseFileLabel = Label(mainWindow, text="Choose File").grid(row=1, column=0)

# Entry widget is used to get input from user, in this case we will use it get the PDF file location.
entry = Entry(mainWindow, width=30)
entry.grid(row=1, column=1)

# Button widget for browsing the file explorer and locating file.
btnOpenFile = Button(mainWindow, text="Browse", command=lambda: source_filename())
btnOpenFile.grid(row=1, column=2)

# Button which will convert PDF to Image on click.
btnConvert = Button(mainWindow, text="CONVERT", command=pdf2img_converter, font=("New Times Roman", 12, "bold"))
btnConvert.grid(row=3, column=1, padx=5, pady=5)

# mainloop method is used when you program is ready to run.
# mainloop() is infinite loop which runs until program is not closed
mainWindow.mainloop()


