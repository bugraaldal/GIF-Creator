import tkinter
from tkinter import filedialog
from PIL import Image
import os
# If there isn't a folder named GIF MAKER on the desktop, create one.
if not(os.path.isdir("/home/buura/Desktop/GIF MAKER")):
    os.mkdir("/home/buura/Desktop/GIF MAKER")

gif_index = 0  # Since we are going to loop the images of the gif, start the index from 0
to_convert = []  # A list to hold our images which we want to convert
# Walking through the files and counting them to name the gif properly
path, dirs, files = next(os.walk("/home/buura/Desktop/GIF MAKER"))
file_count = len(files)


class GIF_Related:
    def createGIF(self):
        global file_count
        global to_convert
        """ If there weren't any files selected and the user  just clicks to
          "Create a GIF with the added photos" button pop up a window and show 
         a message pointing to the problem"""
        if len(to_convert) == 0:
            empty_top = tkinter.Toplevel()
            empty_top.title("Error")  # Name the window "Error"
            # Show the "No files were selected." message
            no_file = tkinter.Label(
                empty_top, text="No files were selected.", font="none 24")
            no_file.pack()
            # Else, (if there are items in the list.)
        else:
            # Convert the items to GIF format -using Pillow (PIL) and save them to the "GIF MAKER" folder
            fp_out = f"/home/buura/Desktop/GIF MAKER/GIF{file_count+1}.gif"
            img, *imgs = [Image.open(f) for f in to_convert]
            img.save(fp=fp_out, format='GIF', append_images=imgs,
                     save_all=True, duration=300, loop=0)
            # Pop up a screen, showing the gif
            top = tkinter.Toplevel()
            top.title(F"GIF{file_count+1}.gif")
            photo = tkinter.PhotoImage(
                file=f"/home/buura/Desktop/GIF MAKER/GIF{file_count+1}.gif")

            def next_frame():
                global gif_index
                try:
                    photo.configure(format="gif -index {}".format(gif_index))
                    gif_index += 1
                except tkinter.TclError:
                    gif_index = 0
                    return next_frame()
                else:
                    top.after(300, next_frame)
            label = tkinter.Label(top, image=photo)
            label.pack()
            top.after_idle(next_frame)

    def addPhoto(self):  # The function that lets you choose files (images) and add them to the list
        global to_convert
        for widget in frame.winfo_children():
            widget.destroy()
        photo = filedialog.askopenfilename(initialdir="/home/", title="Select File",
                                           filetypes=(("png", "*.png"), ("jpg", "*.jpg"), ("ppm", "*.ppm"), ("all", "*.*")))
        to_convert.append(photo)
        for ph in to_convert:
            label = tkinter.Label(frame, text=ph, bg="gray")
            label.pack()


gif = GIF_Related()
root = tkinter.Tk()
# The main skeleton of the main window
root.title("GIF Maker")
TITLE = tkinter.Label(root, text="GIF MAKER", bg="Blue",
                      fg="white", font="none 12 bold")
TITLE.pack(side="top")
canvas = tkinter.Canvas(root, height=450, width=700, bg="Blue")
canvas.pack()
root.configure(background="blue")
frame = tkinter.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

createGIF_Button = tkinter.Button(root, text="Create a GIF with the added photos", height=1, width=1, padx=310,
                                  pady=5, fg="white", bg="DARK BLUE", command=gif.createGIF)
createGIF_Button.pack(side="bottom")
addPhoto_Button = tkinter.Button(root, text="Add Photos to create a gif", padx=310, height=1, width=1,
                                 pady=5, fg="white", bg="DARK BLUE", command=gif.addPhoto)
addPhoto_Button.pack(side="bottom")
root.mainloop()
