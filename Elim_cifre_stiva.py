#Se dau doua numere naturale n si k cu n > k , k > 0. Se citeste un numar x cu n cifre. Se memoreaza in stiva 'stack' cifrele lui x de la dreapta la stanga. Sa se elimine din stiva 'stack' exact k elemente astfel incat, dupa
#eliminare, sa se recompuna un numar cu valoare maxima. Numarul se va compune dupa regula : cu cat o cifra e mai sus in stiva, cu atat e mai la stanga in numarul final.
#
#Exemplu : n = 6. k = 2, x = 652323
#se elimina 2 si 2, output: 6533

n=int(input())
k=int(input())
x=int(input())
stack=[]

while x>0:
    stack.append(x%10)
    x//=10


while len(stack)>n-k:
    for i  in range(len(stack)):
        Min=9999
        if stack[i]<Min:
            Min=stack[i]
    stack.pop(i)

nr_final=0
while len(stack)>0:
    nr_final*=10
    nr_final+=stack[-1]
    stack.pop()

print(nr_final)