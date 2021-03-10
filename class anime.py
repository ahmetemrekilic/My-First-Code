import time

class Anime():

    def __init__(self,name,episode,starting_date):
        self.name=name
        self.episode=episode
        self.starting_date=starting_date


class Anime1(Anime):
    def __init__(self,name,episode,starting_date,type):
        super().__init__(name,episode,starting_date)
        self.type=type

    def show_anime_information(self,):
        print(""""
        Anime name:             {}
        Anime episode:          {}
        Anime starting_date:    {}
        Anime type:             {}
        """.format(self.name,self.episode,self.starting_date,self.type))

    def __str__(self):
        return ("Anime name:{}\nAnime episode:{}\nAnime starting_date:{}\nAnime type:{}\n".format(self.name,self.episode,self.starting_date,self.type))
    
    def __len__(self):
        return self.episode
    
    def add_episode(self,ep):
        print("Episode uploading..")
        time.sleep(2)
        self.episode+=ep

    def add_type(self,ty):
        print("Type uploading..")
        time.sleep(2)
        self.type.append(ty)

anime1=Anime1("Black Clover",170,2017,"Supernatural")
anime2=Anime1("One Piece",900,1998,["Advanture"])
anime1.show_anime_information()

anime2.add_episode(65)
anime2.add_type("Supernatural")
anime2.show_anime_information()
print("Anime episode len:",len(anime2))
#YOU CAN ADD NEW OBJECT
#YOU CAN ADD İNFORMATİON WITH FUNCTIONS





