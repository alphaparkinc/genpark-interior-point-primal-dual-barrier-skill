# Logarithmic Barrier Interior-Point Skill

Interior-point algorithm tracing the central path for inequality-constrained convex optimization problems.

```mermaid
flowchart TD
    FeasiblePoint["Initial Feasible Interior Point x0"] --> Barrier["Add Log-Barrier Term: -μ ∑ log(slack)"]
    Barrier --> Newton["Newton / Gradient Step on Penalized Objective"]
    Newton --> Decay["Anneal Barrier Parameter μ = γ * μ"]
    Decay --> Check{"Target Barrier Precision Reached?"}
    Check -- No --> Newton
    Check -- Yes --> BoundarySol["Optimal Constrained Solution"]
```

## Features
- **100% Python Standard Library**: Pure standard library functions.
- **Central Path Tracing**: Strictly stays within the interior of the feasible set.
- **Penalty Annealing**: Smooth convergence to active boundary faces.
