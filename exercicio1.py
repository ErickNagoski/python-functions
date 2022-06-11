def main():
    a = 10
    b = 15
    c = 4
    print('Condição 1',(((a<b) and a<c)) or c!=0)
    print('Condição 2',(a<b and (a<c or c!=0)))
    a = 1
    b = 9
    c = 0
    print('Condição 3',(not(a >= 0 and b == c)))
    c = 9
    print("Condição 4", (not(a >= 0 )and not(b == c))) 
    c = 0
    print("Condição 5", ((a>=0 or b==c)and b>a))
    a = -2
    b = 0
    c = 2
    print("Condição 6", (not (a<=b) or (c>b)))
    print("Condição 7", (not (a<=0 or (c>b))))
    a = 0
    b = 1
    c = 0
    print("Condição 7", ((a==0) and (b!=0) and (c==0)))
    a = 5 
    b = 0
    print("Condição 8", ((a==0) and (b!=0) and (c==0)))
    print("Condição 9", ((a==0) or (b!=0) or (c==0)))
main()