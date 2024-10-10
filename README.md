### No Switch Scenario

This correctly simulates the scenario where the contestant does not switch their choice.

1. The contestant picks a door at random.
2. The winning door is also chosen at random.
3. The contestant’s choice is compared directly to the winning door.

### Switch Scenario

This correctly simulates the scenario where the contestant always switches their choice after the host reveals a non-winning door.

1. The contestant picks a door at random.
2. The winning door is chosen at random.
3. The host reveals a door that is neither the contestant’s choice nor the winning door.
4. The contestant then switches to the remaining unopened door.

### Results

The results of these simulations should align with the well-known probabilities of the Monty Hall problem:

- No Switch: The probability of winning is approximately 1/3 (33.33%).
- Switch: The probability of winning is approximately 2/3 (66.67%).
- Running a large number of simulations (1,000,000 in this case) ensures that the results will be statistically significant and should closely match these theoretical probabilities.
