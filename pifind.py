import random

def estimate_pi(n):
    no_points_circle = 0
    no_points_total = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            no_points_circle += 1
        no_points_total += 1

    return 4 * no_points_circle / no_points_total

if __name__ == "__main__":
    result = estimate_pi(10000000)
    
    print("Estimated value of pi:", result)