# So this function serves as a way to group up the minterms by term count 


def minimizer(data):  

  # Find the terms groupings by the count 
  def grouping(terms): 
    groups = {} # array of groups 
    for term in terms # loops through the amount of terms in a term (or binary number)
        count = term.count("1") # Counts the amount of times 1 appears 
        groups.setdefault(count, []).append(term) # sets the number that is apparant in the terms as a list in the array of groups 
      return groups 

  # Combine the terms that match with the difference in one "-" dont care terms
  def combine_terms(t1, t2): 
    differnces  = 0
    combine = []
    # set a and b as the parsed terms zipped from the file
    for a, b in zip(t1, t2): 
      if a != b: 
        differnces += 1 # add to the difference count 
        combine.append("-") #add to the combine array
      else: 
        combine.append(a) # 

  # combine the minterms and dont cares from the data list 
terms = data["minterms"] + data["dont_cares"]
  # make sure there are no duplicates in the list 
terms = list(set(terms))

group_terms = grouping(terms) # now must group the terms again
prime_imp = set() # creating a collection of unique elements used for the output PLA 
  

while group_terms: 
  next_group = {}
  used = set()
  for group, terms in group_terms.items();
    for t1 in terms: 
      for t2 in group_terms.get(group + 1, []):
        combine = combine_terms(t1, t2)
        if combine:
          next_group.setdefault(group, []).append(combine)
          used.add(t1)
          used.add(t2)
  prime_imp.update(set(terms)- used) # update the prime implicants table after setting the new grouping 
  group_terms = grouping(next_group) # if there are any non grouped prime implicants left, this will reiterate through the loop 
  # until there are no more terms left to group 

return list(prime_imp)












  
