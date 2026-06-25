from Book import Book
from Member import Member
class Library:
    def __init__(self):
       self.books = [
    Book("Atomic Habits", "James Clear", "9780735211292",True),
    Book("Deep Work", "Cal Newport", "9781455586691",True),
    Book("Clean Code", "Robert C. Martin", "9780132350884",True),
    Book("The Pragmatic Programmer", "Andrew Hunt", "9780135957059",True),
    Book("Think Python", "Allen B. Downey", "9781491939369",True),
    Book("Python Crash Course", "Eric Matthes", "9781593279288",True),
    Book("Grokking Algorithms", "Aditya Bhargava", "9781617292231",True),
    Book("Introduction to Algorithms", "Thomas H. Cormen", "9780262046305",True),
    Book("Designing Data-Intensive Applications", "Martin Kleppmann", "9781449373320",True),
    Book("Clean Architecture", "Robert C. Martin", "9780134494166",True)
]
       self.members = [
    Member(101, "Rabiyya"),
    Member(102, "Ali"),
    Member(103, "Ahmed"),
    Member(104, "Fatima"),
    Member(105, "Ayesha"),
    Member(106, "Hassan"),
    Member(107, "Zain"),
    Member(108, "Maryam"),
    Member(109, "Bilal"),
    Member(110, "Sara")
]
    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title}Book added Successfully")
    def register_member(self,name):
        self.members.append(name)
        print(f"{self.member.name} registered successfully")
    def find_book(self,title):
        for item in self.books:
            if item.title==title:
               print("Book Found")
               return item
        return None
    def find_member(self,member_id):
        for item in self.members:
            if item.member_id==member_id:
                print(f"Member Found{item.name}")
                return item
    def display_available_books(self):
        for item in self.books:
            if item.is_available:
                print(item.title)
    def issue_book(self,member_id,title):
        member=self.find_member(member_id)
        if not member:
            return False
        book=self.find_book(title)
        if not book:
            return False
        if not book.is_available:
            return False
        member.borrow_book(book)
        return True
    def accept_return(self,member_id,title):
        member=self.find_member(member_id)
        if not member:
            return False
        book=self.find_book(title)
        if not book:
            return False
            
        return member.return_book(book)
    
           
        
        
    