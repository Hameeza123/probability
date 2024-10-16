Documenting work I've done in the probability space. Gonna drop any fun project I've worked on here, computational or not.

Random Walk (random_walk.py)\n
Given a starting point, goal, terminating point, and probabilities for a random walk, calculate the probability of success (reaching goal). Got a question like this in a quant OA so I immortalized it in code lol. Better not see that question again real talk.

Essentially, the probability of success from any given position is defined by that of the surrounding positions only. Thus, the Markov Property is satisfied. This can be solved recursively on paper. This implementation stores the probabilities in a tridiagonal matrix and solves the system using numpy. This way I have the probability of success from any position possible.
