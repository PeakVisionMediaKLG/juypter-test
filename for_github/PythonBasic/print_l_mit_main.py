def print_listenelemente(l):
    counter=0
    for elem in l:        
        print("Listenelement Nr: ",counter,elem)
        counter+=1
    return

if __name__=="__main__":
    l=[1,2,4,"elme",False]
    print_listenelemente(l)
