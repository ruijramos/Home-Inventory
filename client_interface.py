from tkinter import *
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
from db_management import insert_form, delete_form, update_form, see_form

# Colors.
co0 = "#2e2d2b"   # Black
co1 = "#feffff"   # White
co2 = "#4fa882"   # Green
co3 = "#38576b"   # Value
co4 = "#403d3d"   # Letter
co5 = "#e06636"   # - Profit
co6 = "#038cfc"   # Blue
co7 = "#3fbfb9"   # Green
co8 = "#263238"   # + Green
co9 = "#e9edf5"   # + Green


# Create window.
window = Tk ()
window.title ("")
window.geometry('900x550')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)
style = ttk.Style(window)
style.theme_use("clam")


# Frames to slipt window in different sections.
upFrame = Frame(window, width=1043, height=50, bg=co1, relief="flat")
upFrame.grid(row=0, column=0)
middleFrame = Frame(window, width=1043, height=270,bg=co1, pady=20, relief="flat")
middleFrame.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)
rightFrame = Frame(window, width=1043, height=480,bg=co1, relief="flat")
rightFrame.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


# Insert app logo.
app_img  = Image.open('images/app_logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(upFrame, image=app_img, text=" Home Inventory", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)


global tree

# Insert function.
def insert():

    name = box_name.get()
    local = box_local.get()
    description = box_description.get()
    brand = box_brand.get()
    date = box_date.get()
    price = box_price.get()
    serie_id = box_serie_id.get()
    insert_list = [name, local, description, brand, date, price, serie_id]

    for i in insert_list:
        if i=='':
            messagebox.showerror('Error', 'Fill all spaces.')
            return

    insert_form(insert_list)
    messagebox.showinfo('Success', 'Data was successfully inserted.')

    box_name.delete(0, 'end')
    box_local.delete(0, 'end')
    box_description.delete(0, 'end')
    box_brand.delete(0, 'end')
    box_date.delete(0, 'end')
    box_price.delete(0, 'end')
    box_serie_id.delete(0, 'end')

    for widget in rightFrame.winfo_children():
        widget.destroy()

    populate_table()

# Update function.
def update():

    try:
        treev_data = tree.focus()
        treev_dic = tree.item(treev_data)
        treev_list = treev_dic['values']
        value = treev_list[0]

        box_name.delete(0, 'end')
        box_local.delete(0, 'end')
        box_description.delete(0, 'end')
        box_brand.delete(0, 'end')
        box_date.delete(0, 'end')
        box_price.delete(0, 'end')
        box_serie_id.delete(0, 'end')

        id = int(treev_list[0])
        box_name.insert(0, treev_list[1])
        box_local.insert(0, treev_list[2])
        box_description.insert(0, treev_list[3])
        box_brand.insert(0, treev_list[4])
        box_date.insert(0, treev_list[5])
        box_price.insert(0, treev_list[6])
        box_serie_id.insert(0, treev_list[7])

        def update_db():

            name = box_name.get()
            local = box_local.get()
            description = box_description.get()
            brand = box_brand.get()
            date = box_date.get()
            price = box_price.get()
            serie_id = box_serie_id.get()

            update_list = [name, local, description, brand, date, price, serie_id, id]

            for i in update_list:
                if i=='':
                    messagebox.showerror('Error', 'Fill all spaces.')
                    return

            update_form(update_list)
            messagebox.showinfo('Success', 'Data was successfully inserted.')

            box_name.delete(0, 'end')
            box_local.delete(0, 'end')
            box_description.delete(0, 'end')
            box_brand.delete(0, 'end')
            box_date.delete(0, 'end')
            box_price.delete(0, 'end')
            box_serie_id.delete(0, 'end')
          
            confirm_button.destroy()

            for widget in rightFrame.winfo_children():
                widget.destroy()

            populate_table()

        confirm_button = Button(middleFrame, command=update_db, text="Confirm".upper(), width=13, height=1, bg=co2, fg=co1,font=('ivy 8 bold'),relief=RAISED, overrelief=RIDGE)
        confirm_button.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Error', 'Select one item from the table.')

# Delete function.
def delete():

    try:
        treev_data = tree.focus()
        treev_dic = tree.item(treev_data)
        treev_list = treev_dic['values']
        value = treev_list[0]

        delete_form([value])
        messagebox.showinfo('Sucess', 'Data was successfully deleted.')

        for widget in rightFrame.winfo_children():
            widget.destroy()

        populate_table()

    except IndexError:
        messagebox.showerror('Error', 'Select one item from the table.')


# Create form.
text_name = Label(middleFrame, text="Name:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_name.place(x=10, y=10)
box_name = Entry(middleFrame, width=30, justify='left',relief="solid")
box_name.place(x=130, y=11)

text_local = Label(middleFrame, text="Room:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_local.place(x=10, y=40)
box_local = Entry(middleFrame, width=30, justify='left',relief="solid")
box_local.place(x=130, y=41)

text_description = Label(middleFrame, text="Description:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_description.place(x=10, y=70)
box_description = Entry(middleFrame, width=30, justify='left',relief="solid")
box_description.place(x=130, y=71)

text_brand = Label(middleFrame, text="Brand/Model", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_brand.place(x=10, y=100)
box_brand = Entry(middleFrame, width=30, justify='left',relief="solid")
box_brand.place(x=130, y=101)

text_date = Label(middleFrame, text="Purchase date:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_date.place(x=10, y=130)
box_date = DateEntry(middleFrame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
box_date.place(x=130, y=131)

text_price = Label(middleFrame, text="Purchase price:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_price.place(x=10, y=160)
box_price = Entry(middleFrame, width=30, justify='left',relief="solid")
box_price.place(x=130, y=161)

text_serie_id = Label(middleFrame, text="Serial number:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_serie_id.place(x=10, y=190)
box_serie_id = Entry(middleFrame, width=30, justify='left',relief="solid")
box_serie_id.place(x=130, y=191)


# Create buttons to communicate with the database

# Insert button.
img_add  = Image.open('images/add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)
insert_button = Button(middleFrame, image=img_add, command=insert, compound=LEFT, anchor=NW, text="   Add".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
insert_button.place(x=330, y=10)

# Update button.
img_update  = Image.open('images/update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)
update_button = Button(middleFrame, image=img_update, command=update, compound=LEFT, anchor=NW, text="   Update".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
update_button.place(x=330, y=50)

# Delete button.
img_delete  = Image.open('images/delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
delete_button = Button(middleFrame, image=img_delete, command=delete, compound=LEFT, anchor=NW, text="   Delete".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
delete_button.place(x=330, y=90)

# Total value label.
text_total_value = Label(middleFrame, text="Total value spent:", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
text_total_value.place(x=470, y=10)
box_total_value = Label(middleFrame, width=10, height=1,anchor=CENTER, font=('Ivy 10 bold'), bg=co7, fg=co1, relief=FLAT)
box_total_value.place(x=600, y=10)


# Function to display DB items in the interface table.
def populate_table():

    global tree

    # Creating a treeview with dual scrollbars.
    table_head = ['ID', 'Name', 'Room', 'Description', 'Brand', 'Purchase Date', 'Purchase Price', 'Serial Number']

    tree = ttk.Treeview(rightFrame, selectmode="extended", columns=table_head, show="headings")

    # Vertical scrollbar.
    vsb = ttk.Scrollbar(rightFrame, orient="vertical", command=tree.yview)
    # Horizontal scrollbar.
    hsb = ttk.Scrollbar(rightFrame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    rightFrame.grid_rowconfigure(0, weight=28)

    hd = ["center", "center", "center", "center", "center", "center", "center", 'center']
    h  = [40, 150, 100, 160, 130, 100, 100, 100]
    n  = 0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # Adjust column's width to the header string.
        tree.column(col, width=h[n],anchor=hd[n])
        n += 1

    # Get values from database.
    items_list = see_form()
    for item in items_list:
        tree.insert('', 'end', values=item)

    quantity = []
    for item in items_list:
        quantity.append(item[6])
    total_value = sum(quantity)
    box_total_value['text'] = '{:,.2f} €'.format(total_value) 

populate_table()

window.mainloop()
