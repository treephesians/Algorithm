def solution(today, terms, privacies):
    answer = []
    nToday = int("".join(today.split(".")))
    dTerms = dict(term.split() for term in terms)
    
    for i in range(len(privacies)):
        date, c = privacies[i].split(" ")
        nDate = int("".join(date.split(".")))
        d = nDate + int(dTerms[c]) * 100
        if d % 10000 > 1300:
            d -= 1200
            d += 10000
        print(d)
        if d < nToday:
            answer.append(i)

    return answer


# today	terms	privacies	result
# "2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	[1, 3]
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))