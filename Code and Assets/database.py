from sqlalchemy import create_engine, false, text
import sqlalchemy as db
import datetime

## testing github
##NOTE: PROBABLY DO NOT NEED TO USE SQLALCHEMY DECLARATIVE STYLE

#region creating engine to connect to database, initializing tables into a MetaData_obj
engine = create_engine("mysql+pymysql://root:Inferno935@127.0.0.1:3306/library")
metadata_obj = db.MetaData()
metadata_obj.reflect(bind = engine)
connection = engine.connect()
#endregion


#Creating a member
def createMember(id, name, faculty, phoneNum, email):
        id_list = []
        same_id = connection.execute(f"SELECT * FROM Members WHERE memberID = '{id}'")
        for row in same_id:
                id_list += row
        if id == "" or name == "" or faculty == "" or phoneNum == "" or email == "":
                return False
        if not id_list:
                connection.execute(f"INSERT INTO Members VALUES('{id}', '{name}', '{faculty}', {phoneNum}, '{email}')")
                return True
        return False

def hasFine(memberID):
        fines = connection.execute(f"SELECT * FROM Fines WHERE memberID = '{memberID}'")
        for fine in fines:
                if fine[1] > 0:
                        return True
        return False
        
def delete_member_details(id):
        same_id = connection.execute(f"SELECT * FROM Members WHERE memberID = '{id}'")
        print_records = ""
        for record in same_id:
                print_records += "Accession Number: " + str(record[0]) + "\n" \
                        + "Name: " + str(record[1]) + "\n" \
                        + "Faculty: " + str(record[2]) + "\n" \
                        + "Phone Number: " + str(record[3]) + "\n" \
                        + "Email: " + str(record[4])
        return print_records


def delete_member(id):
        id_list = []
        same_id = connection.execute(f"SELECT * FROM Books WHERE memberID = '{id}'")
        for row in same_id:
                id_list += row
        if id_list:
                return False
        if hasFine(id):
                return False
        connection.execute(f"DELETE FROM Reserves WHERE memberID = '{id}'")
        connection.execute(f"DELETE FROM Members WHERE memberID = '{id}'")
        return True

#print(delete_member("A601F"))

#Updating member detials
def doesMemberExist(id):
        id_list = []
        same_id = connection.execute(f"SELECT * FROM Members WHERE memberID = '{id}'")
        for row in same_id:
                id_list += row
        if id_list:
                return True
        return False

def updateMember(id, name, faculty, phoneNum, email):
        if name == "" or faculty == "" or phoneNum == "" or email == "":
                return False 
        connection.execute(f"UPDATE Members SET name = '{name}', faculty = '{faculty}', phoneNo = {phoneNum}, email = '{email}' WHERE memberID = '{id}'")
        return True

#test-code
#print(updateMember("A401D", "Jerome", "SoC", "219210413", "test@gmail.com"))

#Adding new books
def doesBookExist(id):
        id_list = []
        same_id = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{id}'")
        for row in same_id:
                id_list += row
        if id_list:
                return True
        return False

def addBook(accessionNum, title, authors, isbn, publisher, publishYear):
        if accessionNum == "" or title == "" or authors == "" or isbn == "" or publisher == "" or publishYear == "":
                return False
        if doesBookExist(accessionNum):
                return False
        connection.execute(f"INSERT INTO Books(accessionNo, title, isbn, publisher, publishYear) VALUES ('{accessionNum}', '{title}', {isbn}, '{publisher}', {publishYear})")
        author_list = authors.split(',')
        for author in author_list:
                connection.execute(f"INSERT INTO Authors VALUES ('{accessionNum}', '{author}')")
        return True

#test-code
#print(addBook("A51", "How to pass bt2102", "Danny Poo,Tan Eng Chye", "8917234", "NUS", "2022"))

def isBorrowed(accessionNo):
        same_book = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        for row in same_book:
                if row[5]:
                        return True
        return False

def isReserved(accessionNo):
        reserve_list = []
        reserved_book = connection.execute(f"SELECT * FROM Reserves WHERE accessionNo = '{accessionNo}'")
        for row in reserved_book:
                reserve_list += row
        if reserve_list:
                return True
        return False
        
#Withdrawing book
def removeBook(accessionNo):
        if not doesBookExist(accessionNo):
                return "Book does not exist"       
        if isBorrowed(accessionNo):
                return "Book is currently on loan"
        if isReserved(accessionNo):
                return "Book is currently reserved"
        connection.execute(f"DELETE FROM Books WHERE accessionNo = '{accessionNo}'")
        connection.execute(f"DELETE FROM Authors WHERE accessionNo = '{accessionNo}'")
        return "Success"

#test-code
#print(removeBook("A51"))

