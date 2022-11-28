"""
Python code for finding powerset of a set recursively.

There's an easier method using binary digits. Can you figure it out?
(Hint: a powerset contains 2^n sets if a set has n elements)
"""

def powerset(A:set, pset:list=[], depth=0) -> list:
    """
    Finds the powerset of a set A

    params: 
    A : set
        The set of which its powerset is to be found
    pset : list
        Initial powerset
    depth : integer
        A number that determines which recursive depth function is in

    @returns
    result: list
        A list of the powerset
    """

    if len(A) == 1: return [A]

    B = list(A)
    pset_set = []
    for i in range(len(A)):
        if depth == 0:
            pset=[]
        pset_set += powerset(set(B[i:i+len(B)-1]) if i+len(B)-1<=len(B) else set(B[i:len(B)] + B[:i-1]), pset)

    for element in pset_set:
        pset.append(element)
    union:set = set()
    for element in pset_set:
        union.update(element)
    pset.append(union)
    result = [set()]
    [result.append(element) for element in pset if element not in result]
    return result

