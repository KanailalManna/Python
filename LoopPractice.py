#1.write a programme to print a multiplication table of a given number

# num = int(input("Enter a number to print table :"))
# for i in range(1,11):
#     print(str(num)+"x"+str(i)+"="+str(num*i))
    
    # print(f"{num}x{i}={num*i}")   #we can write like this way, using f-string 
                                    #here {} is for variable and before "" we have to use 'f'



#2. check a list start with 'r' 

# l1 = ["Kanai","Ritam","Adrija","Ritwika","Mama"]
# for name in l1:
#     if name.startswith("R") :
#         print("Hello " + name)



#3. Factorial of a number

# num = int(input("Enter a number :"))
# result = 1
# for i in range(1,num+1):
#     result *= i
# print(result)


#4. parrern problem
# n = int(input("Enter number"))
# for i in range(n):
#     print(" "*(n-i-1), end="")
#     print("*"*(2*i+1), end="")
#     print(" "*(n-i-1))


#5. Parrern problem
# n = int(input("Enter number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



#pattern problem
# n = int(input("Enter pattern :"))
# for i in range(n,0,-1):
#     for j in range(int(i*(i+1)/2)-i+1,int(i*(i+1)/2)+1):
#         print(str(j)+"  ", end="")
#     print()


#pattern problem
# n=5
# for i in range (1,n+1):
#     for j in range(1,n+1-i) :
#         print(" ",end="")
#     for j in range(1,i*2):
#         print(i,end="")


    