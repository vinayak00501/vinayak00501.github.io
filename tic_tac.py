from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.minsize(height=400, width=400)
root.maxsize(height=400, width=400)
root.configure(bg="#1A1A1A")

c = Canvas(root, bg="#1A1A1A", borderwidth=0)
c.place(x=0, y=0, width=400, height=400)

List = ["x", "o", "x", "o", "x", "o", "x", "o", "x", "o", "x", "o", "x"]

image = Image.open("blank.jpg")
photo_resize = image.resize((76, 76))
photo = ImageTk.PhotoImage(photo_resize)

o_image = Image.open("o_image_crop.png")
o_photo_resize = o_image.resize((76, 76))
o_photo = ImageTk.PhotoImage(o_photo_resize)

o_photo_small = o_image.resize((25, 25))
o_photo_small_photo = ImageTk.PhotoImage(o_photo_small)

cross_image = Image.open("cross_image_crop.png")
cross_photo_resize = cross_image.resize((76, 76))
cross_photo = ImageTk.PhotoImage(cross_photo_resize)

cross_photo_small = cross_image.resize((25, 25))
cross_photo_small_photo = ImageTk.PhotoImage(cross_photo_small)

neon_green_line = Image.open("neon_green_bg_removed.png")
neon_green_line_resize = neon_green_line.resize((360, 40))
neon_green_line_photo = ImageTk.PhotoImage(neon_green_line_resize)

neon_green_line_90 = Image.open("neon_green_bg_removed_90.png")
neon_green_line_90_resize = neon_green_line_90.resize((40, 360))
neon_green_line_90_photo = ImageTk.PhotoImage(neon_green_line_90_resize)

neon_green_line_45 = neon_green_line.rotate((45))
neon_green_line_45_photo = ImageTk.PhotoImage(neon_green_line_45)
neon_green_line_45.save("neon_45.png")

#c.create_rectangle((80, 80, 320, 320), fill="white")
c.create_line((160, 80, 160, 320), fill="white", width=4)
c.create_line((240, 80, 240, 320), fill="white", width=4)
c.create_line((80, 160, 320, 160), fill="white", width=4)
c.create_line((80, 240, 320, 240), fill="white", width=4)

btn_clr = "#1A1A1A"
b1 = Button(root, borderwidth=0, bg=btn_clr, image=photo, activebackground=btn_clr, command= lambda : btn_change(b1), state=NORMAL)
b2 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b2), state=NORMAL)
b3 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b3), state=NORMAL)
b4 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b4), state=NORMAL)
b5 = Button(root, borderwidth=0, bg=btn_clr, image=photo, activebackground=btn_clr, command= lambda : btn_change(b5), state=NORMAL)
b6 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b6), state=NORMAL)
b7 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b7), state=NORMAL)
b8 = Button(root, borderwidth=0, bg=btn_clr,              activebackground=btn_clr, command= lambda : btn_change(b8), state=NORMAL)
b9 = Button(root, borderwidth=0, bg=btn_clr, image=photo, activebackground=btn_clr, command= lambda : btn_change(b9), state=NORMAL)

b1.place(x=82, y=82, width=76, height=76)
b2.place(x=162, y=82, width=76, height=76)
b3.place(x=242, y=82, width=76, height=76)
b4.place(x=82, y=162, width=76, height=76)
b5.place(x=162, y=162, width=76, height=76)
b6.place(x=242, y=162, width=76, height=76)  
b7.place(x=82, y=242, width=76, height=76)
b8.place(x=162, y=242, width=76, height=76)
b9.place(x=242, y=242, width=76, height=76)

