def solution1(phone_book):
    phone_book.sort()
    
    answer = True
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if(len(phone_book[j].split(phone_book[i])) > 1):
                answer = False
    return answer

def solution2(phone_book):

    answer = True

    return answer