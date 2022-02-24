poem = "Centre of equal daughters, equal sons,All, all alike endeared, grown, ungrown, young or old,Strong, ample, fair, enduring, capable, rich,Perennial with the Earth, with Freedom, Law and Love,A grand, sane, towering, seated Mother,Chaired in the adamant of Time."
new_poem =''
for i in poem:
    if i not in ('a','e','i','o','u'):
        new_poem = new_poem + i
print(new_poem)