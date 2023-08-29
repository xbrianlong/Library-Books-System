from tkinter import *
from PIL import ImageTk, Image
import datetime

from sqlalchemy import update

import database

#region root and style definitions
root = Tk()
dfont = "Roboto"

root.title("ALS Group 19")
root.attributes('-fullscreen', True)
#endregion

#region fields for entry fields
createMemberFields = ["","","","",""]
deleteMemberFields = [""]

#endregion

#region helper functions
def showframe(frame):
    frame.tkraise()

def doubleshowframe(frame1, frame2):
    showframe(frame1)
    showframe(frame2)

def update_frame(launcher, frame, *args):
    frame_popup = frame
    updated_frame = launcher(frame_popup, *args)
    showframe(updated_frame)

## requires that the table col_num be the same as the number of headers in header_lst
def showtablegui(frame, table, header_lst):
    if len(table) == 0:
        for i in range(len(header_lst)):
            header = Label(frame, width=10, text= header_lst[i],\
                           borderwidth=2,relief='ridge',\
                           anchor='w',bg='yellow')
            header.grid(0, column = i)
    
    else:
        for i in range(len(header_lst)):
            header = Label(frame, width=10, text= header_lst[i],\
                           borderwidth=2,relief='ridge',\
                           anchor='w',bg='yellow')
            header.grid(0, column = i)
            
            
        row_num = 1
        for tuple in table:
                for col_num in range(len(tuple)):
                    elem = Label(frame, width = 10, text = tuple[col_num],\
                                borderwidth=2,relief='ridge', anchor="w",\
                                font = (dfont,30))
                    elem.grid(row = row_num, col = col_num)
                    
                row_num += 1
        
#endregion

'''MM stands for Main Menu
MBS stands for Membership
RSV stands for Reservations'''

#region frame_MM (Main Menu)
frame_MM = Frame(root)
def frame_MM_launcher():
    frame_MM.grid(row=0, column=0, sticky="nsew")

    label_MM_ALS = Label(frame_MM, text="ALS", padx=100, pady=50, font=(dfont, 30))
    button_MM_MBS = Button(frame_MM, text="Membership", padx=50, pady=5, font=(dfont, 30), command=lambda:showframe(frame_MBS), bg="powderblue")
    button_MM_Books = Button(frame_MM, text="Books", padx=100, pady=5, font=(dfont, 30), command=lambda:showframe(frame_Books), bg="powderblue")
    button_MM_Loans = Button(frame_MM, text="Loans", padx=50, pady=5, font=(dfont, 30), bg="powderblue", command=lambda:showframe(frame_Loans))
    button_MM_RSV = Button(frame_MM, text="Reservations", padx=50, pady=5, font=(dfont, 30), bg="powderblue", command=lambda:showframe(frame_RSV))
    button_MM_Fines = Button(frame_MM, text="Fines", padx=100, pady=5, font=(dfont, 30), bg="powderblue", command=lambda:showframe(frame_Fines))
    button_MM_Reports = Button(frame_MM, text="Reports", padx=50, pady=5, font=(dfont, 30), bg="powderblue", command=lambda:showframe(frame_Reports))
    button_MM_Exit = Button(frame_MM, text="Exit ALS (OR press Alt F4)", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(root.destroy()), bg="white")

    label_MM_ALS.grid(row=0, column=1)
    button_MM_MBS.grid(row=1, column=0)
    button_MM_Books.grid(row=1, column=1)
    button_MM_Loans.grid(row=1, column=2)
    button_MM_RSV.grid(row=2, column=0)
    button_MM_Fines.grid(row=2, column=1)
    button_MM_Reports.grid(row=2, column=2)
    button_MM_Exit.grid(row=3, column=0, columnspan=3)
frame_MM_launcher()
#endregion

#MEMBERSHIP SECTION

#region frame_MBS (Membership)
frame_MBS = Frame(root)
MBS_img = ImageTk.PhotoImage(Image.open("MBS_pic.jpg"))

