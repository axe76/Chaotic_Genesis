import math

def chaotic_map(n,x_0,y_0):
    d = 0.3
    a = 2.5 
    x=[]
    x.append(x_0)
    y = []
    y.append(y_0)

    for i in range(n-1):
        x.append((x[i]+d+(a*math.sin(2*math.pi*y[i])))%1)
        y.append(1 - a*pow(x[i],2) + y[i])

    return (x,y)

def float_to_shuffled_ints(x,y):
    x_sorted = sorted(x, reverse=True)
    y_sorted = sorted(y, reverse=True)

    shuffled_x = []
    for x_val in x:
        if x_val in x_sorted:
            i = x_sorted.index(x_val)
            shuffled_x.append(i)

    shuffled_y = []
    for y_val in y:
        if y_val in y_sorted:
            i = y_sorted.index(y_val)
            shuffled_y.append(i)


    print('shuffled_x = ',shuffled_x)
    print('shuffled_y = ',shuffled_y)

    key = []
    for i in shuffled_x:
        key.append(shuffled_y[i])

    return key

plaintext = input('Enter Message: ')
ascii_lst = [ord(i) for i in plaintext]
n = len(ascii_lst)

ascii_avg = sum(ascii_lst)/n

x_0 = ascii_avg/max(ascii_lst)

(x,y) = chaotic_map(n,x_0,y_0=0.2)

private_key = float_to_shuffled_ints(x,y)
print('Private Key = ',private_key)

ciphertext = []
for i in range(len(ascii_lst)):
    ciphertext.append(chr(ascii_lst[i]+private_key[i]))

print('CipherText = ',ciphertext)