def nextReserve(accessionNo):
        reserved_books = connection.execute(f"SELECT * FROM Reserves WHERE accessionNo = '{accessionNo}'")
        earliest_member = ""
        earliest_date = ""
        count = 0
        for row in reserved_books:
                if count == 0:
                        earliest_date = row[2]
                        earliest_member = row[0]
                if row[2] < earliest_date:
                        earliest_date = row[2]
                        earliest_member = row[0]
                count += 1
        return earliest_member


#Borrowing a book
def borrowBook(accessionNo, memberID):
        if not doesBookExist(accessionNo):
                return "Book does not exist"
        if not doesMemberExist(memberID):
                return "Invalid Member ID"
        if isBorrowed(accessionNo):
                book_list = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
                for row in book_list:
                        return row[7]
        if isReserved(accessionNo):
                if nextReserve(accessionNo) != memberID:
                        return "Book is reserved"
        if hasFine(memberID):
                return "Member has outstanding fines"
        member_book_list = []
        member_books = connection.execute(f"SELECT * FROM Books WHERE memberID = '{memberID}'")
        for book in member_books:
                member_book_list += [book]
        if len(member_book_list) >= 2:
                return "Member loan quota exceeded"
        today = datetime.datetime.now()
        end_date = today + datetime.timedelta(days=14)
        today_date = today.date().strftime("%Y-%m-%d")
        end_date = end_date.date().strftime("%Y-%m-%d")       
        connection.execute(f"UPDATE Books SET memberID = '{memberID}', borrowDate = '{today_date}', dueDate = '{end_date}' WHERE accessionNo = '{accessionNo}'")
        if isReserved(accessionNo):
                connection.execute(f"DELETE FROM Reserves WHERE memberID = '{memberID}' AND accessionNo = '{accessionNo}'")
        return "Success"

#test-code
# print(borrowBook("A21", "A601F"))
# print(borrowBook("A03", "A601F"))
# print(borrowBook("A02", "A601F"))

#Returning a book(False means got fines)
def returnBook(accessionNo, returnDate):
        if not doesBookExist(accessionNo):
                return "Book does not exist"
        if not isBorrowed(accessionNo):
                return "Book has not been borrowed"
        book = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        for row in book:
                memberID = row[5]
                formatDueDate = row[7]
        formatReturnDate = datetime.datetime.strptime(returnDate, "%Y-%m-%d")
        formatReturnDate = formatReturnDate.date()
        diffDays = formatReturnDate - formatDueDate
        connection.execute(f"UPDATE Books SET memberID = NULL, borrowDate = NULL, dueDate = NULL WHERE accessionNo = '{accessionNo}'")
        if diffDays.days > 0:
                fines = diffDays.days * 1
                if hasFine(memberID):
                        connection.execute(f"UPDATE Fines SET payAmount = payAmount + {fines} WHERE memberID = '{memberID}'")
                else:
                        connection.execute(f"INSERT INTO Fines(memberID, payAmount) VALUES ('{memberID}', {fines})")
                return "Book returned successfully but has fines"
        return "Book returned successfully"

#test-code
#print(returnBook("A21", "2022-04-21"))
#print(returnBook("A03", "2022-03-24"))
        
#Reserving book
def reserveBook(accessionNo, memberID, reserveDate):
        if not doesBookExist(accessionNo):
                return "Book does not exist"
        if not doesMemberExist(memberID):
                return "Invalid Member ID"
        if not isBorrowed(accessionNo):
                return "Book is not borrowed"
        if hasFine(memberID):
                return "Member has outstanding fines"
        memberReserve = []
        member_reservedBooks = connection.execute(f"SELECT * FROM Reserves WHERE memberID = '{memberID}'")
        for book in member_reservedBooks:
                memberReserve += [book]
        if len(memberReserve) >= 2:
                return "Member reserve quota exceeded"
        connection.execute(f"INSERT INTO Reserves VALUES ('{memberID}', '{accessionNo}', '{reserveDate}')")
        return "Success"

#test-code
# print(reserveBook("A01", "A101A", "2022-03-10"))
# print(reserveBook("A01", "A201B", "2022-03-11"))  
# print(returnBook("A01", "2022-04-21"))
# print(borrowBook("A01", "A201B"))
# print(borrowBook("A01","A101A"))

#Cancel reservation
def cancelReserve(accessionNo, memberID, cancelDate):
        if not doesBookExist(accessionNo):
                return "Book does not exist"
        if not doesMemberExist(memberID):
                return "Member does not exist"
        reserve_list = []
        member_reserve = connection.execute(f"SELECT * FROM Reserves where accessionNo = '{accessionNo}' AND memberID = '{memberID}'")
        for row in member_reserve:
                reserve_list += row
        if not reserve_list:
                return "Member has no such reservation"
        if not isBorrowed(accessionNo) and nextReserve(accessionNo) == memberID:
                return "Cannot cancel reservation, book is available"
        connection.execute(f"DELETE FROM Reserves WHERE accessionNo = '{accessionNo}' AND memberID = '{memberID}'")
        return "Success"

