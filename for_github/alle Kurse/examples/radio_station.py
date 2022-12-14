from random import choice

def song_generator(song_list):
    new_song = None
    while True:
        if new_song != None:
            if new_song not in song_list:
                song_list.append(new_song)
            new_song = yield new_song
        else:
            new_song = yield(choice(song_list))           

songs = ["Her Şeyi Yak - Sezen Aksu", 
         "Bluesette - Toots Thielemans",
         "Six Marimbas - Steve Reich",
         "Riverside - Agnes Obel",
         "Not for Radio - Nas",
         "What's going on - Taste",
         "On Stream - Nils Petter Molvær",
         "La' Inta Habibi - Fayrouz",
         "Ik Leef Niet Meer Voor Jou - Marco Borsato",
         "Δέκα λεπτά - Αθηνά Ανδρεάδη"]

radio = song_generator(songs)
for i in range(5):
    print(next(radio))

print(radio.send("Sorma - Sezen Aksu"))
for i in range(5):
    print(next(radio))
