#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Linear 'O(n)' since it's using a while loop to consistently check on an equation. With the equation being updated rapidly, the runtime will only slow down a bit.

b)
Linearithmic 'O(n log n)' which will take up time at a faster rate since there is nested loops in place. For every step the first loop iterates, the second one has to activate again from the very first number.

c)
Linear 'O(n)' since there's a recursive function that slowly brings down the main arguement until it reaches the single if statement.

## Exercise II

def minimized dropping(n, f)

    #take the height (n) of the building and subtract it with the breaking point of the egg (f). Return it with the value of the eggs dropped minimized (danger_zone).

    #go through each floor, dropping one egg from the first floor until the last. with each egg being dropped and when it reaches its breaking point, take the hieght of the building (n) and subtract with the floor at which the egg was dropped at. 

    for i in n:
        if drop_egg(i) = break:
            return 1
        else:
            return broken + drop_egg(i)

The runtime complexity would have to be constant 'O(1)' since its doing a simple calculation (assuming one egg was dropped at each floor) taking out the floors that is safe for the egg to drop.






