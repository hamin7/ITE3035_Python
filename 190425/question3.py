usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing",
             "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')
print(usernames)
