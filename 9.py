for i in range(0, 1000):
    for j in range(0, 1000):
        for k in range (0, 1000):
            if k+j+i == 1000:
                if k*k+j*j==i*i:
                    print(k*j*i)
                    
