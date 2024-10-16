# Probability Projects

Documenting work I've done in the probability space. Gonna drop any fun projects I've worked on here, computational or not.

## Random Walk (`random_walk.py`)

Given a starting point, goal, terminating point, and probabilities for a random walk, this calculates the probability of success (reaching the goal). Got a question like this in a quant OA, so I immortalized it in code lol.

### Problem Overview
The probability of success from any given position is defined by the probabilities of the surrounding positions. This satisfies the **Markov Property**, meaning it only depends on where you are, not how you got there.

### Approach
You could solve this recursively on paper, but this implementation builds a tridiagonal matrix to store the probabilities and uses `numpy` to solve the system. That way, you can get the probability of success from any position possible. 
