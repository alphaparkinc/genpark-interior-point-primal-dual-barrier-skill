"""Logarithmic Barrier Interior-Point Method.
100% Python Standard Library.
"""

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

class LogBarrierSolver:
    """Minimizes f(x) subject to g_i(x) <= 0 via log-barrier penalty."""
    @staticmethod
    def solve_linear_constrained(c, A, b, x0, mu0=10.0, mu_decay=0.2, inner_iters=20, outer_iters=5):
        x = list(x0)
        mu = mu0
        
        for _ in range(outer_iters):
            for _ in range(inner_iters):
                grad = list(c)
                feasible = True
                for i in range(len(A)):
                    slack = b[i] - dot(A[i], x)
                    if slack <= 1e-6:
                        feasible = False
                        break
                    for j in range(len(x)):
                        grad[j] += mu * A[i][j] / slack
                if not feasible:
                    break
                step = 0.01
                x = [x[j] - step * grad[j] for j in range(len(x))]
            mu *= mu_decay
            
        return [round(xi, 4) for xi in x]