def frame_MBS_launcher():
    frame_MBS.grid(row=0, column=0, sticky="nsew")

    label_MBS_instruction = Label(frame_MBS, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_MBS_Creation = Button(frame_MBS, text="1. Creation: Membership creation", padx=100, pady=50, font=(dfont, 20), command=lambda:showframe(frame_MBS_Creation), bg="mistyrose")
    button_MBS_Deletion = Button(frame_MBS, text="2. Deletion: Membership deletion", padx=100, pady=50, font=(dfont, 20), command=lambda:showframe(frame_MBS_Deletion), bg="mistyrose")
    button_MBS_Update = Button(frame_MBS, text="3. Update: Membership update", padx=100, pady=50, font=(dfont, 20), command=lambda:showframe(frame_MBS_Update), bg="mistyrose")
    button_MBS_Back = Button(frame_MBS, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_MBS_img = Label(frame_MBS, image=MBS_img)

    label_MBS_instruction.grid(row=0, column=0, columnspan=2)
    button_MBS_Creation.grid(row=1, column=1, rowspan=2)
    button_MBS_Deletion.grid(row=3, column=1, rowspan=2)
    button_MBS_Update.grid(row=5, column=1, rowspan=2)
    button_MBS_Back.grid(row=7, column=0, columnspan=2)
    label_MBS_img.grid(row=1, column=0, rowspan=6)
frame_MBS_launcher()
#endregion frame_MBS

#region frame_MBS_Creation
frame_MBS_Creation = Frame(root)
def frame_MBS_Creation_launcher():
    frame_MBS_Creation.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_MBS)
        frame_MBS_Creation_launcher()
        
    MBS_Creation_instruction = Label(frame_MBS_Creation, text="To Create Member, Please Enter Requested Information Below:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    e_MBS_Creation_ID = Entry(frame_MBS_Creation, width=50, font=(dfont,30))
    e_MBS_Creation_ID.insert(0, "Enter Membership ID")
    e_MBS_Creation_Name = Entry(frame_MBS_Creation, width=50, font=(dfont,30))
    e_MBS_Creation_Name.insert(0, "Enter Member Name")
    e_MBS_Creation_Faculty = Entry(frame_MBS_Creation, width=50, font=(dfont,30))
    e_MBS_Creation_Faculty.insert(0, "Enter Member Faculty")
    e_MBS_Creation_pnum = Entry(frame_MBS_Creation, width=50, font=(dfont,30))
    e_MBS_Creation_pnum.insert(0, "Enter Phone Number")
    e_MBS_Creation_Email = Entry(frame_MBS_Creation, width=50, font=(dfont,30))
    e_MBS_Creation_Email.insert(0, "Enter Email Address")

    

    ##def createMember(id, name, faculty, phoneNum, email):
    def createMemberUI():
        global createMemberFields
        createMemberFields[0] = e_MBS_Creation_ID.get()
        createMemberFields[1] = e_MBS_Creation_Name.get()
        createMemberFields[2] = e_MBS_Creation_Faculty.get()
        createMemberFields[3] = e_MBS_Creation_pnum.get()
        createMemberFields[4] = e_MBS_Creation_Email.get()
        createMemberStatus = database.createMember(createMemberFields[0], 
                                          createMemberFields[1], 
                                          createMemberFields[2],
                                          createMemberFields[3],
                                          createMemberFields[4])             
        if createMemberStatus == True:
            showframe(frame_create_member)        
        else:
            showframe(frame_Create_Member_Error_Popup)
            
    button_MBS_Creation_Back = Button(frame_MBS_Creation, text="Back to Membership Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_MBS_Creation_ConfirmMember = Button(frame_MBS_Creation, text="Create Member", padx=200, pady=5, font=(dfont, 15), command=lambda:createMemberUI())

    MBS_Creation_instruction.grid(row=0, column=0, columnspan=2)
    e_MBS_Creation_ID.grid(row=1, column=0, columnspan=2)
    e_MBS_Creation_Name.grid(row=2, column=0, columnspan=2)
    e_MBS_Creation_Faculty.grid(row=3, column=0, columnspan=2)
    e_MBS_Creation_pnum.grid(row=4, column=0, columnspan=2)
    e_MBS_Creation_Email.grid(row=5, column=0, columnspan=2)
    button_MBS_Creation_Back.grid(row=6, column=1)
    button_MBS_Creation_ConfirmMember.grid(row=6, column=0)
frame_MBS_Creation_launcher()

#Create Successfully Created Member Popup
frame_create_member = Frame(root, bg="green")
def label_create_member_launcher():
    label_create_member = Label(frame_create_member, text="SUCCESS: ALS Membership created", font=(dfont, 15), bg="green")
    button_create_member = Button(frame_create_member, text="Back to Create Function", padx=200, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_MBS_Creation))

    label_create_member.pack()
    button_create_member.pack()
    frame_create_member.grid(row=0, column=0)
label_create_member_launcher()

#Create Create Member Error Popup
frame_Create_Member_Error_Popup = Frame(root, bg="red")
def frame_Create_Member_Error_Popup_launcher():
    frame_Create_Member_Error_Popup.grid(row=0, column=0)

    label_Create_Member_Error_Popup1 = Label(frame_Create_Member_Error_Popup, text="Error! ", font=(dfont, 50), fg="yellow", bg="red")
    label_Create_Member_Error_Popup2 = Label(frame_Create_Member_Error_Popup, text="Member already exists; \n Missing or Incomplete fields", font=(dfont, 20), fg="yellow", bg="red")
    button_Create_Member_Error_Popup = Button(frame_Create_Member_Error_Popup, text="Back to Create Function", padx=50, pady=20, font=(dfont, 20),
                                borderwidth=5, bg="red", fg="yellow", command=lambda:showframe(frame_MBS_Creation))

    label_Create_Member_Error_Popup1.pack()
    label_Create_Member_Error_Popup2.pack()
    button_Create_Member_Error_Popup.pack()
frame_Create_Member_Error_Popup_launcher()
#endregion frame_MBS_Creation

#region frame_MBS_Deletion
frame_MBS_Deletion = Frame(root)
def frame_MBS_Deletion_launcher():
    frame_MBS_Deletion.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_MBS)
        frame_MBS_Deletion_launcher()
        
    MBS_Deletion_instruction = Label(frame_MBS_Deletion, text="To Delete Member, Please Enter Membership ID:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    global e_MBS_Deletion_ID
    e_MBS_Deletion_ID = Entry(frame_MBS_Deletion, width=50, font=(dfont,30))
    e_MBS_Deletion_ID.insert(0, "Enter Membership ID")
    button_MBS_Deletion_Back = Button(frame_MBS_Deletion, text="Back to Membership Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_MBS_Deletion_DeleteMember = Button(frame_MBS_Deletion, text="Delete Member", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Confirm_Delete_Member_Popup_launcher, Frame(root, bg="green")))

    MBS_Deletion_instruction.grid(row=0, column=0, columnspan=2)
    e_MBS_Deletion_ID.grid(row=1, column=0, columnspan=2)
    button_MBS_Deletion_Back.grid(row=2, column=1)
    button_MBS_Deletion_DeleteMember.grid(row=2, column=0)
frame_MBS_Deletion_launcher()


#Create Confirm Delete Member Popup
def frame_Confirm_Delete_Member_Popup_launcher(frame_Confirm_Delete_Member_Popup):
    frame_Confirm_Delete_Member_Popup.grid(row=0, column=0)

    ##def delete_member(id):
    # def deleteMemberUI():
    #     global deleteMemberFields
    #     deleteMemberFields[0] = e_MBS_Deletion_ID.get()

    #     deleteMemberStatus = database.delete_member(deleteMemberFields[0])             
    #     if deleteMemberStatus == True:
    #         showframe(frame_MBS_Deletion)        
    #     else:
    #         showframe(frame_Delete_Member_Error_Popup)
    
    label_Confirm_Delete_Member_Popup = Label(frame_Confirm_Delete_Member_Popup, text="Please Confirm Details to Be Correct", font=(dfont, 20), bg="green")
    label_Confirm_Delete_Member_Details_Popup = Label(frame_Confirm_Delete_Member_Popup, text=database.delete_member_details(e_MBS_Deletion_ID.get()), font=(dfont, 15), bg="green")
    button_Confirm_Delete_Member_Popup = Button(frame_Confirm_Delete_Member_Popup, text="Confirm Deletion", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:member_deletion_pass_or_fail())
    button_Confirm_Delete_Member_Popup_Back = Button(frame_Confirm_Delete_Member_Popup, text="Back to Delete Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_MBS_Deletion))

    label_Confirm_Delete_Member_Popup.grid(row=0, column=0, columnspan=2)
    label_Confirm_Delete_Member_Details_Popup.grid(row=1, column=0, columnspan=2)
    button_Confirm_Delete_Member_Popup.grid(row=2, column=0)
    button_Confirm_Delete_Member_Popup_Back.grid(row=2, column=1)
    def member_deletion_pass_or_fail():
        result = database.delete_member(e_MBS_Deletion_ID.get())
        if result:
            showframe(frame_MBS_Deletion)
        else:
            update_frame(frame_Delete_Member_Error_Popup_launcher, Frame(root, bg="red"))
    return frame_Confirm_Delete_Member_Popup  

#Create Delete Member Error Popup
def frame_Delete_Member_Error_Popup_launcher(frame_Delete_Member_Error_Popup):
    frame_Delete_Member_Error_Popup.grid(row=0, column=0)

    label_Delete_Member_Error_Popup1 = Label(frame_Delete_Member_Error_Popup, text="Error!", font=(dfont, 50), fg="yellow", bg="red")
    label_Delete_Member_Error_Popup2 = Label(frame_Delete_Member_Error_Popup, text="Member has loans, \n reservations or \n outstanding fines \n", font=(dfont, 20), fg="yellow", bg="red")
    button_Delete_Member_Error_Popup = Button(frame_Delete_Member_Error_Popup, text="Back to Delete Function", padx=50, pady=20, font=(dfont, 20),
                                borderwidth=5, bg="red", fg="yellow", command=lambda:showframe(frame_MBS_Deletion))

    label_Delete_Member_Error_Popup1.pack()
    label_Delete_Member_Error_Popup2.pack()
    button_Delete_Member_Error_Popup.pack()
frame_Delete_Member_Error_Popup = Frame(root, bg="red")

#endregion frame_MBS_Deletion

#region frame_MBS_Update

#Page 1
MBS_Update2_ID = None
MBS_Update2_Member_ID = None
frame_MBS_Update = Frame(root)
def frame_MBS_Update_launcher():
    frame_MBS_Update.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_MBS)
        frame_MBS_Update_launcher()

    def get_Update_MBS_ID():
        #Takes in Membership ID to put in Page 2
        global MBS_Update2_Member_ID
        global MBS_Update2_ID
        MBS_Update2_Member_ID = e_MBS_Update_ID.get()
        MBS_Update2_ID = Label(frame_MBS_Update2, text="Membership ID: "+ MBS_Update2_Member_ID, padx=200, pady=20, font=(dfont, 20), bg="lightblue")
        MBS_Update2_ID.grid(row=1, column=0, columnspan=2)
        showframe(frame_MBS_Update2)

    #if member exist show
    def member_exist():
        result = database.doesMemberExist(e_MBS_Update_ID.get())
        if result:
            get_Update_MBS_ID()
        
    MBS_Update_instruction = Label(frame_MBS_Update, text="To Update a Member, Please Enter Membership ID:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    e_MBS_Update_ID = Entry(frame_MBS_Update, width=50, font=(dfont,30))
    e_MBS_Update_ID.insert(0, "Enter Membership ID")
    button_MBS_Update_Back = Button(frame_MBS_Update, text="Back to Membership Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_MBS_Update_UpdateMember = Button(frame_MBS_Update, text="Update Member", padx=200, pady=5, font=(dfont, 15), command=member_exist)
        

    MBS_Update_instruction.grid(row=0, column=0, columnspan=2)
    e_MBS_Update_ID.grid(row=1, column=0, columnspan=2)
    button_MBS_Update_Back.grid(row=2, column=1)
    button_MBS_Update_UpdateMember.grid(row=2, column=0)
frame_MBS_Update_launcher()

#Page 2
frame_MBS_Update2 = Frame(root)
MBS_Update2_Member_Details = None

def frame_MBS_Update2_launcher():

    def get_MBS_Update2_Member_Details():
        #Takes in Member Details to put in Confirm Details Page
        global MBS_Update2_Member_Details
        MBS_Update2_Member_Details = Label(update_frame(frame_MBS_Update2_Confirm_launcher, Frame(root, bg="green")), text = f"Membership ID: {MBS_Update2_Member_ID}\nName: {e_MBS_Update2_Name.get()}\nFaculty: {e_MBS_Update2_Faculty.get()}\nPhone Number: {e_MBS_Update2_pnum.get()}\nEmail: {e_MBS_Update2_Email.get()}", padx=200, pady=20, font=(dfont, 15), bg="green")
        MBS_Update2_Member_Details.grid(row=1, column=0, columnspan=2)
        update_frame(frame_MBS_Update2_Confirm_launcher, Frame(root, bg="green"))

    frame_MBS_Update2.grid(row=0, column=0, sticky="nsew")

    global e_MBS_Update2_Name
    global e_MBS_Update2_Faculty
    global e_MBS_Update2_pnum
    global e_MBS_Update2_Email

    MBS_Update2_instruction = Label(frame_MBS_Update2, text="Please enter requested information below:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    e_MBS_Update2_Name = Entry(frame_MBS_Update2, width=50, font=(dfont,30))
    e_MBS_Update2_Name.insert(0, "Update Member Name")
    e_MBS_Update2_Faculty = Entry(frame_MBS_Update2, width=50, font=(dfont,30))
    e_MBS_Update2_Faculty.insert(0, "Update Member Faculty")
    e_MBS_Update2_pnum = Entry(frame_MBS_Update2, width=50, font=(dfont,30))
    e_MBS_Update2_pnum.insert(0, "Update Phone Number")
    e_MBS_Update2_Email = Entry(frame_MBS_Update2, width=50, font=(dfont,30))
    e_MBS_Update2_Email.insert(0, "Update Email Address")

    button_MBS_Update2_Back = Button(frame_MBS_Update2, text="Back to Membership Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MBS))
    button_MBS_Update2_UpdateMember = Button(frame_MBS_Update2, text="Update Member", padx=200, pady=5, font=(dfont, 15), command=get_MBS_Update2_Member_Details)

    button_MBS_Update2_Back.grid(row=6, column=1)
    button_MBS_Update2_UpdateMember.grid(row=6, column=0)

    MBS_Update2_instruction.grid(row=0, column=0, columnspan=2)
    e_MBS_Update2_Name.grid(row=2, column=0, columnspan=2)
    e_MBS_Update2_Faculty.grid(row=3, column=0, columnspan=2)
    e_MBS_Update2_pnum.grid(row=4, column=0, columnspan=2)
    e_MBS_Update2_Email.grid(row=5, column=0, columnspan=2)
frame_MBS_Update2_launcher()
#Create Confirm Update Member Popup


def frame_MBS_Update2_Confirm_launcher(frame_MBS_Update2_Confirm):
    frame_MBS_Update2_Confirm.grid(row=0, column=0)

    label_MBS_Update2_Confirm = Label(frame_MBS_Update2_Confirm, text="Please Confirm Details to Be Correct", font=(dfont, 20), bg="green")
    #REMINDER: Need to retrieve and add member details to confirm details to be correct
    string = ""
    string += "Membership ID: " + str(MBS_Update2_Member_ID) + "\n" + \
        "Name: " + str(e_MBS_Update2_Name.get()) + "\n" + \
        "Faculty: " + str(e_MBS_Update2_Faculty.get()) + "\n" + \
        "Phone Number: " + str(e_MBS_Update2_pnum.get()) + "\n" + \
        "Email: " + str(e_MBS_Update2_Email.get())

    label_Loans_Update2_Confirm_Details = Label(frame_MBS_Update2_Confirm, text=string, font=(dfont, 15), bg="green")

    button_MBS_Update2_Confirm = Button(frame_MBS_Update2_Confirm, text="Confirm Update", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:member_update_pass_or_fail())
    button_MBS_Update2_Confirm_Back = Button(frame_MBS_Update2_Confirm, text="Back to Update Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_MBS_Update2))

    def member_update_pass_or_fail():
        result = database.updateMember(MBS_Update2_Member_ID, e_MBS_Update2_Name.get(), e_MBS_Update2_Faculty.get(), e_MBS_Update2_pnum.get(), e_MBS_Update2_Email.get())
        if result:
            doubleshowframe(frame_MBS_Update2, frame_MBS_Update2_Success)
        else:
            showframe(frame_Update_Member_Error_Popup)

    label_MBS_Update2_Confirm.grid(row=0, column=0, columnspan=2)
    label_Loans_Update2_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_MBS_Update2_Confirm.grid(row=2, column=0)
    button_MBS_Update2_Confirm_Back.grid(row=2, column=1)
    



#Create Successfully Updated Member Popup
frame_MBS_Update2_Success = Frame(root, bg="green")
def frame_MBS_Update2_Success_launcher():
    frame_MBS_Update2_Success.grid(row=0, column=0)

    label_MBS_Update2_Success = Label(frame_MBS_Update2_Success, text="Success! \n ALS Membership Updated.", font=(dfont, 25), bg="green")
    button_MBS_Update2_Success = Button(frame_MBS_Update2_Success, text="Create Another Member", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_MBS_Creation))
    button_MBS_Update2_Success_Back = Button(frame_MBS_Update2_Success, text="Back to Update Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_MBS_Update2))

    label_MBS_Update2_Success.grid(row=0, column=0, columnspan=2)
    button_MBS_Update2_Success.grid(row=1, column=0)
    button_MBS_Update2_Success_Back.grid(row=1, column=1)
frame_MBS_Update2_Success_launcher()

#Create Update Member Error Popup
frame_Update_Member_Error_Popup = Frame(root, bg="red")
def Update_Member_Error_Popup_launcher():
    frame_Update_Member_Error_Popup.grid(row=0, column=0)

    label_Update_Member_Error_Popup1 = Label(frame_Update_Member_Error_Popup, text="Error!", font=(dfont, 50), fg="yellow", bg="red")
    label_Update_Member_Error_Popup2 = Label(frame_Update_Member_Error_Popup, text="Missing or Incomplete fields", font=(dfont, 20), fg="yellow", bg="red")
    button_Update_Member_Error_Popup = Button(frame_Update_Member_Error_Popup, text="Back to Update Function", padx=50, pady=20, font=(dfont, 20),
                                borderwidth=5, bg="red", fg="yellow", command=lambda:showframe(frame_MBS_Update))

    label_Update_Member_Error_Popup1.pack()
    label_Update_Member_Error_Popup2.pack()
    button_Update_Member_Error_Popup.pack()
Update_Member_Error_Popup_launcher()
#endregion frame_MBS_Update

#BOOKS SECTION

#region frame_Books
frame_Books = Frame(root)
Books_img = ImageTk.PhotoImage(Image.open("Books_pic.jpg"))

def frame_Books_launcher():
    frame_Books.grid(row=0, column=0, sticky="nsew")

    label_Books_instruction = Label(frame_Books, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_Books_Acquisition = Button(frame_Books, text="4. Acquisition: Book Acquisition", padx=100, pady=50, font=(dfont, 20), command=lambda:showframe(frame_Books_Acquisition), bg="peachpuff")
    button_Books_Withdrawal = Button(frame_Books, text="5. Withdrawal: Book Withdrawal", padx=100, pady=50, font=(dfont, 20), bg="peachpuff", command=lambda:showframe(frame_Books_Withdrawal))
    button_Books_Back = Button(frame_Books, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_Books_img = Label(frame_Books, image=Books_img)

    label_Books_instruction.grid(row=0, column=0, columnspan=2)
    button_Books_Acquisition.grid(row=1, column=1)
    button_Books_Withdrawal.grid(row=2, column=1)
    button_Books_Back.grid(row=3, column=0, columnspan=2)
    label_Books_img.grid(row=1, column=0, rowspan=2)
frame_Books_launcher()
#endregion frame_Books

#region frame_Books_Acquisition
frame_Books_Acquisition = Frame(root)
def frame_Books_Acquistion_launcher():
    frame_Books_Acquisition.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_Books)
        frame_Books_Acquistion_launcher()
    
    Books_Acquisition_instruction = Label(frame_Books_Acquisition, text="For New Book Acquisition, Please Enter Required Information Below:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    e_Books_Acquisition_Accessionnum = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_Accessionnum.insert(0, "Enter Accession Number")
    e_Books_Acquisition_Title = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_Title.insert(0, "Enter Book Title")
    e_Books_Acquisition_Authors = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_Authors.insert(0, "Enter Book Authors")
    e_Books_Acquisition_ISBN = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_ISBN.insert(0, "Enter ISBN Number")
    e_Books_Acquisition_Publisher = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_Publisher.insert(0, "Enter Publisher name")
    e_Books_Acquisition_Publicationyear = Entry(frame_Books_Acquisition, width=50, font=(dfont,30))
    e_Books_Acquisition_Publicationyear.insert(0, "Enter Publication Year")

    button_Books_Acquisition_Back = Button(frame_Books_Acquisition, text="Back to Books Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Books_Acquisition_Add = Button(frame_Books_Acquisition, text="Add New Book", padx=200, pady=5, font=(dfont, 15), command=lambda:book_acquisition_pass_or_fail())


    Books_Acquisition_instruction.grid(row=0, column=0, columnspan=2)
    e_Books_Acquisition_Accessionnum.grid(row=1, column=0, columnspan=2)
    e_Books_Acquisition_Title.grid(row=2, column=0, columnspan=2)
    e_Books_Acquisition_Authors.grid(row=3, column=0, columnspan=2)
    e_Books_Acquisition_ISBN.grid(row=4, column=0, columnspan=2)
    e_Books_Acquisition_Publisher.grid(row=5, column=0, columnspan=2)
    e_Books_Acquisition_Publicationyear.grid(row=6, column=0, columnspan=2)
    button_Books_Acquisition_Back.grid(row=7, column=1)
    button_Books_Acquisition_Add.grid(row=7, column=0)

    #Member Creation Success or Failure
    def book_acquisition_pass_or_fail():
        result = database.addBook(e_Books_Acquisition_Accessionnum.get(), e_Books_Acquisition_Title.get(),e_Books_Acquisition_Authors.get(), e_Books_Acquisition_ISBN.get(), e_Books_Acquisition_Publisher.get(), e_Books_Acquisition_Publicationyear.get())
        if result:
            showframe(frame_Books_Acquisition_Success)
        else:
            showframe(frame_Books_Acquisition_Error)
frame_Books_Acquistion_launcher()

#Create Successfully Added New Book Popup
frame_Books_Acquisition_Success = Frame(root, bg="green")
def frame_Books_Acquisition_Success_launcher():
    frame_Books_Acquisition_Success.grid(row=0, column=0)

    label_Books_Acquisition_Success = Label(frame_Books_Acquisition_Success, text="Success! \n New Book added in Library", font=(dfont, 25), bg="green")
    button_Books_Acquisition_Success_Back = Button(frame_Books_Acquisition_Success, text="Back to Acquisition Function", padx=50, pady=50, font=(dfont, 18),
                                borderwidth=5, bg="green", command=lambda:showframe(frame_Books_Acquisition))

    label_Books_Acquisition_Success.pack()
    button_Books_Acquisition_Success_Back.pack()
frame_Books_Acquisition_Success_launcher()

#Create Add Book Error Popup
frame_Books_Acquisition_Error = Frame(root, bg="red")
def frame_Books_Acqusition_Error_launcher():
    frame_Books_Acquisition_Error.grid(row=0, column=0)

    label_Books_Acquisition_Error = Label(frame_Books_Acquisition_Error, text="Error! \n Book already added; \n Duplicate, Missing or \n Incomplete fields.", font=(dfont, 25), bg="red")
    button_Books_Acquisition_Error_Back = Button(frame_Books_Acquisition_Error, text="Back to Acquisition Function", padx=50, pady=50, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Books_Acquisition))

    label_Books_Acquisition_Error.pack()
    button_Books_Acquisition_Error_Back.pack()
frame_Books_Acqusition_Error_launcher()

#endregion frame_Books_Acquisition

#region frame_Books_Withdrawal
frame_Books_Withdrawal = Frame(root)
def frame_Books_Withdrawal_launcher():
    
    def back_to_previous_menu():
        showframe(frame_Books)
        frame_Books_Withdrawal_launcher()
    
    frame_Books_Withdrawal.grid(row=0, column=0, sticky="nsew")

    Books_Withdrawal_instruction = Label(frame_Books_Withdrawal, text="To Remove Outdated Books From System, Please Enter Required Information Below:", padx=150, pady=20, font=(dfont, 20), bg="aquamarine")
    global Books_Withdrawal_Accessionnum
    Books_Withdrawal_Accessionnum = Entry(frame_Books_Withdrawal, width=50, font=(dfont,30))
    Books_Withdrawal_Accessionnum.insert(0, "Enter Book Accession Number")
    button_Books_Withdrawal_Back = Button(frame_Books_Withdrawal, text="Back to Books Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Books_Withdrawal_WithdrawBook = Button(frame_Books_Withdrawal, text="Withdraw Book", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Books_Withdrawal_Confirm_launcher, Frame(root, bg="green")))

    Books_Withdrawal_instruction.grid(row=0, column=0, columnspan=2)
    Books_Withdrawal_Accessionnum.grid(row=1, column=0, columnspan=2)
    button_Books_Withdrawal_Back.grid(row=2, column=1)
    button_Books_Withdrawal_WithdrawBook.grid(row=2, column=0)
frame_Books_Withdrawal_launcher()

#Create Confirm Book Details Popup
def frame_Books_Withdrawal_Confirm_launcher(frame_Books_Withdrawal_Confirm):
    frame_Books_Withdrawal_Confirm.grid(row=0, column=0)

    label_Books_Withdrawal_Confirm = Label(frame_Books_Withdrawal_Confirm, text="Please Confirm Details to Be Correct", font=(dfont, 20), bg="green")
    label_Books_Withdrawal_Confirm_Details = Label(frame_Books_Withdrawal_Confirm, text=database.remove_book_details(Books_Withdrawal_Accessionnum.get()), font=(dfont, 15), bg="green")
    button_Books_Withdrawal_Confirm = Button(frame_Books_Withdrawal_Confirm, text="Confirm Withdrawal", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:book_withdrawal_pass_fail())
    button_Books_Withdrawal_Confirm_Back = Button(frame_Books_Withdrawal_Confirm, text="Back to Withdrawal Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_Books_Withdrawal))

    label_Books_Withdrawal_Confirm.grid(row=0, column=0, columnspan=2)
    label_Books_Withdrawal_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_Books_Withdrawal_Confirm.grid(row=2, column=0)
    button_Books_Withdrawal_Confirm_Back.grid(row=2, column=1)
    def book_withdrawal_pass_fail():
        result = database.removeBook(Books_Withdrawal_Accessionnum.get())
        if result == "Success":
            showframe(frame_Books_Withdrawal)
        else:
            showframe(frame_Books_Withdrawal)
            update_frame(frame_Books_Withdrawal_Error_launcher, Frame(root, bg="red"), result)
    return frame_Books_Withdrawal_Confirm

#Create Books Withdrawal Error Popup
def frame_Books_Withdrawal_Error_launcher(frame_Books_Withdrawal_Error, text):
    frame_Books_Withdrawal_Error.grid(row=0, column=0)

    label_Books_Withdrawal_Error = Label(frame_Books_Withdrawal_Error, text="Error! \n" + text, font=(dfont, 25), bg="red")
    button_Books_Withdrawal_Error_Back = Button(frame_Books_Withdrawal_Error, text="Back to Withdrawal Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Books_Withdrawal))

    label_Books_Withdrawal_Error.pack()
    button_Books_Withdrawal_Error_Back.pack()
    return frame_Books_Withdrawal_Error
#endregion frame_Books_Withdrawal

#LOANS SECTION

#region frame_Loans
frame_Loans = Frame(root)
Loans_img = ImageTk.PhotoImage(Image.open("Loans_pic.jpg"))

def frame_Loans_launcher():
    frame_Loans.grid(row=0, column=0, sticky="nsew")

    label_Loans_instruction = Label(frame_Loans, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_Loans_Borrow = Button(frame_Loans, text="6. Borrow: Book Borrowing", padx=150, pady=60, font=(dfont, 20), command=lambda:showframe(frame_Loans_Borrow), bg="darkolivegreen1")
    button_Loans_Return = Button(frame_Loans, text="7. Return: Book Returning", padx=150, pady=60, font=(dfont, 20), bg="darkolivegreen1", command=lambda:showframe(frame_Loans_Return))
    button_Loans_Back = Button(frame_Loans, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_Loans_img = Label(frame_Loans, image=Loans_img)

    label_Loans_instruction.grid(row=0, column=0, columnspan=2)
    button_Loans_Borrow.grid(row=1, column=1)
    button_Loans_Return.grid(row=2, column=1)
    button_Loans_Back.grid(row=3, column=0, columnspan=2)
    label_Loans_img.grid(row=1, column=0, rowspan=2)
frame_Loans_launcher()

#endregion frame_Loans

#region frame_Loans_Borrow
frame_Loans_Borrow = Frame(root)
def frame_Loans_Borrow_launcher():
    frame_Loans_Borrow.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_Loans)
        frame_Loans_Borrow_launcher()

    Loans_Borrow_instruction = Label(frame_Loans_Borrow, text="To Borrow A Book, Please Enter Information Below:", padx=150, pady=20, font=(dfont, 30), bg="aquamarine")
    
    global Loans_Borrow_Accessionnum
    global Loans_Borrow_ID
    
    Loans_Borrow_Accessionnum = Entry(frame_Loans_Borrow, width=50, font=(dfont,30))
    Loans_Borrow_Accessionnum.insert(0, "Enter Book Accession Number")
    Loans_Borrow_ID = Entry(frame_Loans_Borrow, width=50, font=(dfont,30))
    Loans_Borrow_ID.insert(0, "Enter Your Membership ID")
    button_Loans_Borrow_Back = Button(frame_Loans_Borrow, text="Back to Loans Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Loans_Borrow = Button(frame_Loans_Borrow, text="Borrow Book", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Loans_Borrow_Confirm_launcher, Frame(root, bg="green")))

    Loans_Borrow_instruction.grid(row=0, column=0, columnspan=2)
    Loans_Borrow_Accessionnum.grid(row=1, column=0, columnspan=2)
    Loans_Borrow_ID.grid(row=2, column=0, columnspan=2)
    button_Loans_Borrow_Back.grid(row=3, column=1)
    button_Loans_Borrow.grid(row=3, column=0)
frame_Loans_Borrow_launcher()

#Create Confirm Loan Details Popup
def frame_Loans_Borrow_Confirm_launcher(frame_Loans_Borrow_Confirm):
    frame_Loans_Borrow_Confirm.grid(row=0, column=0)

    label_Loans_Borrow_Confirm = Label(frame_Loans_Borrow_Confirm, text="Please Confirm Details to Be Correct", font=(dfont, 20), bg="green")
    label_Loans_Borrow_Confirm_Details = Label(frame_Loans_Borrow_Confirm, text=database.borrow_book_details(Loans_Borrow_Accessionnum.get(), Loans_Borrow_ID.get()), font=(dfont, 15), bg="green")
    button_Loans_Borrow_Confirm = Button(frame_Loans_Borrow_Confirm, text="Confirm Loan", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:loans_borrow())
    button_Loans_Borrow_Confirm_Back = Button(frame_Loans_Borrow_Confirm, text="Back to Borrow Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_Loans_Borrow))

    label_Loans_Borrow_Confirm.grid(row=0, column=0, columnspan=2)
    label_Loans_Borrow_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_Loans_Borrow_Confirm.grid(row=2, column=0)
    button_Loans_Borrow_Confirm_Back.grid(row=2, column=1)
    def loans_borrow():
        result = database.borrowBook(Loans_Borrow_Accessionnum.get(), Loans_Borrow_ID.get())
        if result == "Success":
            showframe(frame_Loans_Borrow)
        elif isinstance(result, datetime.date):
            showframe(frame_Loans_Borrow)
            return update_frame(frame_Loans_Borrow_Error_Onloan_launcher, Frame(root, bg="red"), result)
        else:
            showframe(frame_Loans_Borrow)
            return update_frame(frame_Loans_Borrow_Error_launcher, Frame(root, bg="red"), result)
    return frame_Loans_Borrow_Confirm

#Create Loan Borrow Error Popup Onloan
def frame_Loans_Borrow_Error_Onloan_launcher(frame_Loans_Borrow_Error_Onloan, date):
    frame_Loans_Borrow_Error_Onloan.grid(row=0, column=0)

    label_Loans_Borrow_Error_Onloan = Label(frame_Loans_Borrow_Error_Onloan, text="Error! \n Book is currently on Loan \n until: " + date.strftime("%m/%d/%Y") + ".", font=(dfont, 25), bg="red")
    button_Loans_Borrow_Error_Onloan_Back = Button(frame_Loans_Borrow_Error_Onloan, text="Back to Borrow Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Loans_Borrow))

    label_Loans_Borrow_Error_Onloan.pack()
    button_Loans_Borrow_Error_Onloan_Back.pack()
    return frame_Loans_Borrow_Error_Onloan


#Create Loan Borrow Error Popup Quota
def frame_Loans_Borrow_Error_launcher(frame_Loans_Borrow_Error, text):
    frame_Loans_Borrow_Error.grid(row=0, column=0)

    label_Loans_Borrow_Error = Label(frame_Loans_Borrow_Error, text="Error!\n" + text, font=(dfont, 25), bg="red")
    button_Loans_Borrow_Error_Back = Button(frame_Loans_Borrow_Error, text="Back to Borrow Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Loans_Borrow))

    label_Loans_Borrow_Error.pack()
    button_Loans_Borrow_Error_Back.pack()
    return frame_Loans_Borrow_Error
#endregion frame_Loans_Borrow

#region frame_Loans_Return
frame_Loans_Return = Frame(root)
def frame_Loans_Return_launcher():
    frame_Loans_Return.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        frame_Loans_Return_launcher()
        showframe(frame_Loans)

    Loans_Return_instruction = Label(frame_Loans_Return, text="To Return A Book, Please Enter Information Below:", padx=150, pady=20, font=(dfont, 30), bg="aquamarine")
    
    global Loans_Return_Accessionnum
    global Loans_Return_Date
    
    Loans_Return_Accessionnum = Entry(frame_Loans_Return, width=50, font=(dfont,30))
    Loans_Return_Accessionnum.insert(0, "Enter Book Accession Number")
    Loans_Return_Date = Entry(frame_Loans_Return, width=50, font=(dfont,30))
    Loans_Return_Date.insert(0, "Enter Your Return Date (YYYY-MM-DD)")
    button_Loans_Return_Back = Button(frame_Loans_Return, text="Back to Loans Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Loans_Return = Button(frame_Loans_Return, text="Return Book", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Loans_Return_Confirm_launcher, Frame(root, bg="green")))

    Loans_Return_instruction.grid(row=0, column=0, columnspan=2)
    Loans_Return_Accessionnum.grid(row=1, column=0, columnspan=2)
    Loans_Return_Date.grid(row=2, column=0, columnspan=2)
    button_Loans_Return_Back.grid(row=3, column=1)
    button_Loans_Return.grid(row=3, column=0)
frame_Loans_Return_launcher()

    #Create Confirm Return Details Popup
def frame_Loans_Return_Confirm_launcher(frame_Loans_Return_Confirm):    
    frame_Loans_Return_Confirm.grid(row=0, column=0)

    label_Loans_Return_Confirm = Label(frame_Loans_Return_Confirm, text="Please Confirm Details to Be Correct", font=(dfont, 20), bg="green")
    label_Loans_Return_Confirm_Details = Label(frame_Loans_Return_Confirm, text=database.return_book_details(Loans_Return_Accessionnum.get(),Loans_Return_Date.get()), font=(dfont, 15), bg="green")
    button_Loans_Return_Confirm = Button(frame_Loans_Return_Confirm, text="Confirm Return", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:book_loan_pass_or_fail())
    button_Loans_Return_Confirm_Back = Button(frame_Loans_Return_Confirm, text="Back to Return Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_Loans_Return))

    label_Loans_Return_Confirm.grid(row=0, column=0, columnspan=2)
    label_Loans_Return_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_Loans_Return_Confirm.grid(row=2, column=0)
    button_Loans_Return_Confirm_Back.grid(row=2, column=1)
    def book_loan_pass_or_fail():
        result = database.returnBook(Loans_Return_Accessionnum.get(),Loans_Return_Date.get())
        if result == "Book returned successfully":
            showframe(frame_Loans_Return)
        else:
            showframe(frame_Loans_Return)
            update_frame(frame_Loans_Return_Error_Fines_launcher, Frame(root, bg="red"), result)
    return frame_Loans_Return_Confirm

#Create Loan Return Error Popup Fines
def frame_Loans_Return_Error_Fines_launcher(frame_Loans_Return_Error_Fines, text):
    frame_Loans_Return_Error_Fines.grid(row=0, column=0)

    label_Loans_Return_Error_Fines = Label(frame_Loans_Return_Error_Fines, text="Error! \n" + text, font=(dfont, 20), bg="red")
    button_Loans_Return_Error_Fines_Back = Button(frame_Loans_Return_Error_Fines, text="Back to Return Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Loans_Return))

    label_Loans_Return_Error_Fines.pack()
    button_Loans_Return_Error_Fines_Back.pack()
    return frame_Loans_Return_Error_Fines
#endregion frame_Loans_Return

#RESERVATIONS SECTION

#region frame_RSV
frame_RSV = Frame(root)
RSV_img = ImageTk.PhotoImage(Image.open("RSV_pic.jpg"))

def frame_RSV_launcher():
    frame_RSV.grid(row=0, column=0, sticky="nsew")

    label_RSV_instruction = Label(frame_RSV, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_RSV_Reservation = Button(frame_RSV, text="8. Reserve a Book: Book Reservation", padx=115, pady=80, font=(dfont, 18), command=lambda:showframe(frame_RSV_Reservation), bg="khaki")
    button_RSV_Cancel = Button(frame_RSV, text="9. Cancel Reservation: Reservation Cancellation", padx=60, pady=80, font=(dfont, 18), bg="khaki", command=lambda:showframe(frame_RSV_Cancellation))
    button_RSV_Back = Button(frame_RSV, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_RSV_img = Label(frame_RSV, image=RSV_img)

    label_RSV_instruction.grid(row=0, column=0, columnspan=2)
    button_RSV_Reservation.grid(row=1, column=1)
    button_RSV_Cancel.grid(row=2, column=1)
    button_RSV_Back.grid(row=3, column=0, columnspan=2)
    label_RSV_img.grid(row=1, column=0, rowspan=2)
frame_RSV_launcher()
#endregion frame_RSV

#region frame_RSV_Reservation
frame_RSV_Reservation = Frame(root)
def frame_RSV_Reservation_launcher():
    frame_RSV_Reservation.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_RSV)
        frame_RSV_Reservation_launcher()

    RSV_Reservation_instruction = Label(frame_RSV_Reservation, text="To Reserve A Book, Please Enter Information Below:", padx=150, pady=20, font=(dfont, 30), bg="aquamarine")
   
    global RSV_Reservation_Accessionnum
    global RSV_Reservation_ID
    global RSV_Reservation_ReserveDate
   
    RSV_Reservation_Accessionnum = Entry(frame_RSV_Reservation, width=50, font=(dfont,30))
    RSV_Reservation_Accessionnum.insert(0, "Enter Book Accession Number")
    RSV_Reservation_ID = Entry(frame_RSV_Reservation, width=50, font=(dfont,30))
    RSV_Reservation_ID.insert(0, "Enter Your Membership ID")
    RSV_Reservation_ReserveDate = Entry(frame_RSV_Reservation, width=50, font=(dfont,30))
    RSV_Reservation_ReserveDate.insert(0, "Enter Date of Reservation (YYYY-MM-DD)")
    button_RSV_Reservation_Back = Button(frame_RSV_Reservation, text="Back to Reservations Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_RSV_Reservation = Button(frame_RSV_Reservation, text="Reserve Book", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_RSV_Reservation_Confirm_launcher, Frame(root, bg="green")))

    RSV_Reservation_instruction.grid(row=0, column=0, columnspan=2)
    RSV_Reservation_Accessionnum.grid(row=1, column=0, columnspan=2)
    RSV_Reservation_ID.grid(row=2, column=0, columnspan=2)
    RSV_Reservation_ReserveDate.grid(row=3, column=0, columnspan=2)
    button_RSV_Reservation_Back.grid(row=4, column=1)
    button_RSV_Reservation.grid(row=4, column=0)
frame_RSV_Reservation_launcher()

#Create Confirm Reservation Details Popup
def frame_RSV_Reservation_Confirm_launcher(frame_RSV_Reservation_Confirm):    
    frame_RSV_Reservation_Confirm.grid(row=0, column=0)

    label_RSV_Reservation_Confirm = Label(frame_RSV_Reservation_Confirm, text="Confirm Reservation Details to Be Correct", font=(dfont, 15), bg="green")
    label_RSV_Reservation_Confirm_Details = Label(frame_RSV_Reservation_Confirm, text=database.reserve_details(RSV_Reservation_Accessionnum.get(), RSV_Reservation_ID.get(), RSV_Reservation_ReserveDate.get(), "Reserve"), font=(dfont, 15), bg="green")
    button_RSV_Reservation_Confirm = Button(frame_RSV_Reservation_Confirm, text="Confirm Reservation", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:reservation_pass_fail())
    button_RSV_Reservation_Confirm_Back = Button(frame_RSV_Reservation_Confirm, text="Back to Reserve Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_RSV_Reservation))

    label_RSV_Reservation_Confirm.grid(row=0, column=0, columnspan=2)
    label_RSV_Reservation_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_RSV_Reservation_Confirm.grid(row=2, column=0)
    button_RSV_Reservation_Confirm_Back.grid(row=2, column=1)
    def reservation_pass_fail():
        result = database.reserveBook(RSV_Reservation_Accessionnum.get(), RSV_Reservation_ID.get(), RSV_Reservation_ReserveDate.get())
        if result == "Success":
            showframe(frame_RSV_Reservation)
        elif result == "Member has outstanding fines":
            showframe(frame_RSV_Reservation)
            update_frame(frame_RSV_Reservation_Error_Fines_launcher, Frame(root, bg="red"), database.getFine(RSV_Reservation_ID.get()))
        else:
            showframe(frame_RSV_Reservation)
            update_frame(frame_RSV_Reservation_Error_launcher, Frame(root, bg="red"), result)

    return frame_RSV_Reservation_Confirm

#Create RSV Reservation Error 2 Books
def frame_RSV_Reservation_Error_launcher(frame_RSV_Reservation_Error, text):
    frame_RSV_Reservation_Error.grid(row=0, column=0)

    label_RSV_Reservation_Error = Label(frame_RSV_Reservation_Error, text="Error! \n" + text, font=(dfont, 20), bg="red")
    button_RSV_Reservation_Error_Back = Button(frame_RSV_Reservation_Error, text="Back to Reserve Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_RSV_Reservation))

    label_RSV_Reservation_Error.pack()
    button_RSV_Reservation_Error_Back.pack()
    return frame_RSV_Reservation_Error

#Create RSV Reservation Error Fines
def frame_RSV_Reservation_Error_Fines_launcher(frame_RSV_Reservation_Error_Fines, text):
    frame_RSV_Reservation_Error_Fines.grid(row=0, column=0)

    label_RSV_Reservation_Error_Fines = Label(frame_RSV_Reservation_Error_Fines, text="Error! \n Member currently has \nOutstanding Fine of: $" + str(text), font=(dfont, 20), bg="red")
    button_RSV_Reservation_Error_Fines_Back = Button(frame_RSV_Reservation_Error_Fines, text="Back to Reserve Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_RSV_Reservation))

    label_RSV_Reservation_Error_Fines.pack()
    button_RSV_Reservation_Error_Fines_Back.pack()
    return frame_RSV_Reservation_Error_Fines

#endregion frame_RSV_Reservation

#region frame_RSV_Cancellation
frame_RSV_Cancellation = Frame(root)
def frame_RSV_Cancellation_launcher():
    frame_RSV_Cancellation.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_RSV)
        frame_RSV_Cancellation_launcher()

    global RSV_Cancellation_Accessionnum
    global RSV_Cancellation_ID
    global RSV_Cancellation_CancelDate

    RSV_Cancellation_instruction = Label(frame_RSV_Cancellation, text="To Cancel a Reservation, Please Enter Information Below:", padx=150, pady=20, font=(dfont, 30), bg="aquamarine")
    RSV_Cancellation_Accessionnum = Entry(frame_RSV_Cancellation, width=50, font=(dfont,30))
    RSV_Cancellation_Accessionnum.insert(0, "Enter Book Accession Number")
    RSV_Cancellation_ID = Entry(frame_RSV_Cancellation, width=50, font=(dfont,30))
    RSV_Cancellation_ID.insert(0, "Enter Your Membership ID")
    RSV_Cancellation_CancelDate = Entry(frame_RSV_Cancellation, width=50, font=(dfont,30))
    RSV_Cancellation_CancelDate.insert(0, "Enter Date of Cancellation (YYYY-MM-DD)")
    button_RSV_Cancellation_Back = Button(frame_RSV_Cancellation, text="Back to Reservations Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_RSV_Cancellation = Button(frame_RSV_Cancellation, text="Cancel Reservation", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_RSV_Cancellation_Confirm_launcher, Frame(root, bg="green")))

    RSV_Cancellation_instruction.grid(row=0, column=0, columnspan=2)
    RSV_Cancellation_Accessionnum.grid(row=1, column=0, columnspan=2)
    RSV_Cancellation_ID.grid(row=2, column=0, columnspan=2)
    RSV_Cancellation_CancelDate.grid(row=3, column=0, columnspan=2)
    button_RSV_Cancellation_Back.grid(row=4, column=1)
    button_RSV_Cancellation.grid(row=4, column=0)
frame_RSV_Cancellation_launcher()

#Create Confirm Cancellation Details Popup
def frame_RSV_Cancellation_Confirm_launcher(frame_RSV_Cancellation_Confirm):    
    frame_RSV_Cancellation_Confirm.grid(row=0, column=0)
    label_RSV_Cancellation_Confirm = Label(frame_RSV_Cancellation_Confirm, text="Confirm Cancellation Details to Be Correct", font=(dfont, 15), bg="green")
    label_RSV_Cancellation_Confirm_Details = Label(frame_RSV_Cancellation_Confirm, text=database.reserve_details(RSV_Cancellation_Accessionnum.get(), RSV_Cancellation_ID.get(), RSV_Cancellation_CancelDate.get(), "Cancellation"), font=(dfont, 15), bg="green")
    button_RSV_Cancellation_Confirm = Button(frame_RSV_Cancellation_Confirm, text="Confirm Cancellation", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:cancellation_pass_fail())
    button_RSV_Cancellation_Confirm_Back = Button(frame_RSV_Cancellation_Confirm, text="Back to Cancellation Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_RSV_Cancellation))

    label_RSV_Cancellation_Confirm.grid(row=0, column=0, columnspan=2)
    label_RSV_Cancellation_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_RSV_Cancellation_Confirm.grid(row=2, column=0)
    button_RSV_Cancellation_Confirm_Back.grid(row=2, column=1)
    def cancellation_pass_fail():
        result = database.cancelReserve(RSV_Cancellation_Accessionnum.get(), RSV_Cancellation_ID.get(), RSV_Cancellation_CancelDate.get())
        if result == "Success":
            showframe(frame_RSV_Cancellation)
        else:
            showframe(frame_RSV_Cancellation)
            update_frame(frame_RSV_Cancellation_Error_launcher, Frame(root, bg="red"), result)
    return frame_RSV_Cancellation_Confirm

#Create RSV Cancellation Error NoReservation
def frame_RSV_Cancellation_Error_launcher(frame_RSV_Cancellation_Error, text):
    frame_RSV_Cancellation_Error.grid(row=0, column=0)

    label_RSV_Cancellation_Error_NoReservation = Label(frame_RSV_Cancellation_Error, text="Error! \n" + text, font=(dfont, 20), bg="red")
    button_RSV_Cancellation_Error_NoReservation_Back = Button(frame_RSV_Cancellation_Error, text="Back to Reserve Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_RSV_Cancellation))

    label_RSV_Cancellation_Error_NoReservation.pack()
    button_RSV_Cancellation_Error_NoReservation_Back.pack()
    return frame_RSV_Cancellation_Error

#endregion frame_RSV_Cancellation

#FINES
#region frame_Fines
frame_Fines = Frame(root)
Fines_img = ImageTk.PhotoImage(Image.open("Fines_pic.jpg"))

def frame_Fines_launcher():
    frame_Fines.grid(row=0, column=0, sticky="nsew")

    label_Fines_instruction = Label(frame_Fines, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_Fines_Payment = Button(frame_Fines, text="10. Fine Payment", padx=180, pady=80, font=(dfont, 25), command=lambda:showframe(frame_Fines_Payment), bg="orange")
    button_Fines_Back = Button(frame_Fines, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_Fines_img = Label(frame_Fines, image=Fines_img)

    label_Fines_instruction.grid(row=0, column=0, columnspan=2)
    button_Fines_Payment.grid(row=1, column=1)
    button_Fines_Back.grid(row=2, column=0, columnspan=2)
    label_Fines_img.grid(row=1, column=0)
frame_Fines_launcher()
#endregion frame_Fines

#region frame_Fines_Payment
frame_Fines_Payment = Frame(root)
def frame_Fines_Payment_launcher():
    frame_Fines_Payment.grid(row=0, column=0, sticky="nsew")

    def back_to_previous_menu():
        showframe(frame_Fines)
        frame_Fines_Payment_launcher()

    Fines_Payment_instruction = Label(frame_Fines_Payment, text="To Pay a Fine, Please Enter Information Below:", padx=150, pady=20, font=(dfont, 30), bg="aquamarine")
    
    global Fines_Payment_MemID
    global Fines_Payment_PaymentDate
    global Fines_Payment_PaymentAmt
    
    Fines_Payment_MemID = Entry(frame_Fines_Payment, width=50, font=(dfont,30))
    Fines_Payment_MemID.insert(0, "Enter Member ID")
    Fines_Payment_PaymentDate = Entry(frame_Fines_Payment, width=50, font=(dfont,30))
    Fines_Payment_PaymentDate.insert(0, "Enter Date Payment Received (YYYY-MM-DD)")
    Fines_Payment_PaymentAmt = Entry(frame_Fines_Payment, width=50, font=(dfont,30))
    Fines_Payment_PaymentAmt.insert(0, "Enter Total Fine Amount")
    button_Fines_Payment_Back = Button(frame_Fines_Payment, text="Back to Fines Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Fines_Payment = Button(frame_Fines_Payment, text="Pay Fine", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Fines_Payment_Confirm_launcher, Frame(root, bg="green")))

    Fines_Payment_instruction.grid(row=0, column=0, columnspan=2)
    Fines_Payment_MemID.grid(row=1, column=0, columnspan=2)
    Fines_Payment_PaymentDate.grid(row=2, column=0, columnspan=2)
    Fines_Payment_PaymentAmt.grid(row=3, column=0, columnspan=2)
    button_Fines_Payment_Back.grid(row=4, column=1)
    button_Fines_Payment.grid(row=4, column=0)
frame_Fines_Payment_launcher()

#Create Confirm Payment Details Popup
def frame_Fines_Payment_Confirm_launcher(frame_Fines_Payment_Confirm):    
    frame_Fines_Payment_Confirm.grid(row=0, column=0)
    payment_due = database.getFine(Fines_Payment_MemID.get())
    report = "Payment Due: " + str(payment_due) + "\n" \
        + "Member ID: " + str(Fines_Payment_MemID.get()) + "\n" \
        + "Payment Date: " + str(Fines_Payment_PaymentDate.get()) + "\n" \
        + "\n" + "Exact Fee Only"
    label_Fines_Payment_Confirm = Label(frame_Fines_Payment_Confirm, text="Please Confirm Details to Be Correct", font=(dfont, 15), bg="green")
    label_Fines_Payment_Confirm_Details = Label(frame_Fines_Payment_Confirm, text=report, font=(dfont, 15), bg="green")
    button_Fines_Payment_Confirm = Button(frame_Fines_Payment_Confirm, text="Confirm Payment", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:fine_pass_fail())
    button_Fines_Payment_Confirm_Back = Button(frame_Fines_Payment_Confirm, text="Back to Payment Function", padx=100, pady=50, font=(dfont, 15),
                                borderwidth=2, bg="green", command=lambda:showframe(frame_Fines_Payment))

    label_Fines_Payment_Confirm.grid(row=0, column=0, columnspan=2)
    label_Fines_Payment_Confirm_Details.grid(row=1, column=0, columnspan=2)
    button_Fines_Payment_Confirm.grid(row=2, column=0)
    button_Fines_Payment_Confirm_Back.grid(row=2, column=1)
    def fine_pass_fail():
        result = database.payFines(Fines_Payment_MemID.get(), Fines_Payment_PaymentDate.get(), int(Fines_Payment_PaymentAmt.get()))
        if result == "Success":
            showframe(frame_Fines_Payment)
        else:
            showframe(frame_Fines_Payment)
            return update_frame(frame_Fines_Payment_Error_launcher, Frame(root, bg="red"), result)
    return frame_Fines_Payment_Confirm

#Create Fines Payment Error
def frame_Fines_Payment_Error_launcher(frame_Fines_Payment_Error, text):
    frame_Fines_Payment_Error.grid(row=0, column=0)

    label_Fines_Payment_Error = Label(frame_Fines_Payment_Error, text="Error! " + text, font=(dfont, 20), bg="red")
    button_Fines_Payment_Error_Back = Button(frame_Fines_Payment_Error, text="Back to Payment Function", padx=50, pady=20, font=(dfont, 18),
                                borderwidth=5, bg="red", command=lambda:showframe(frame_Fines_Payment))

    label_Fines_Payment_Error.pack()
    button_Fines_Payment_Error_Back.pack()
    return frame_Fines_Payment_Error
#endregion frame_Fines_Payment

#REPORTS

#region frame_Reports
frame_Reports = Frame(root)
Reports_img = ImageTk.PhotoImage(Image.open("Reports_pic.jpg"))

def frame_Reports_launcher():
    frame_Reports.grid(row=0, column=0, sticky="nsew")

    label_Reports_instruction = Label(frame_Reports, text="Select one of the Options below:", padx=200, pady=20, font=(dfont, 30), bg="aquamarine")
    button_Reports_BookSearch = Button(frame_Reports, text="11. Book Search", padx=150, pady=25, font=(dfont, 20), command=lambda:showframe(frame_Reports_BookSearch), bg="cornflowerblue")
    button_Reports_BooksLoan = Button(frame_Reports, text="12. Books on Loan", padx=140, pady=25, font=(dfont, 20), command=lambda:update_frame(frame_Reports_BooksLoan_launcher, Frame(root, bg="green")), bg="cornflowerblue")
    button_Reports_BooksReservation = Button(frame_Reports, text="13. Books on Reservation", padx=100, pady=25, font=(dfont, 20), command=lambda:update_frame(frame_Reports_BooksReservation_launcher, Frame(root, bg="green")), bg="cornflowerblue")
    button_Reports_OutFines = Button(frame_Reports, text="14. Outstanding Fines", padx=120, pady=25, font=(dfont, 20), command=lambda:update_frame(frame_Reports_OutFines_launcher, Frame(root, bg="green")), bg="cornflowerblue")
    button_Reports_BooksLoanMem = Button(frame_Reports, text="15. Books on Loan to Member", padx=70, pady=25, font=(dfont, 20), command=lambda:showframe(frame_Reports_BooksLoanMem), bg="cornflowerblue")
    button_Reports_Back = Button(frame_Reports, text="Back to Main Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_MM), bg="white")
    label_Reports_img = Label(frame_Reports, image=Reports_img)

    label_Reports_instruction.grid(row=0, column=0, columnspan=2)
    button_Reports_BookSearch.grid(row=1, column=1)
    button_Reports_BooksLoan.grid(row=2, column=1)
    button_Reports_BooksReservation.grid(row=3, column=1)
    button_Reports_OutFines.grid(row=4, column=1)
    button_Reports_BooksLoanMem.grid(row=5, column=1)
    button_Reports_Back.grid(row=6, column=0, columnspan=2)
    label_Reports_img.grid(row=1, column=0, rowspan=5)
frame_Reports_launcher()
#endregion frame_Reports

#region Empty Page (to place behind reports)
frame_Reports_EmptyPage = Frame(root)

def frame_Reports_EmptyPage_launcher():
    frame_Reports_EmptyPage.grid(row=0, column=0, sticky="nsew")

frame_Reports_EmptyPage_launcher()
#endregion Empty Page

#region frame_Reports_BookSearch
frame_Reports_BookSearch = Frame(root)

def frame_Reports_BookSearch_launcher():
    frame_Reports_BookSearch.grid(row=0, column=0, sticky="nsew")

    global e_Reports_BookSearch_BookTitle
    global e_Reports_BookSearch_Authors
    global e_Reports_BookSearch_ISBN
    global e_Reports_BookSearch_Publisher
    global e_Reports_BookSearch_PublicationYear

    Reports_BookSearch_instruction = Label(frame_Reports_BookSearch, text="Search based on one of the categories below:", padx=200, pady=20, font=(dfont, 20), bg="aquamarine")
    e_Reports_BookSearch_BookTitle = Entry(frame_Reports_BookSearch, width=50, font=(dfont,30))
    e_Reports_BookSearch_BookTitle.insert(0, "Enter Book Title")
    e_Reports_BookSearch_Authors = Entry(frame_Reports_BookSearch, width=50, font=(dfont,30))
    e_Reports_BookSearch_Authors.insert(0, "Enter Book Author")
    e_Reports_BookSearch_ISBN = Entry(frame_Reports_BookSearch, width=50, font=(dfont,30))
    e_Reports_BookSearch_ISBN.insert(0, "Enter ISBN Number")
    e_Reports_BookSearch_Publisher = Entry(frame_Reports_BookSearch, width=50, font=(dfont,30))
    e_Reports_BookSearch_Publisher.insert(0, "Enter Publisher Name")
    e_Reports_BookSearch_PublicationYear = Entry(frame_Reports_BookSearch, width=50, font=(dfont,30))
    e_Reports_BookSearch_PublicationYear.insert(0, "Enter Publication Year")

    button_Reports_BookSearch_Back = Button(frame_Reports_BookSearch, text="Back to Reports Menu", padx=200, pady=5, font=(dfont, 15), command=lambda:showframe(frame_Reports))
    button_Reports_BookSearch_SearchBook = Button(frame_Reports_BookSearch, text="Search Book", padx=200, pady=5, font=(dfont, 15), command=lambda:  update_frame(frame_Reports_BookSearch_Results_launcher, Frame(root, bg="green"), e_Reports_BookSearch_BookTitle.get(), e_Reports_BookSearch_Authors.get(), e_Reports_BookSearch_ISBN.get(), e_Reports_BookSearch_Publisher.get(), e_Reports_BookSearch_PublicationYear.get()))

    button_Reports_BookSearch_Back.grid(row=6, column=1)
    button_Reports_BookSearch_SearchBook.grid(row=6, column=0)

    Reports_BookSearch_instruction.grid(row=0, column=0, columnspan=2)
    e_Reports_BookSearch_BookTitle.grid(row=1, column=0, columnspan=2)
    e_Reports_BookSearch_Authors.grid(row=2, column=0, columnspan=2)
    e_Reports_BookSearch_ISBN.grid(row=3, column=0, columnspan=2)
    e_Reports_BookSearch_Publisher.grid(row=4, column=0, columnspan=2)
    e_Reports_BookSearch_PublicationYear.grid(row=5, column=0, columnspan=2)
frame_Reports_BookSearch_launcher()

#Create Book Search Results Popup
frame_Reports_BookSearch_Results = Frame(root)

def frame_Reports_BookSearch_Results_launcher(frame_Reports_BookSearch_Results, title, authors, isbn, publisher, publish_year):
    
    def previous_menu():
            frame_Reports_BookSearch_launcher()
            showframe(frame_Reports_BookSearch)
    showframe(frame_Reports_EmptyPage)

    if title == "Enter Book Title":
        title = ""
    if authors == "Enter Book Author":
        authors = ""
    if isbn == "Enter ISBN Number":
        isbn = ""
    if publisher == "Enter Publisher Name":
        publisher = ""
    if publish_year == "Enter Publication Year":
        publish_year = ""

    frame_Reports_BookSearch_Results.grid(row=0, column=0)

    Reports_BookSearch_Result_instruction = Label(frame_Reports_BookSearch_Results, text="Book Search Results", padx=200, pady=20, font=(dfont, 20), bg="green")
    
     #table
    result = database.selectBook(title, authors, isbn, publisher, publish_year)
    i=0 
    for book in result:
        for j in range(len(book)):
            # check_authors = book[2]

            text = book[j]
            display_text = str(text)
            if j == 2:  # 2 is the list index containing the author string
                display_text = display_text.replace(", ", "\n")
                # replace will replace all "," in string and return the changed string
                # printing display_text will return "abc\nefg\nhij"
                # if "," doesnt exist in authors, printing display_text will return the original string: authors
            e = Label(frame_Reports_BookSearch_Results, text = display_text, width=30, fg='blue', anchor=W) 
            e.grid(row=i+2, column=j, padx=1, pady=1, sticky=N)
        i=i+1
    button_Reports_BookSearch_Results_Back = Button(frame_Reports_BookSearch_Results, text="Back to Reports Menu", padx=232, pady=5, font=(dfont, 15), bg="green", command=lambda:previous_menu())

    if result:
        #headers
        e=Label(frame_Reports_BookSearch_Results,width=30,text='Accession Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(frame_Reports_BookSearch_Results,width=30,text='Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(frame_Reports_BookSearch_Results,width=30,text='Author(s)',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(frame_Reports_BookSearch_Results,width=30,text='ISBN',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=3)
        e=Label(frame_Reports_BookSearch_Results,width=30,text='Publisher',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=4)
        e=Label(frame_Reports_BookSearch_Results,width=30,text='Published Year',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=5)

    Reports_BookSearch_Result_instruction.grid(row=0, column=0, columnspan=6)
    button_Reports_BookSearch_Results_Back.grid(row=i+3, column=0, columnspan=6, pady=5)
    return frame_Reports_BookSearch_Results


#endregion frame_Reports_BookSearch

#region frame_Reports_BooksLoan
def frame_Reports_BooksLoan_launcher(frame_Reports_BooksLoan):
    showframe(frame_Reports_EmptyPage)
    frame_Reports_BooksLoan.grid(row=0, column=0)

    Reports_BookSearch_instruction = Label(frame_Reports_BooksLoan, text="Books on Loan Report", padx=200, pady=20, font=(dfont, 20), bg="green")

    #table
    result = database.loanedBooks()
    i=0 
    for book in result:
        for j in range(len(book)):
            # check_authors = book[2]

            text = book[j]
            display_text = str(text)
            if j == 2:  # 2 is the list index containing the author string
                display_text = display_text.replace(", ", "\n")
                # replace will replace all "," in string and return the changed string
                # printing display_text will return "abc\nefg\nhij"
                # if "," doesnt exist in authors, printing display_text will return the original string: authors
            e = Label(frame_Reports_BooksLoan, text = display_text, width=30, fg='blue', anchor=W) 
            e.grid(row=i+2, column=j, padx=1, pady=1, sticky=N)
        i=i+1
    button_Reports_BooksLoan_Back = Button(frame_Reports_BooksLoan, text="Back to Reports Menu", padx=232, pady=5, font=(dfont, 15), bg="green", command=lambda:showframe(frame_Reports))

    if result:
        #headers
        e=Label(frame_Reports_BooksLoan,width=30,text='Accession Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(frame_Reports_BooksLoan,width=30,text='Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(frame_Reports_BooksLoan,width=30,text='Author(s)',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(frame_Reports_BooksLoan,width=30,text='ISBN',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=3)
        e=Label(frame_Reports_BooksLoan,width=30,text='Publisher',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=4)
        e=Label(frame_Reports_BooksLoan,width=30,text='Published Year',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=5)

    Reports_BookSearch_instruction.grid(row=0, column=0, columnspan=6)
    button_Reports_BooksLoan_Back.grid(row=i+3, column=0, columnspan=6, pady=5)
    return frame_Reports_BooksLoan
#endregion frame_Reports_BooksLoan

#region frame_Reports_BooksReservation
def frame_Reports_BooksReservation_launcher(frame_Reports_BooksReservation):
    showframe(frame_Reports_EmptyPage)
    frame_Reports_BooksReservation.grid(row=0, column=0)

    Reports_BooksReservation_instruction = Label(frame_Reports_BooksReservation, text="Books on Reservation Report", padx=151, pady=20, font=(dfont, 20), bg="green")
    
    #table
    result = database.reservedBooks()
    i=0 
    for book in result:
        for j in range(len(book)):
            # check_authors = book[2]

            text = book[j]
            display_text = str(text)
            if j == 2:  # 2 is the list index containing the author string
                display_text = display_text.replace(", ", "\n")
                # replace will replace all "," in string and return the changed string
                # printing display_text will return "abc\nefg\nhij"
                # if "," doesnt exist in authors, printing display_text will return the original string: authors
            e = Label(frame_Reports_BooksReservation, text = display_text, width=30, fg='blue', anchor=W) 
            e.grid(row=i+2, column=j, padx=1, pady=1, sticky=N)
        i=i+1
    button_Reports_BooksReservation_Back = Button(frame_Reports_BooksReservation, text="Back to Reports Menu", padx=232, pady=5, font=(dfont, 15), bg="green", command=lambda:showframe(frame_Reports))

    if result:
        #headers
        e=Label(frame_Reports_BooksReservation,width=30,text='Accession Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(frame_Reports_BooksReservation,width=30,text='Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(frame_Reports_BooksReservation,width=30,text='Membership ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(frame_Reports_BooksReservation,width=30,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=3)

    Reports_BooksReservation_instruction.grid(row=0, column=0, columnspan=4)
    button_Reports_BooksReservation_Back.grid(row=i+3, column=0, columnspan=4, pady=5)
    return frame_Reports_BooksReservation
#endregion frame_Reports_BooksReservation

#region frame_Reports_OutFines
def frame_Reports_OutFines_launcher(frame_Reports_OutFines):
    showframe(frame_Reports_EmptyPage)
    frame_Reports_OutFines.grid(row=0, column=0)

    Reports_OutFines_instruction = Label(frame_Reports_OutFines, text="Members with Outstanding Fines", padx=150, pady=20, font=(dfont, 20), bg="green")
    #table
    result = database.outstandingFines()
    i=0 
    for fine in result:
        for j in range(len(fine)):
            # check_authors = book[2]

            text = fine[j]
            display_text = str(text)
            if j == 2:  # 2 is the list index containing the author string
                display_text = display_text.replace(", ", "\n")
                # replace will replace all "," in string and return the changed string
                # printing display_text will return "abc\nefg\nhij"
                # if "," doesnt exist in authors, printing display_text will return the original string: authors
            e = Label(frame_Reports_OutFines, text = display_text, width=30, fg='blue', anchor=W) 
            e.grid(row=i+2, column=j, padx=1, pady=1, sticky=N)
        i=i+1
    button_Reports_OutFines_Back = Button(frame_Reports_OutFines, text="Back to Reports Menu", padx=232, pady=5, font=(dfont, 15), bg="green", command=lambda:showframe(frame_Reports))

    if result:
        #headers
        e=Label(frame_Reports_OutFines,width=30,text='Membership ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(frame_Reports_OutFines,width=30,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(frame_Reports_OutFines,width=30,text='Faculty',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(frame_Reports_OutFines,width=30,text='Phone Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=3)
        e=Label(frame_Reports_OutFines,width=30,text='Email Address',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=4)

    Reports_OutFines_instruction.grid(row=0, column=0, columnspan=5)
    button_Reports_OutFines_Back.grid(row=i+3, column=0, columnspan=5, pady=5)
    return frame_Reports_OutFines
#endregion frame_Reports_OutFines

#region frame_Reports_BooksLoanMem
frame_Reports_BooksLoanMem = Frame(root)
def frame_Reports_BooksLoanMem_launcher():

    global Reports_BooksLoanMem_MemID
    
    def back_to_previous_menu():
        showframe(frame_Reports)
        frame_Reports_BooksLoanMem_launcher()
    
    frame_Reports_BooksLoanMem.grid(row=0, column=0, sticky="nsew")

    Reports_BooksLoanMem_instruction = Label(frame_Reports_BooksLoanMem, text="Books on Loan to Member", padx=150, pady=20, font=(dfont, 20), bg="aquamarine")
    Reports_BooksLoanMem_MemID = Entry(frame_Reports_BooksLoanMem, width=50, font=(dfont,30))
    Reports_BooksLoanMem_MemID.insert(0, "Enter Membership ID")
    button_Reports_BooksLoanMem_Back = Button(frame_Reports_BooksLoanMem, text="Back to Reports Menu", padx=150, pady=5, font=(dfont, 15), command=lambda:back_to_previous_menu())
    button_Reports_BooksLoanMem_SearchMem = Button(frame_Reports_BooksLoanMem, text="Search Member", padx=200, pady=5, font=(dfont, 15), command=lambda:update_frame(frame_Reports_BooksLoanMem_Result_launcher, Frame(root, bg="green"), Reports_BooksLoanMem_MemID.get()))

    Reports_BooksLoanMem_instruction.grid(row=0, column=0, columnspan=2)
    Reports_BooksLoanMem_MemID.grid(row=1, column=0, columnspan=2)
    button_Reports_BooksLoanMem_Back.grid(row=2, column=1)
    button_Reports_BooksLoanMem_SearchMem.grid(row=2, column=0)
frame_Reports_BooksLoanMem_launcher()

#Create Books on Loan to Member Results
def frame_Reports_BooksLoanMem_Result_launcher(frame_Reports_BooksLoanMem_Result, memberID):
    showframe(frame_Reports_EmptyPage)
    frame_Reports_BooksLoanMem_Result.grid(row=0, column=0)

    Reports_BooksLoanMem_Result_instruction = Label(frame_Reports_BooksLoanMem_Result, text="Books on Loan to Member", padx=150, pady=20, font=(dfont, 20), bg="green")
    
    #table
    result = database.loanedMember(memberID)

    if result == "Member does not exist":
        showframe(frame_Reports_BooksLoanMem)
        return

    i=0 
    for fine in result:
        for j in range(len(fine)):
            text = fine[j]
            display_text = str(text)
            if j == 2:  # 2 is the list index containing the author string
                display_text = display_text.replace(", ", "\n")
                # replace will replace all "," in string and return the changed string
                # printing display_text will return "abc\nefg\nhij"
                # if "," doesnt exist in authors, printing display_text will return the original string: authors
            e = Label(frame_Reports_BooksLoanMem_Result, text = display_text, width=30, fg='blue', anchor=W) 
            e.grid(row=i+2, column=j, padx=1, pady=1, sticky=N)
        i=i+1
    
    button_Reports_BooksLoanMem_Result_Back = Button(frame_Reports_BooksLoanMem_Result, text="Back to Reports Menu", padx=208, pady=5, font=(dfont, 15), bg="green", command=lambda:showframe(frame_Reports))

    if result:
        #headers
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='Accession Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=0)
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=1)
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='Author(s)',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=2)
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='ISBN',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=3)
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='Publisher',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=4)
        e=Label(frame_Reports_BooksLoanMem_Result,width=30,text='Published Year',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=1,column=5)
    
    Reports_BooksLoanMem_Result_instruction.grid(row=0, column=0, columnspan=6)
    button_Reports_BooksLoanMem_Result_Back.grid(row=i+3, column=0, columnspan=6, pady=5)
    return frame_Reports_BooksLoanMem_Result
#endregion frame_Reports_BooksLoanMem
showframe(frame_MM)
root.mainloop()

