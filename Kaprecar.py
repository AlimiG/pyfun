def max(num):
    maxi = ''
    temp = list(map(int,list(num)))
    temp = sorted(temp,reverse=True)
    for i in temp:
        maxi += str(i)
    return int(maxi)

def min(num):
    mini = ''
    temp = list(map(int,list(num)))
    temp = sorted(temp)
    for i in temp:
        mini += str(i)
    return int(mini)

if __name__ == '__main__':
    #num = []
    #count = 0
    #while len(num) != 4:
        #num = input("Introduzca un numero de 4 cifras: "
    for i in range(0,10000):
        count = 0
        num = str(i)
        if len(num) < 4:
            num = '0'*(4-len(num))+num
        while num != '6174':
            num = max(num) - min(num)
            if num == 0:
                break
            num = str(num)
            if len(num) < 4:
                num = '0'+ num
            #print(num)
            count += 1
        
        print(f"{i} : {count}")
