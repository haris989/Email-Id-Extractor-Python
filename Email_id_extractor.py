def no_of_x_in_y(x, y):
    number = 0
    for i in y:
        if i == x:
            number = number + 1

    return number


def if_email(case):
    index_at_the_rate = 0
    index_dot = 0
    for i in range(0, len(case)):
        if case[i] == "@":
            index_at_the_rate = i
            break
    if no_of_x_in_y(".", case[index_at_the_rate:len(case)]) == 0:
        return 0

    if(len(case[0:index_at_the_rate])==0):
        return 0

    if no_of_x_in_y("@", case) != 1:
        return 0
    else:
        return 1
    
    print("Please Input your text.")
    given_text = input()
a = given_text.split()
emails = []
for i in range(0, len(a)):
    present_case = a[i]
    if (if_email(present_case) == 1):
        emails.append(present_case)

print(emails)
