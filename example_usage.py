"""Example demonstrating Log-Barrier optimization."""
from client import LogBarrierSolver

def main():
    c = [1.0, 1.0]
    A = [[-1.0, 0.0], [0.0, -1.0]]
    b = [-1.0, -1.0]
    sol = LogBarrierSolver.solve_linear_constrained(c, A, b, x0=[2.0, 2.0])
    print("Interior-Point Solution:", sol)

if __name__ == "__main__":
    main()
