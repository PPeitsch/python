def propagar(lista):  
    long = len(lista)-1
    propagacion = lista.copy()
    
    for i, f in enumerate(propagacion):
        if f == 1:
            if i < long and propagacion[i+1] == 0:
                propagacion[i+1] = 1
                
    propagacion.reverse()
        
    for i, f in enumerate(propagacion):
        if f == 1:
            if i < long and propagacion[i+1] == 0:
                propagacion[i+1] = 1
    
    propagacion.reverse()
    return propagacion
        
#l = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
#l = [1,0,0,-1,0]
#l = [1,0,0,0]
#l = [0,0,0,1]
#l = [0,0,0,0,1,0,0,0,0]
#l = [0,0,0,0,-1,-1,0,0,0,0,0,0,0,0,0,1]
l = [ 0, 0, 0, 1, 0, 0]
print(l)
propagado = propagar(l)
print(propagado)