# booking 조건
# 도서 목록
# 회원 여부

# 대여 책, 책 대여 기간, 대여 여부

# 렌탈 조건 - 대여할 책, 대여 기간
# 반납 조건 - 대여한 책, 대여 기간
# 예약 조건 - 대여할 책, 대여 시기, 대여 여부

class Book:
    def __init__(self) -> None:
        pass


class Book_rantal(Book):
    def book_rantal(self, bookname, period):
        self.book_name = bookname
        self.book_period = period


class Book_return(Book):
    def book_return(self, bookname, period):
        self.book_name = bookname
        self.book_period = period


class Book_booking(Book):
    def book_booking(self, bookname, period, exist):



