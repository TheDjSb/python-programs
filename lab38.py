#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.Sample data : {'1':['rahul','singh'], '2':['aman','mandal']}



import itertools      
d ={'1':['rahul','singh'], '2':['aman','mandal']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))