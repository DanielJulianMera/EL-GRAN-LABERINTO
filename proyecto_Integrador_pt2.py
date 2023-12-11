from readchar import readkey, key

while True:
    k = readkey()
    if k == key.UP:
         break
    else:
        print(k)