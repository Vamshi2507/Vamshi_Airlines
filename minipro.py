from tkinter import *
import tkinter.messagebox as MBx
import mysql.connector as mysql


def main():
    
    def book():
        Passenger_Id = passen_id.get();
        Name = name.get();
        Mobile = mob_num.get();
        Email = email_id.get()
        Age = age.get();
        Boarding_point = boarding.get();
        Destination_point=destination.get();
        Date=date.get();
        Time=time.get();

        
        if(Passenger_Id=="" or Name=="" or Mobile=="" or Email=="" or Age=="" or Boarding_point=="" or Destination_point=="" or Date=="" or Time==""):
            MBx.showinfo ("Insert Status", "All Fields are required")
            show()
        else:
            con = mysql.connect (host="localhost", user="root", password="Vamshi@3304",database="airline")
            cursor = con.cursor()
            cursor.execute("insert into passengers values ('"+ Passenger_Id +"','"+ Name +"','"+ Mobile +"','"+ Email +"','"+ Age +"','"+ Boarding_point+"','"+ Destination_point+"','"+ Date+"','"+ Time+"')")
            cursor.execute("commit");
                            
            passen_id.delete(0, 'end')
            name.delete(0, 'end')
            mob_num.delete(0, 'end')
            email_id.delete(0, 'end')
            age.delete(0, 'end')
            boarding.delete(0, 'end')
            destination.delete(0, 'end')
            date.delete(0, 'end')
            time.delete(0, 'end')
                     
            MBx.showinfo("Booking Status", "Ticket Booked Successfully");
            show()
            con.close();
            
    def cancel():
        if(passen_id.get () == ""):
            MBx.showinfo("Delete Status", "Feild Can't be empty")
        else:
            con = mysql.connect (host="localhost", user="root", password="Vamshi@3304",database="airline")
            cursor = con.cursor()
            cursor.execute("delete from passengers where Passenger_Id='"+ passen_id.get () +"'")
            cursor.execute("commit");
            
            passen_id.delete(0, 'end')
            name.delete(0, 'end')
            mob_num.delete(0, 'end')
            email_id.delete(0, 'end')
            age.delete(0, 'end')
            boarding.delete(0, 'end')
            destination.delete(0, 'end')
            date.delete(0, 'end')
            time.delete(0, 'end')
            
            MBx.showinfo("Cancel Status", "Ticket Cancelled Successfully");
            show()
            con.close();
            
    def update():
        Passenger_Id = passen_id.get();
        Name = name .get();
        Mobile = mob_num.get();
        Email=email_id.get();
        Age = age.get();
        Boarding_point=boarding.get();
        Destination_point=destination.get();
        Date=date.get();
        Time=time.get();
        

        
        if(Passenger_Id=="" or Name=="" or Mobile=="" or Email=="" or Age=="" or Boarding_point=="" or Destination_point=="" or Date=="" or Time==""):
            MBx.showinfo ("update Status", "All Fields are required")
            show()
        else:
            con = mysql.connect (host="localhost", user="root", password="Vamshi@3304",database="airline")
            cursor = con.cursor ()
            cursor.execute("update passengers set Name='"+ Name +"', Mobile='"+ Mobile +"',Email='"+ Email +"', Age='"+ Age +"',Boarding_point='"+ Boarding_point +"', Destination_point='"+ Destination_point +"',Date='"+ Date +"',Time='"+ Time +"' where Passenger_Id='"+ Passenger_Id +"'")
            cursor.execute("commit");
                            
            passen_id.delete(0, 'end')
            name.delete(0, 'end')
            mob_num.delete(0, 'end')
            email_id.delete(0, 'end')
            age.delete(0, 'end')
            boarding.delete(0, 'end')
            destination.delete(0, 'end')
            date.delete(0, 'end')
            time.delete(0, 'end')
            
            MBx.showinfo("update Status", "updated Successfully");
            show()
            con.close();

    def get():
        if(passen_id.get () == ""):
            MBx.showinfo("Fetch Status", "Feild Can't be empty")
            show()
        else:
            con = mysql.connect (host="localhost", user="root", password="Vamshi@3304",database="airline")
            cursor = con.cursor()
            cursor.execute("select *  from passengers where Passenger_Id='"+ passen_id.get () +"'")
            rows = cursor.fetchall()
            cursor.execute("commit");
            
            for row in rows:
                name.insert(0, row[1])
                mob_num.insert(0,row[2])
                email_id.insert(0, row[3])
                age.insert(0, row[4])
                boarding.insert(0, row[5])
                destination.insert(0, row[6])
                date.insert(0, row[7])
                time.insert(0, row[8])
                
            con.close();


    def show():
        con = mysql.connect (host="localhost", user="root", password="Vamshi@3304",database="airline")
        cursor = con.cursor()
        cursor.execute ("select * from passengers")
        rows = cursor.fetchall()
        list.delete(0,list.size())
        
        for row in rows:
            insertData = str(row[0])+'      '+ row[1]
            list.insert(list.size()+1,insertData)
            
        con.close()            

    root = Tk()
    root.geometry("600x300")
    root.title("Airline Ticket Booking System")
    root['bg']='light blue'


    Passenger_Id = Label(root,text='Passeneger ID',bg="light blue", font=('Times New Roman', 16))
    Passenger_Id.place(x=20, y=30)

    Name = Label(root,text='Passenger Name',bg="light blue",font=('Times New Roman', 16))
    Name.place(x=20, y=60)

    Mobile = Label(root, text='Passenger Mobile',bg="light blue", font=('Times New Roman', 16))
    Mobile.place(x=20, y=90);

    Email = Label(root, text='Passenger Email',bg="light blue", font=('Times New Roman', 16))
    Email.place(x=20, y=120);

    Age = Label(root, text='Passenger Age',bg="light blue", font=('Times New Roman', 16))
    Age.place(x=20, y=150);

    Boarding_point = Label(root, text='Bording Point',bg="light blue", font=('Times New Roman', 16))
    Boarding_point.place(x=20, y=180);
    
    Destination_point=Label(root,text="Destination Point",bg="light blue", font=('Times New Roman',16))
    Destination_point.place(x=20,y=210);
    
    Date=Label(root,text="Enter date of travel",bg="light blue",font=('Times New Roman',16))
    Date.place(x=20,y=240)
    
    Time=Label(root,text="Time",bg="light blue",font=('Times New Roman',16))
    Time.place(x=20,y=270)


    passen_id = Entry()
    passen_id.place(x=180, y=30)

    name= Entry()
    name.place(x=180, y=60)

    mob_num=Entry()
    mob_num.place(x=180, y=90)

    email_id = Entry()
    email_id.place(x=180, y=120)

    age=Entry()
    age.place(x=180, y=150)

    boarding = Entry()
    boarding.place(x=180, y=180)
    
    destination = Entry()
    destination.place(x=180,y=210)
    
    date=Entry()
    date.place(x=180,y=240)
    
    time= Entry()
    time.place(x=180,y=270)


    Book=Button(root, text="Book Ticket", font=("Times New Roman", 16), bg="white", command=book)
    Book.place(x=100,y=330)


    Cancel=Button(root, text="Cancel Ticket", font=("Times New Roman", 16), bg="white", command=cancel)
    Cancel.place(x=300,y=330)


    change=Button(root, text="Change Passengers Details", font=("Times New Roman", 16), bg="white", command=update)
    change.place(x=500,y=330)



    get=Button(root, text="Get", font=("Times New Roman", 16), bg="white", command=get)
    get.place(x=800,y=330)

    list1=Label(root,text="Passengers list",bg="light blue",font=("Times New Roman",16))
    list1.place(x=350,y=0)
    list = Listbox(root)
    list.place(x=350, y=30)
    show()
    root.mainloop()





