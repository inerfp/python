# booking 조건
# 도서 목록
# 회원 여부

# 대여 책, 책 대여 기간, 대여 여부
# 렌탈 조건 - 대여할 책, 대여 기간
# 반납 조건 - 대여한 책, 대여 기간
import csv
import os
from pydoc import replace

file_path = '/Users/nerda/Documents/side_project/python/books/template/'


class MemberJoin:
    def join(self):
        print("회원 가입 \n")
        mnumber = int(input("회원 번호를 받으세요 : "))
        join_name = input("이름을 입력하세요 : ")
        join_age = int(input("나이를 입력하세요 : "))
        with open('{}members.csv'.format(file_path), 'a', newline='') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'id': mnumber, 'name': join_name, 'age': join_age})
# 입력 정보 / 회원 정보 / 이름 / 나이 / 빌린 책 정보 (bookid)


class BookList:
    def add_list(self):
        print("책 추가 \n")
        bnumber = int(input("책 번호를 받으세요 : "))
        book_name = input("책 이름을 입력하세요 : ")
        with open('{}books.csv'.format(file_path), 'a', newline='') as csvfile:
            fieldnames = ['id', 'bookname', 'have']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow(
                {'id': bnumber, 'bookname': book_name, 'have': True})
# 입력 정보 / 책 정보 / 책 이름


class Book_Rantal:
    def book_rantal(self):
        print("빌릴 책 입력\n")
        with open('/Users/nerda/Documents/side_project/python/books/template/rantal.csv', 'a', newline='') as csvfile:
            fieldnames = ['id', 'memberid', 'bookid']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow('id': None, 'memberid': None, 'bookid': None)


# 파일 입출력
members = []
books = []
while True:
    print("1. 회원가입")
    print("2. 도서 정보 입력")
    print("3. 회원 이름 변경")
    print("4. 도서 반납")
    a = int(input("숫자를 입력하시오 \n"))

    if a == 1:
        join_data = MemberJoin()
        join_member = join_data.join()
        # members.append(join_member)
    if a == 2:
        add_book = BookList()
        books = add_book.add_list()
    # 책 빌리는 플로우 > 회원 정보 입력 > 빌릴 책 입력 > 대여
    # 회원 정보 입력 체크 맴버 db 접근 (csv open) > 회원 정보 리스트 넣기 > 입력값 회원 여부 체크
    # 빌릴 책 입력 > 보유 책 체크 > 대여 상태 체크
    if a == 3:
        with open('{}members.csv'.format(file_path), 'w', encoding='utf-8') as csvfile:
            a = input("회원 이름 입력 ")
            b = input("변경할 이름 입력")
            members = csv.writer(csvfile)
            for row in members:
                if a == row[1]:
                    members.writerows([b])

    if a == 0:
        print(members)
