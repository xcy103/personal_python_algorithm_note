import sys

# Using fast I/O
input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        x = int(input_data[idx])
        idx += 1
        
        # A Pythagorean triple requires x > 2
        if x <= 2:
            print("No")
            continue
        
        print("Yes")
        
        if x % 2 == 1:
            # Odd case formula: x, (x^2 - 1)/2, (x^2 + 1)/2
            a = x
            b = (x * x - 1) // 2
            c = (x * x + 1) // 2
        else:
            # Even case formula: x, (x/2)^2 - 1, (x/2)^2 + 1
            k = x // 2
            a = x
            b = k * k - 1
            c = k * k + 1
            
        print(a, b, c)