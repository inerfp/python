# booking 조건
# 도서 목록
# 회원 여부

# 대여 책, 책 대여 기간, 대여 여부

# 렌탈 조건 - 대여할 책, 대여 기간
# 반납 조건 - 대여한 책, 대여 기간
import csv


class MemberJoin:
    def join(self):
        print("회원 가입 \n")
        mnumber = int(input("회원 번호를 받으세요 : "))
        join_name = input("이름을 입력하세요 : ")
        join_age = int(input("나이를 입력하세요 : "))
        with open('members.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(
                {'id': mnumber, 'name': join_name, 'age': join_age})
        # member = {"id": mnumber, "name": join_name, "age": join_age}


class BookList:
    def add_list(self):
        print("책 추가 \n")
        bnumber = int(input("책 번호를 받으세요 : "))
        book_name = input("책 이름을 입력하세요 : ")
        with open('books.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'bookname']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(
                {'id': bnumber, 'bookname': book_name})

# class Book_rantal(Book):
#     def book_rantal(self, bookname, period):
#         self.book_name = bookname
#         self.book_period = period


# class Book_return(Book):
#     def book_return(self, bookname, period):
#         self.book_name = bookname
#         self.book_period = period


# class Book_booking(Book):
#     def book_booking(self, bookname, period, exist):

# 파일 입출력
members = []
books = []
while True:
    print("1. 회원가입")
    print("2. 회원정보 변경")
    print("3. 도서 대여")
    print("4. 도서 반납")
    a = int(input("숫자를 입력하시오 \n"))
    if a == 1:
        join_data = MemberJoin()
        join_member = join_data.join()
        # members.append(join_member)

    # if a == 2:
    #     number = int(input("변경하고자 하는 회원 번호를 말씀해주세요"))
    #     change_members = []
    #     for i in members:
    #         if i["id"] == number:
    #             change_members = members[i]
    #             change_name = input("변경할 이름을 입력하세요 ")
    #             change_age = int(input("변경할 나이를 입력하세요 "))
    #             change_members["name"] = change_name
    #             change_members["age"] = change_age
    #         print(i)

    if a == 3:
        add_book = BookList()
        books = add_book.add_list()
    if a == 0:
        print(members)
