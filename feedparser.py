# trigger file - if you've done through part 11 but no stories are popping
# up, you should edit this file to contain triggers that will fire on current
# news stories!
# Problem 11: 

# subject trigger named t1
t1 SUBJECT world

# title trigger named t2
t2 TITLE Intel

# phrase trigger named t3
t3 PHRASE New York City

# composite trigger named t4
t4 AND t2 t3

# the trigger set contains t1 and t4
ADD t1 t4


