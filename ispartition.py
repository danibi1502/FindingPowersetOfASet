def ispartition(subsets:list, check_set:set) -> bool:
    """
    Checks if given subsets are partitions of a given set

    params:
    subsets : list
        A list of sets
    check_set : set
        The set function checks if subsets are  partitions of

    returns:
    result : bool
        True if susbets are partitions of set and False otherwise
    """

    def adds_up(subsets:list, check_set:set) -> bool:
        add_set = set()
        for subset in subsets:
            add_set.update(subset)
        return add_set==check_set
    
    def no_repititions(subsets:list) -> bool:
        seen:list = []
        for subset in subsets:
            for element in subset:
                if element not in seen: seen.append(element) 
                else: return False
        return True
    
    return (adds_up(subsets, check_set) and no_repititions(subsets))