#loginpage

def signin():
    uname=e1.get()
    password=e2.get()
    if uname=='' and password=='' :
        MBx.showinfo('','Please Enter the login credentials')
    elif uname=='vamshi' and password=='2003' :
        root.destroy()
        main()
    else:
        MBx.showinfo('','Please enter a valid Usename or Password')


def signup():
    root1=Tk()
    root1.title('login to the server')
    root1.geometry('300x200')
    root1.configure(bg="light blue")

    User_Name = user_name.get();
    Mobile = mob_num.get();
    Email = email_id.get()
    Age = age.get();
    Password = password.get();


    User_Name = Label(root1,text='Passenger Name',bg="light blue",font=('Times New Roman', 16))
    User_Name.place(x=20, y=60)

    Mobile = Label(root1, text='Passenger Mobile',bg="light blue", font=('Times New Roman', 16))
    Mobile.place(x=20, y=90);

    Email = Label(root1, text='Passenger Email',bg="light blue", font=('Times New Roman', 16))
    Email.place(x=20, y=120);

    Age = Label(root1, text='Passenger Age',bg="light blue", font=('Times New Roman', 16))
    Age.place(x=20, y=150);

    Password = Label(root1, text='Password',bg="light blue", font=('Times New Roman', 16))
    Password.place(x=20, y=180);
    
    user_name= Entry()
    user_name.place(x=180, y=30)

    mob_num=Entry()
    mob_num.place(x=180, y=60)

    email_id = Entry()
    email_id.place(x=180, y=90)

    age=Entry()
    age.place(x=180, y=120)

    password = Entry()
    password.place(x=180, y=150)
    
    root1.mainloop()

    

root=Tk()
root.title('login to the server')
root.geometry('300x200')
root.configure(bg="light blue")


Label(root,text='username',bg='light blue',font=("Times New Roman", 16)).place(x=10 ,y=10)
Label(root,text='password',bg='light blue',font=("Times New Roman",16)).place(x=10,y=40)
e1=Entry(root)
e1.place(x=140,y=10)

e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show='*')

Button(root,text='login',command=signin, height =1 , width= 10, bg='white',fg='black',font=("Times New Roman",16)).place(x=100,y=100)
Button(root,text='sign up',command=signup, height=1,width=10,bg='white',fg='black',font=('Times New Roman',16)).place(x=100,y=200)
root.mainloop()
