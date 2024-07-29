import time 


counter = 0

max = 5

while True:
    counter += 1
    print("Hello")
    time.sleep(counter)
    if counter == max:
        print("End of Loop")
        break