def gentable(n):
    data=""
    for i in range(1,11):
        data+=f"{n} X {i} ={n*i}\n"
    with open(f"Table_{n}","w") as file:
        file.write(data)
    
    
for i in range(1,3):
    gentable(i)
    