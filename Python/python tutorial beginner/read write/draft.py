with open('657567.png','rb') as f:
    with open('657567copy.png','wb') as f_copy:
        for line in f:
            f_copy.write(line)