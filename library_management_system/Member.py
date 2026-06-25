class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
    
    def borrow_book(self,book):
            if book.is_available:
                print("Book is avaialable and you can definitely borrow")
                self.borrowed_books.append(book)
                book.is_available=False
                return True
            return False
    def return_book(self,book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
                print("Book Returned Honestly")
                book.is_available=True
                return True
            return False
            
                
        