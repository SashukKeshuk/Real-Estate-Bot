from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from db import *

root = Tk()

def post():
	text = textInput.get("1.0", END)
	text2 = textInput2.get("1.0", END)
	houseT = houseType.get()
	house = Type.get()
	cost = Cost.get()
	rooms = roomInput.get()
	city = City.get()
	s = "INSERT INTO `articles` (text, cost, type, house_type, rooms, city, text2) VALUES ('" + text + "', " + cost + ", " + house + ", " + houseT + ", '" + rooms + "', '" + city + "', '" + text2 +  "');"
	s_get = "SELECT * FROM `articles` WHERE `text2` = '" + stt(text2) +"'"
	try:
		add_line(s)
		l = get_lines(s_get)
		ss = 'article with id ' + str(l[0]['id']) + ' was added'
		messagebox.showinfo(title='success', message=ss)
	except Exception as e:
		messagebox.showerror(title='failed', message='failed to edit db')
		print(e)

def update():
	text = textInput22.get("1.0", END)
	text2 = textInput21.get("1.0", END)
	houseT = houseType1.get()
	house = Type1.get()
	cost = Cost1.get()
	rooms = roomInput1.get()
	city = City1.get()
	id3 = Id.get()
	print(house)
	s = "UPDATE `articles` SET text='" + text + "', text2='" + text2 + "', house_type=" + str(houseT) + ", rooms='" + rooms + "', city='" + city + "', type=" + str(house) + " WHERE id=" + str(id3)
	try:
		del_line(s)
		messagebox.showinfo('success', 'successfully edited')
	except Exception as e:
		messagebox.showerror('error', 'failed to edit...')
		print('failed to edit')
		print(e)

def paste1():
	data = pyperclip.paste()
	textInput.insert("1.0", data)
def paste2():
	data = pyperclip.paste()
	textInput2.insert("1.0", data)
def paste3():
	data = pyperclip.paste()
	textInput22.insert("1.0", data)
def paste4():
	data = pyperclip.paste()
	textInput21.insert("1.0", data)

def delete():
	id2 = Id2.get()
	q = "DELETE FROM `articles` WHERE id=" + str(id2)
	s = messagebox.askokcancel('are you sure?', 'are you sure?')
	if (s == True):
		try:
			del_line(q)
			messagebox.showinfo('success','successfully deleted')
		except Exception as e:
			messagebox.showerror('error', 'failed to delete...')
			print('failed to delete')
			print(e)

root['bg'] = '#000'
root.title('admin panel')
root.geometry('1300x800')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=1300, width=800)
canvas.pack()
container = ttk.Frame(root)

frame = Frame(root, bg='#000', highlightbackground="red", highlightthickness=2)
frame.place(relx=0, rely=0, relwidth=0.333, relheight=1)
frame1 = Frame(root, bg='#000', highlightbackground="red", highlightthickness=2)
frame1.place(relx=0.333, rely=0, relwidth=0.333, relheight=1)
frame2 = Frame(root, bg='#000', highlightbackground="red", highlightthickness=2)
frame2.place(relx=0.666, rely=0, relwidth=0.333, relheight=1)


title = Label(frame, text='add article', bg='#000', fg='#fff', font=35)
title.pack(pady=10)

label1 = Label(frame, text='short description', bg='#000', fg='#fff', font=20)
label1.pack()
textInput = Text(frame, bg='#000', fg='#fff', width='60', height='13')
textInput.pack()
Paste1 = Button(frame, text='paste', bg='#000', fg='#fff', command=paste1)
Paste1.pack()
label2 = Label(frame, text='full description', bg='#000', fg='#fff', font=20)
label2.pack()
textInput2 = Text(frame, bg='#000', fg='#fff', width='60', height='13')
textInput2.pack()
Paste2 = Button(frame, text='paste', bg='#000', fg='#fff', command=paste2)
Paste2.pack()

roomInput = Entry(frame, bg='#000', fg='#fff')
roomInput.pack(pady=8)
roomInput.insert(0, 'rooms')
houseType = Entry(frame, bg='#000', fg='#fff')
houseType.pack(pady=8)
houseType.insert(0, 'housetype (townhouse = 2, villa - 1, aports - 0)')
Cost = Entry(frame, bg='#000', fg='#fff')
Cost.pack(pady=8)
Cost.insert(0, 'cost')
Type = Entry(frame, bg='#000', fg='#fff')
Type.pack(pady=8)
Type.insert(0, 'type (from ? - 0, from arend - 1)')
City = Entry(frame, bg='#000', fg='#fff')
City.pack(pady=8)
City.insert(0, 'city')


btn = Button(frame, text='submit', bg='#000', fg='#fff', command=post)
btn.pack(pady=8)






title = Label(frame1, text='edit article', bg='#000', fg='#fff', font=35)
title.pack(pady=5)

Id = Entry(frame1, bg='#000', fg='#fff')
Id.pack(pady=4)
Id.insert(0, 'id')

label1 = Label(frame1, text='short description', bg='#000', fg='#fff', font=20)
label1.pack()
textInput22 = Text(frame1, bg='#000', fg='#fff', width='60', height='12', cursor='cross white')
textInput22.pack()
Paste3 = Button(frame1, text='paste', bg='#000', fg='#fff', command=paste3)
Paste3.pack()

label2 = Label(frame1, text='full description', bg='#000', fg='#fff', font=20)
label2.pack()
textInput21 = Text(frame1, bg='#000', fg='#fff', width='60', height='13', cursor='cross white')
textInput21.pack()
Paste4 = Button(frame1, text='paste', bg='#000', fg='#fff', command=paste4)
Paste4.pack()

roomInput1 = Entry(frame1, bg='#000', fg='#fff')
roomInput1.pack(pady=8)
roomInput1.insert(0, 'rooms')
houseType1 = Entry(frame1, bg='#000', fg='#fff')
houseType1.pack(pady=8)
houseType1.insert(0, 'housetype (townhouse = 2, villa - 1, aports - 0)')
Cost1 = Entry(frame1, bg='#000', fg='#fff')
Cost1.pack(pady=8)
Cost1.insert(0, 'cost')
Type1 = Entry(frame1, bg='#000', fg='#fff')
Type1.pack(pady=8)
Type1.insert(0, 'type (from ? - 0, from arend - 1)')
City1 = Entry(frame1, bg='#000', fg='#fff')
City1.pack(pady=8)
City1.insert(0, 'city')


btn1 = Button(frame1, text='submit', bg='#000', fg='#fff', command=update)
btn1.pack(pady=8)








title = Label(frame2, text='delete article', bg='#000', fg='#fff', font=35)
title.pack(pady=10)

Id2 = Entry(frame2, bg='#000', fg='#fff')
Id2.pack(pady=10)
Id2.insert(0, 'id')


btn3 = Button(frame2, text='submit', bg='#000', fg='#fff', command=delete)
btn3.pack(pady=8)






root.mainloop()