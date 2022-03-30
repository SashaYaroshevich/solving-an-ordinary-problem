def word(words):
    words_new = words.split()
    total = dict()
    for i in words_new:
        count = 0
        for j in i:
            if j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or j == "y":
                count += 1
            total[i] = count
    
    list_d = list(total.items())
    list_d.sort(key=lambda i: i[1])
    total_string = []
    for i in list_d:
        total_string.append(i[0])

    return " ".join(total_string)


x = "aaaa aaaaaa aaaaaafaa aa abb"

print(word(x))

