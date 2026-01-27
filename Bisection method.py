import math

# Read the function from the user
fx = input("Enter the function f(x): ")

# Read a, b and epsilon
a = float(input("Enter a: "))
b = float(input("Enter b: "))
epsilon = 0.0001

# Print table header
print("\nIteration\t a\t\t b\t\t c\t\t f(c)")
print("---------------------------------------------------------------")

# Create namespace with math module
namespace = {'math': math, 'x': None}

# Evaluate f(a) and f(b)
namespace['x'] = a
fa = eval(fx, {"__builtins__": {}}, namespace)
namespace['x'] = b
fb = eval(fx, {"__builtins__": {}}, namespace)

# Check the initial condition f(a)*f(b) < 0
if fa * fb >= 0:
    print("No root in the given interval")
else:
    iteration = 0

    while True:
        iteration += 1

        # Compute the midpoint
        c = (a + b) / 2

        # Evaluate f(c)
        namespace['x'] = c
        fc = eval(fx, {"__builtins__": {}}, namespace)

        # Print current iteration values
        print(iteration, "\t\t", round(a, 6), "\t", round(b, 6),
              "\t", round(c, 6), "\t", round(fc, 6))

        # Stopping condition |f(c)| < epsilon
        if abs(fc) < epsilon:
            print("\nRoot found =", c)
            print("Number of iterations =", iteration)
            break

        # Update the interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc