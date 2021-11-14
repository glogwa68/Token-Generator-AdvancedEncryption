gen2 = gen3 = gen4 = gen5 = "" 
  
with open('gen2.txt') as fp: 
    gen2 = fp.read() 

with open('gen3.txt') as fp: 
    gen3 = fp.read() 
  
with open('gen4.txt') as fp: 
    gen4 = fp.read() 

with open('gen5.txt') as fp: 
    gen5 = fp.read() 
  

gen2 += "\n"
gen2 += gen3 
gen2 += "\n"
gen2 += gen4 
gen2 += "\n"
gen2 += gen5 
  
with open ('all.txt', 'w') as fp: 
    fp.write(gen2) 