movie = {'Bramhastra' : ['Amit','Alia','Ranveer']}
print(movie, end = '\n\n')

movie['Pushpa'] = ['alu arjun' , 'samantha']
movie['DDJ'] = ['sharukh', 'kajol']
movie['RRR'] = ['NTR','Alia','Ramcharan']

print(movie, end = '\n\n')

print(movie.keys(), end = '\n\n')
print(movie.values(), end = '\n\n')

print (movie['DDJ'], end = '\n\n')
print (movie['Bramhastra'][1], end = '\n\n')
print(movie['RRR'][0], end = '\n\n')
print(movie['RRR'][1][2], end = '\n\n')

for i in movie.values():
    print(i)

for j in movie.keys():
    print(j)

print()

for k in movie.values():
    for l in k:
        print(l)

print()

for m in movie.values():
    for n in m:
        print()
        for o in n:
            print(o)
            
print('*' * 200, end = '\n\n\n')      
            
movies = {'Bramhastra' : ['Alia','Amit','Ranveer'],'RRR' : ['Alia','Ramcharan' , 'NTR']}

movies['DDJ'] = ['Kajol','Sharukh']


for p,q in movies.items():
    print(p,'------->',q)
    
    
    