def btn_change(b):
    global List, b1, b2, b3, b4, b5, b6, b7, b8, b9
    global b1_var, b2_var, b3_var, b4_var, b5_var, b6_var, b7_var, b8_var, b9_var
    global count
    
    b["state"] = DISABLED
    if List[-1] == "x":
        b["image"] = cross_photo
        List.pop(-1)
        
        
    elif List[-1] == "o":
        b["image"] = o_photo
        List.pop(-1)

    def win_():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        b1["state"] = b2["state"] = b3["state"] = b4["state"] = b5["state"] = b6["state"] = b7["state"] = b8["state"] = b9["state"] = DISABLED
        Label(root, text = "Player won !", font = "Veranda 15 bold", bg=btn_clr, fg = "white").place(x=160, y=335, height=15)

        if List[-2] == "x":
            Label(root, image=cross_photo_small_photo, bg=btn_clr).place(x=125, y=328)
        elif List[-2] == "o" :
            Label(root, image=o_photo_small_photo, bg=btn_clr).place(x=125, y=328)
        
        def End_Game():
            root.quit()

        Button(root, text="End Game!", bg=btn_clr, fg="white", command=End_Game, borderwidth=0, activebackground=btn_clr, activeforeground="white").place(x=320, y=350)

    # 1 2 3
    if b1["state"] == DISABLED and b2["state"] == DISABLED and b3["state"] == DISABLED :
        if b1["image"] == b2["image"] == b3["image"] :
            Label(root, image=neon_green_line_photo, bg=btn_clr, borderwidth=0).place(x=10, y=120, height=4)
            win_()
            
    # 4 5 6
    if b4["state"] == DISABLED and b5["state"] == DISABLED and b6["state"] == DISABLED:
        if b4["image"] == b5["image"] == b6["image"] :
            Label(root, image=neon_green_line_photo, bg=btn_clr, borderwidth=0).place(x=10, y=202, height=4)
            win_()

    # 7 8 9
    if b7["state"] == DISABLED and b8["state"] == DISABLED and b9["state"] == DISABLED:
        if b7["image"] == b8["image"] == b9["image"] : 
            Label(root, image=neon_green_line_photo, bg=btn_clr, borderwidth=0).place(x=10, y=282, height=4)
            win_()
    
    # 1 4 7
    if b1["state"] == DISABLED and b4["state"] == DISABLED and b7["state"] == DISABLED:
        if b1["image"] == b4["image"] == b7["image"] : 
            Label(root, image = neon_green_line_90_photo, bg=btn_clr, borderwidth=0).place(x=120, y=10, width=6)
            win_()
 
    # 2 5 8
    if b2["state"] == DISABLED and b5["state"] == DISABLED and b8["state"] == DISABLED:
        if b2["image"] == b5["image"] == b8["image"] :
            Label(root, image=neon_green_line_90_photo, bg=btn_clr, borderwidth=0).place(x=200, y=10, width=6) 
            win_()
    
    # 3 6 9
    if b3["state"] == DISABLED and b6["state"] == DISABLED and b9["state"] == DISABLED:
        if b3["image"] == b6["image"] == b9["image"] :
            Label(root, image=neon_green_line_90_photo, bg=btn_clr, borderwidth=0).place(x=280, y=10, width=6) 
            win_()

    # 1 5 9 
    if b1["state"] == DISABLED and b5["state"] == DISABLED and b9["state"] == DISABLED:
        if b1["image"] == b5["image"] == b9["image"] :
            b1["image"] = b5["image"] = b9["image"] = None
            b1["bg"] = b5["bg"] = b9["bg"] = "#00FF00"
            win_()

    # 3 5 7
    if b3["state"] == DISABLED and b5["state"] == DISABLED and b7["state"] == DISABLED:
        if b3["image"] == b5["image"] == b7["image"] :
            b3["image"] = b5["image"] = b7["image"] = None
            b3["bg"] = b5["bg"] = b7["bg"] = "#00FF00"
            win_()
        

Label(root, image=cross_photo_small_photo, bg=btn_clr).place(x=125, y=20)
Label(root, text="Goes First !", font="Verdana 15 bold", bg=btn_clr, fg="white").place(x=160, y=20)


def info_command():
    messagebox.showinfo("About", "Tic Tac Toe made by Vinayak!")
info_image = Image.open("info white.png")
info_image_resize = info_image.resize((15, 15))
info_photo = ImageTk.PhotoImage(info_image_resize)
Button(root, image=info_photo, bg=btn_clr, borderwidth=0, command=info_command, activebackground=btn_clr).place(x=370, y=20, width=20, height=15)

root.mainloop()

'''
    if (b1["state"] == DISABLED and b2["state"] == DISABLED and b3["state"] == DISABLED) and b1["image"] == cross_image and b2["image"] == cross_image and b3["image"] == cross_image : 
        print("done")
        Label(root, image = neon_green_line_photo, bg=btn_clr, borderwidth=0).place(x=10, y=120, height=4)
    elif (b1["state"] == DISABLED and b2["state"] == DISABLED and b3["state"] == DISABLED) and ((b1["image"] == cross_photo and b4["image"] == cross_photo and b7["image"] == cross_photo) or (b1["image"] == o_photo and b4["image"] == o_photo and b7["image"] == o_photo)):
        Label(root, image = neon_green_line_90_photo, bg=btn_clr, borderwidth=0).place(x=120, y=10, width=6)
    '''