def solve():
    def is_comp(n):
        array = set()
        array.add(1)
        for i in range(2, n//2 + 1): 
            if n % i == 0:
                array.add(i)
        
        if sum(array) == n:
            divisors = sorted(array) 
            str = "1"
            for i in divisors[1:]: 
                str += " + "
                str += f"{i}"
            print(f"{n} = {str}")
        else:
            print(f"{n} is NOT perfect.")
            
    array = []
    while True:
        n = int(input())
        if n == -1:
            break
        array.append(n)
    for i in array:
        is_comp(i)
solve()