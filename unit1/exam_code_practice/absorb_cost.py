from util import *
'''
Let's say we have two different sentences, s1 and s2. We have a process
that absorbs both sentences by processing the elements at the front over and over
again. However, there is a very specific set of rules spelling out how 
sentence pieces are absorbed and a corresponding cost associated.

- FREE: the first element in the two sentences are the same; both first elements
        can be absorbed together, with a cost of 0
- BOTH: the first element in the two sentences are different; the two can still
        be absorbed together, but now with a cost of 1
- SINGLE: only a single element from either the beginning of s1 or s2 is 
		  consumed; this has a cost of 1.

This means there are multiple ways to absorb s1 and s2, each associated with a 
different cost.

Let's say s1 is "he" and s2 is "e". We could:
- consume both "h" and "e" simultaneously from the two sequences for a BOTH cost of 1
  and then consume s1's "e" for a SINGLE cost of 1 (total cost 2)
- consume SINGLE "h" from s1, then consume the matching "e"'s (FREE) (total cost 1)
- consume every letter individually as SINGLEs (total cost 3)
In this case, the minimum cost to absorb both sentences is 1

Write the function costToAbsorb below, which takes in two sequences as strings and 
returns the MINIMUM cost to absorb them according to the rules above.

Think about what your "states" and "successors" are!
'''


def costToAbsorb(s1, s2):
    start = (s1, s2)
    q = [(start, 0)]
    visited = set()
    while q:
        state, cost = q.pop(0)
        if state in visited:
            continue
        visited.add(state)
        s1, s2 = state
        if not s1 and not s2:
            return cost
        if s1 and s2 and s1[0] == s2[0]:
            q.append(((s1[1:], s2[1:]), cost))
        else:
            q.append(((s1[1:], s2), cost + 1))
            q.append(((s1, s2[1:]), cost + 1))
            if s1 and s2:
                q.append(((s1[1:], s2[1:]), cost + 1))





if __name__=="__main__":
    pass
