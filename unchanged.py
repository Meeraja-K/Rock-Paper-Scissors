import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
root=Tk()
root.title("Rock Paper Scissors Game")
root.geometry("2000x700")
root.config(bg="#588C7E")
heading=Label(root,text='Let\'s play Rock Paper Scissors', font='arial 40 bold',bg='#588C7E',fg='white').pack()
def thanks():
	ImageAddress = "resources/thanks.jpg"
	ImageItself = Image.open(ImageAddress)
	ImageNumpyFormat = np.asarray(ImageItself)
	plt.imshow(ImageNumpyFormat)
	plt.draw()
	plt.pause(2)
	plt.close()
	root.destroy()
def mycommand():
	win = Toplevel()
	win.title("Rock Paper Scissors")
	win.geometry("2000x700")
	win.config(bg="#588C7E")
	l = Label(win, text="Choose One : YOU vs ?", font='arial 40 bold',bg='#588C7E', fg='white').pack()
	def papery():
		wind=Toplevel()
		wind.title("Rock Paper Scissors")
		width=1000
		height=700
		window_width = wind.winfo_screenwidth()
		window_height = wind.winfo_screenheight()
		x = (window_width / 2) - (width / 2)
		y = (window_height / 2) - (height / 2)
		wind.geometry("%dx%d+%d+%d" % (width, height, x, y))
		wind.resizable(0, 0)
		wind.config(bg="#588C7E")
		p1=Label(wind, text= 'Player 1', bg='#588C7E', fg="white", font='arial 35 bold').grid(row=1, column=1)
		Label(wind, text="Enter any digit number").grid(row=3)
		Label(wind,text="Enter position").grid(row=4)
		e1=Entry(wind, width=40)
		e1.grid(row=3, column=1)
		e2=Entry(wind, width=40)
		e2.grid(row=4, column=1)
		p2=Label(wind, text= 'Player 2', bg='#588C7E', fg="white", font='arial 35 bold').grid(row=1, column=3)
		Label(wind, text="Enter any digit number").grid(row=3,column=3)
		Label(wind,text="Enter position").grid(row=4,column=3)
		e3=Entry(wind, width=40)
		e3.grid(row=3, column=4)
		e4=Entry(wind, width=40)
		e4.grid(row=4, column=4)
		p1_score=[]
		p2_score=[]
		def onClick():
			ran=Toplevel()
			ran.geometry("800x550")
			ran.config(background="#588C7E")
			gifImage= "resources/giphy.gif"
			openImage=Image.open(gifImage)
			frames=openImage.n_frames
			imageObject=[PhotoImage(file=gifImage, format=f"gif -index {i} ") for i in range(frames)]
			count=0
			showAnimation = None
			def animation(count):
				global showAnimation
				newImage=imageObject[count]
				gif_Label.configure(image=newImage)
				count+=1
				if count==frames:		
					count=0
				showAnimation=ran.after(100 ,lambda: animation(count))
			gif_Label=Label(ran, image="")
			gif_Label.place(x=155, y=20, width=450, height=500)
			animation(count)
			def messi():
				k1=e1.get()
				k2=int(e2.get())
				k3=e3.get()
				k4=int(e4.get())
				def rock_paper_scissors(k1,k3,k2,k4):
					p5=int(k1[k2])%3
					p6=int(k3[k4])%3
					if (player_one[p5]==player_two[p6]):
						messagebox.showinfo("Note","Its a draw")
					elif(player_one[p5]=="Rock" and player_two[p6]=="Scissor"):
						messagebox.showinfo("Congratulations","Player 1, you chose Rock ✊. You won!")
						p1_score.append(1)
					elif(player_one[p5]=="Rock" and player_two[p6]=="Paper"):
						messagebox.showinfo("Congratulations","Player 2, you chose Paper 🖐️. You won!")
						p2_score.append(1)
					elif(player_one[p5]=="Paper" and player_two[p6]=="Scissors"):
						messagebox.showinfo("Congratulations","Player 2, you chose Scissors ✌️. You won!")
						p2_score.append(1)
					elif(player_one[p5]=="Paper" and player_two[p6]=="Rock"):
						messagebox.showinfo("Congratulations","Player 1, you chose Paper 🖐️. You won!")
						p1_score.append(1)
					elif(player_one[p5]=="Scissors" and player_two[p6]=="Rock"):
						messagebox.showinfo("Congratulations","Player 2, you chose Rock ✊. You won!")
						p2_score.append(1)
					elif(player_one[p5]=="Scissors" and player_two[p6]=="Paper"):
						messagebox.showinfo("Congratulations","Player 1, you chose Scissors ✌️. You won!")
						p1_score.append(1)
				player_one={0:"Rock", 1:"Paper", 2:"Scissors"}
				player_two={0:"Paper",1:"Rock", 2:"Scissors"}
				rock_paper_scissors(k1,k3,k2,k4)
				ran.destroy()
			buy=Button(ran, text="Show who won", bg="pink", fg="red", font='arial 15 bold', command=messi).pack(side=BOTTOM)
		bt1=Button(wind, text="Enter", bg="red", fg="white", font='arial 15 bold', command=onClick).grid(row=15,column=2)
		def score():
			class Table:
				def __init__(self,root):
					for i in range(total_rows):
						for j in range(total_columns):
							self.e = Entry(h, width=20, fg='#588C7E', font='Arial 16 italic')
							self.e.grid(row=i, column=j)
							self.e.insert(END, lst[i][j])
			lst = [('PLAYER','SCORE'),('Player 1',len(p1_score)), ('Player 2',len(p2_score))]
			total_rows = len(lst)
			total_columns = len(lst[0])
			h=Toplevel()
			t = Table(h)	
		  
		bang=Button(wind, text="Scoreboard", bg="pink", fg="white", font='arial 15 bold', command=score).grid(row=15, column=1)	
		b_exit = Button(wind, text="Exit", bg="yellow", fg="white", font='arial 15 bold', command=thanks).grid(row=15, column=4)
		def reset():
			e1.delete(0, END)
			e2.delete(0, END)
			e3.delete(0, END)
			e4.delete(0, END)
		b_r = Button(wind, text="Reset", bg="orange", fg="white", font='arial 15 bold', command=reset).grid(row=15, column=3)
		
	Girl = PhotoImage(file="resources/Girl.png")
	but=Button(win, image=Girl, command=papery)
	but.pack(padx=150, pady=1, side=LEFT)
	def hey():
		see = Toplevel()
		see.title("Rock, Paper, Scissors ")
		width = 650
		height = 580
		window_width = see.winfo_screenwidth()
		window_height = see.winfo_screenheight()
		x = (window_width / 2) - (width / 2)
		y = (window_height / 2) - (height / 2)
		see.geometry("%dx%d+%d+%d" % (width, height, x, y))
		see.resizable(0, 0)
		see.config(bg="#588C7E")
		Blank_img = PhotoImage(file="resources/blank.png")
		Player_Rock = PhotoImage(file="resources/rock_player.png")
		Player_Rock_ado = Player_Rock.subsample(2, 2)
		Player_Paper = PhotoImage(file="resources/paper_player.png")
		Player_Paper_ado = Player_Paper.subsample(2, 2)
		Player_Scissor = PhotoImage(file="resources/scissor_player.png")
		Player_Scissor_ado = Player_Scissor.subsample(2, 2)
		Computer_Rock = PhotoImage(file="resources/rock_computer.png")
		Computer_Paper = PhotoImage(file="resources/paper_computer.png")
		Computer_Scissor = PhotoImage(file="resources/scissor_computer.png")
		c_score=[]
		p_score=[]
		def Rock():
			global player_option
			player_option = 1
			Image_Player.configure(image=Player_Rock)
			Matching() 
		def Paper():
			global player_option
			player_option = 2
			Image_Player.configure(image=Player_Paper)
			Matching() 
		def Scissor():
			global player_option
			player_option = 3
			Image_Player.configure(image=Player_Scissor)
			Matching()
		def Comp_Rock():
			if player_option == 1:
				Label_Status.config(text="Game Tie")
			elif player_option == 2:
				Label_Status.config(text="Player Win")
				p_score.append(1)
			elif player_option == 3:
				Label_Status.config(text="Computer Win")
				c_score.append(1)
		def Comp_Paper():
			if player_option == 1:
				Label_Status.config(text="Computer Win")
				c_score.append(1)
			elif player_option == 2:
				Label_Status.config(text="Game Tie")
			elif player_option == 3:
				Label_Status.config(text="Player Win")
				p_score.append(1)
		def Comp_Scissor():
			if player_option == 1:
				Label_Status.config(text="Player Win")
				p_score.append(1)
			elif player_option == 2:
				Label_Status.config(text="Computer Win")
				c_score.append(1)
			elif player_option == 3:
				Label_Status.config(text="Game Tie")
		def Matching():
			computer_option = random.randint(1, 3)
			if computer_option == 1:
				Image_Computer.configure(image=Computer_Rock)
				Comp_Rock()
			elif computer_option == 2:
				Image_Computer.configure(image=Computer_Paper)
				Comp_Paper()
			elif computer_option == 3:
				Image_Computer.configure(image=Computer_Scissor)
				Comp_Scissor()
		def score():
			class Table:
				def __init__(self,root):
					for i in range(total_rows):
						for j in range(total_columns):
							self.e = Entry(h, width=20, fg='#588C7E', font='Arial 16 italic')
							self.e.grid(row=i, column=j)
							self.e.insert(END, lst[i][j])
			lst = [('PLAYER','SCORE'),('Computer',len(c_score)), ('Player',len(p_score))]
			total_rows = len(lst)
			total_columns = len(lst[0])
			h=Toplevel()
			t = Table(h)
		Image_Player = Label(see, image=Blank_img)
		Image_Computer = Label(see, image=Blank_img)
		Label_Player = Label(see, text="PLAYER")
		Label_Player.grid(row=1, column=1)
		Label_Player.config(bg="#588C7E", fg="white", font='arial 18 bold')
		Label_Computer = Label(see, text="COMPUTER")
		Label_Computer.grid(row=1, column=3)
		Label_Computer.config(bg="#588C7E", fg="white", font='arial 18 bold')
		Label_Status = Label(see, text="", font='arial 18')
		Label_Status.config(fg="black", font='arial 20 bold italic')
		Image_Player.grid(row=2, column=1, padx=30, pady=20)
		Image_Computer.grid(row=2, column=3, pady=20)
		Label_Status.grid(row=3, column=2)
		rock = Button(see, image=Player_Rock_ado, command=Rock)
		paper = Button(see, image=Player_Paper_ado, command=Paper)
		scissor = Button(see, image=Player_Scissor_ado, command=Scissor)
		ban=Button(see, text="Scoreboard", bg="pink", fg="white", font='arial 18 bold', command=score).grid(row=5, column=1)
		button_quit = Button(see, text="Exit", bg="yellow", fg="black", font='arial 18 bold', command=thanks)
		rock.grid(row=4, column=1, pady=30)
		paper.grid(row=4, column=2, pady=30)
		scissor.grid(row=4, column=3, pady=30)
		button_quit.grid(row=5, column=3)
		see.mainloop()
	Computer = PhotoImage(file="resources/Computer.png")
	butt=Button(win, image=Computer, command=hey)
	butt.pack(padx=150, pady=1, side=RIGHT)
	button_quit = Button(win, text="Exit", bg="red", fg="white", font='arial 24 bold', command=thanks)
	button_quit.pack(padx=5,pady=50, side=BOTTOM)
	win.mainloop()
start=PhotoImage(file="resources/rock.png")
button=Button(root,image=start, command=mycommand)
button.pack(pady=90)
quit=Button(root, text="Exit", bg="red", fg="white", font='arial 24 bold', command=thanks)
quit.pack(pady=30)
root.mainloop()
