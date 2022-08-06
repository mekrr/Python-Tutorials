N = 5
for i in range(1,N):
    print("i =",i)
    for j in range(1,N-i+1):
        print(f'[{j},{j+i}]')
