pws = {"user1":"geheim1", "user2":"geheim2"}

user     = input("user: ")
password = input("password: ")

okay = False
if user in pws: 
    okay = (pws[user] == password)
    
if okay:
    print("Alles klar")
else:
    print("password und/oder user nicht bekannt")

