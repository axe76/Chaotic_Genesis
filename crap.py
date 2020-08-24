from fuzzywuzzy import fuzz

fitness = 100-fuzz.ratio('d','bcdef')

print(fitness)


'''
Genetic Algorithm

Given
1. Fitness which is levenshtein distance between cipher and plaintext

Requirement
1. Best possible a and d. - genome will be arrays of (a,d) for multiple generations.
 
a = 1.something to 4
d = 0 to 4

in crossover, we randomly generate offspirings using a1,d2 and a2,d1.
in mutation, for 10% of times, we need to do something based on steps.


x = [0.3,0.997,0.862,0.531,0.761]


x_sorted = [0.997,0.862,0.761,0.531,0.3]

[4,0,1,3,2]

[3,4,2,4,6]

[7,4,6,3,1]= key
[65,66,...]

[cipher]
'''