#test-cases
#print(cancelReserve("A02", "A201B", '2022-03-10'))
#print(cancelReserve("A01", "A201B", '2022-03-10'))
        
#Selecting a book
def selectBook(title, author, isbn, publisher, publicationYear):
        searchOn = ""
        criteria = ""
        result = []
        count = 0
        if title:
                searchOn = "title"
                criteria = text(f"LIKE '% {title} %'")
                criteria2 = text(f"LIKE '{title} %'")
                criteria3 = text(f"LIKE '% {title}'")
                criteria4 = text(f"LIKE '{title}'")
        elif author:
                searchOn = "authorName"
                criteria = f"LIKE '% {author} %'"
                criteria2 = f"LIKE '{author} %'"
                criteria3 = f"LIKE '% {author}'"
                criteria4 = f"LIKE '{author}'"
        elif isbn:
                searchOn = "isbn"
                criteria = f"= {isbn}"
                criteria2 = criteria
                criteria3 = criteria
                criteria4 = criteria
        elif publisher:
                searchOn = "publisher"
                criteria = f"LIKE '% {publisher} %'"
                criteria2 = f"LIKE '{publisher} %'"
                criteria3 = f"LIKE '% {publisher}'"
                criteria4 = f"LIKE '{publisher}'"
        elif publicationYear:
                searchOn = "publishYear"
                criteria = f"= {publicationYear}"
                criteria2 = criteria
                criteria3 = criteria
                criteria4 = criteria
        r2 = connection.execute(text(f"SELECT b.accessionNo, title, authorName, isbn, publisher, publishYear" +
        f" FROM Books b, Authors a WHERE a.accessionNo = b.accessionNo AND ({searchOn} {criteria} OR {searchOn} {criteria2} OR" + 
        f" {searchOn} {criteria3} OR {searchOn} {criteria4})")) 
        if author:
                temp = []
                for row in r2:
                        temp1 = connection.execute("SELECT b.accessionNo, title, authorName, isbn, publisher, publishYear" +
                        f" FROM Books b, Authors a WHERE a.accessionNo = b.accessionNo AND a.accessionNo = '{row[0]}'")
                        for tempss in temp1:
                                temp += [tempss]
                r2 = temp 
        for row in r2:
                row = list(row)
                flag = False
                if (count == 0):
                        result += [row]
                for i in range(len(result)):
                        if count == 0:
                                break
                        if row[0] == result[i][0]:
                                result[i][2] = f"{result[i][2]}, {row[2]}"
                                flag = True
                if not flag and count != 0:
                        result += [row]
                count += 1
        return result

print(selectBook("", "James", "", "", ""))

#Fine payment
def payFines(memberID, payDate, payAmount):
        if not doesMemberExist(memberID):
                return "Member does not exist"
        if not hasFine(memberID):
                return "Member has no fine"
        fines = connection.execute(f"SELECT * FROM Fines WHERE memberID = '{memberID}'")
        for fine in fines:
                if payAmount == fine[1]:
                      connection.execute(f"UPDATE Fines SET payAmount = 0, payDate = '{payDate}' WHERE memberID = '{memberID}'")
                      return "Success"
        return "Incorrect fine payment amount"

# print(payFines("A101A", "2022-10-13", 50))
# print(payFines("A601F", "2022-10-13", 50))
#print(payFines("A601F", "2022-10-13", 27))

#Display books on loan
def loanedBooks():
        result = []
        count = 0
        r2 = connection.execute("SELECT b.accessionNo, title, authorName, isbn, publisher, publishYear " + 
        "FROM Books b, Authors a WHERE a.accessionNo = b.accessionNo AND b.memberID IS NOT NULL")
        for row in r2:
                row = list(row)
                if (count == 0):
                        result += [row]
                flag = False
                for i in range(len(result)):
                        if count == 0:
                                break
                        if row[0] == result[i][0]:
                                result[i][2] = f"{result[i][2]}, {row[2]}"
                                flag = True
                if not flag:
                        if count != 0:
                                result += [row]
                count += 1
        return result

#print(borrowBook("A41", "A801H"))
#print(borrowBook("A35","A5101E"))
#print(borrowBook("A43", "A5101E"))
#print(loanedBooks())

#Display reserved books
def reservedBooks():
        result = []
        r2 = connection.execute(f"SELECT r.accessionNo, b.title, r.memberID, m.name FROM Reserves r, Books b, Members m WHERE" +
        " r.accessionNo = b.accessionNo AND r.memberID = m.memberID")
        for row in r2:
                result += [row]
        return result

