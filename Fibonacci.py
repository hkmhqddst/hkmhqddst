def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

n = int(input("Masukan angka: "))
for fib in fibs():
    if n == fib:
        print("Angka Fibonacci!")
        break
    if fib > n:
        print("Bukan Angka Fibonacci!")
        break