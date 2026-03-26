import threading
import random
import time

balance = 1000
lock = threading.Lock()

def withdraw(name):
    global balance

    amount = random.randint(100, 400)

    lock.acquire()

    print(name, "trying to withdraw", amount)

    if balance >= amount:
        print(name, "withdraw successful")
        time.sleep(1)
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print(name, "insufficient balance")

    lock.release()
t1 = threading.Thread(target=withdraw, args=("Customer1",))
t2 = threading.Thread(target=withdraw, args=("Customer2",))
t3 = threading.Thread(target=withdraw, args=("Customer3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final Balance:", balance)