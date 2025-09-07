def prime_numbers(list1):
    prime = []
    count = 0
    for i in list1:
        if i > 1: 
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(i)
                count += 1
    return prime, count

print("--- prime numbers and their count in a list ---")
while True:
    try:
        count = int(input("how many numbers do you want to add?\ncount: "))
        list1 = [int(input("number: ")) for k in range(count)]
    except ValueError:
        print("count and numbers must be an integer!")
        continue
    
    print("list:", list1)
    
    primes, primes_count = prime_numbers(list1)
    
    print("prime numbers:", primes)
    print("number of prime numbers:", primes_count)
    break