#test-code
# print(reserveBook('A01', 'A201B', '2022-03-10'))
# print(reserveBook('A01', 'A901I', '2022-03-11'))
# print(reserveBook('A03', 'A201B', '2022-03-12'))
# print(reserveBook('A41', 'A5101E', '2022-03-13'))
#print(reservedBooks())

#Display outstanding fines
def outstandingFines():
        result = []
        r2 = connection.execute(f"SELECT f.memberID, name, faculty, phoneNo, email FROM Fines f, Members m WHERE " + 
        "f.memberID = m.memberID AND f.payAmount > 0")
        for row in r2:
                result += [row]
        return result

#test-code
# print(returnBook("A01",'2022-05-12'))
# print(returnBook('A03', '2022-04-01'))
#print(outstandingFines())

def loanedMember(memberID):
        if not doesMemberExist(memberID):
                return "Member does not exist"
        result = []
        count = 0
        r2 = connection.execute(f"SELECT b.accessionNo, title, authorName, isbn, publisher, publishYear " + 
        f"FROM Books b, Authors a WHERE a.accessionNo = b.accessionNo AND b.memberID = '{memberID}'")
        for row in r2:
                row = list(row)
                if (count == 0):
                        result += [row]
                flag = False
                for i in range(len(result)):
                        if count == 0:
                                break
                        if row[0] == result[i][0]:
                                result[i][2] = f"{result[i][2]}, {row[2]}"
                                flag = True
                if not flag:
                        if count != 0:
                                result += [row]
                count += 1
        return result

#test-case
#print(loanedMember("A5101E"))

def remove_book_details(accessionNo):
        same_id = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        author_object = connection.execute(f"SELECT authorName FROM Authors WHERE accessionNo = '{accessionNo}'")
        author_list = []
        for authors in author_object:
                for author in authors:
                        author_list.append(author)
        print_records = ""
        for record in same_id:
                print_records += "Accession Number: " + str(record[0]) + "\n" \
                        + "Title: " + str(record[1]) + "\n" \
                        + "Authors: " + (', '.join(str(author) for author in author_list)) + "\n" \
                        + "ISBN: " + str(record[2]) + "\n" \
                        + "Publisher: " + str(record[3]) + "\n " \
                        + "Published Year: " + str(record[4])
        return print_records

def borrow_book_details(accessionNo, id):
        same_id = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        member_object = connection.execute(f"SELECT * FROM Members WHERE memberID = '{id}'")
        member_list = []
        today = datetime.datetime.now()
        end_date = today + datetime.timedelta(days=14)
        today_date = today.date().strftime("%Y-%m-%d")
        end_date = end_date.date().strftime("%Y-%m-%d") 
        for member in member_object:
                for detail in member:
                        member_list.append(detail)
        print_records = ""
        for record in same_id:
                print_records += "Accession Number: " + str(record[0]) + "\n" \
                        + "Title: " + str(record[1]) + "\n" \
                        + "Borrow Date: " + today_date + "\n" \
                        + "Membership_ID: " + member_list[0] + "\n" \
                        + "Member Name: " + member_list[1] + "\n " \
                        + "Due Date: " + end_date
        return print_records

def return_book_details(accessionNo, returnDate):
        book = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        for row in book:
                title = row[1]
                memberID = row[5]
                formatDueDate = row[7]
        member_object = connection.execute(f"SELECT * FROM Members WHERE memberID = '{memberID}'")
        for row in member_object:
                memberName = row[1]
        formatReturnDate = datetime.datetime.strptime(returnDate, "%Y-%m-%d")
        formatReturnDate = formatReturnDate.date()
        diffDays = formatReturnDate - formatDueDate
        fines = 0
        if diffDays.days > 0:
                fines = diffDays.days * 1
        print_records = ""
        print_records += "Accession Number: " + str(accessionNo) + "\n" \
                + "Title: " + str(title) + "\n" \
                + "Membership ID: " + str(memberID) + "\n" \
                + "Member Name: " + str(memberName) + "\n" \
                + "Return Date: " + returnDate + "\n " \
                + "Fine: $" + str(fines)
        return print_records

def reserve_details(accessionNo, memberID, date, action):
        books = connection.execute(f"SELECT * FROM Books WHERE accessionNo = '{accessionNo}'")
        members = connection.execute(f"SELECT * FROM Members WHERE memberID = '{memberID}'")
        title = ""
        name = ""
        for row in books:
                title = row[1]
        for row in members:
                name = row[1]
        print_records = "Accession Number: " + str(accessionNo) + "\n" \
                        + "Title: " + str(title) + "\n" \
                        + "Membership ID: " + str(memberID) + "\n" \
                        + "Member Name: " + str(name) + "\n" \
                        + str(action) + ": " + str(date)
        return print_records

def getFine(memberID):
        fines = connection.execute(f"SELECT * FROM Fines WHERE memberID = '{memberID}'")
        for fine in fines:
                if fine[1] > 0:
                        return fine[1]
        return 0