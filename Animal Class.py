class Animal():
    def __init__(self,type,gender,weight,height,voice):
        self.type=type
        self.gender=gender
        self.weight=weight
        self.height=height
        self.voice=voice

    def __len__(self):
        return self.height

class Dog(Animal):
    def __init__(self,type,gender,weight,height,voice,pet):
        super().__init__(type,gender,weight,height,voice)
        self.pet=pet

    def showDog(self):
        print("""
                    Dog type:   {}
                    Dog gender: {}
                    Dog weight: {}
                    Dog height: {}
                    Dog voice:  {}
                    Is that pet:    {}            
        """.format(self.type,self.gender,self.weight,self.height,self.voice,self.pet))

class Birds(Animal):
    def __init__(self,type,gender,weight,height,voice,wild):
        super().__init__(type,gender,weight,height,voice)
        self.wild=wild

    def showBirds(self):
        print("""
                   Birds type:   {}
                   Birds gender: {}
                   Birds weight: {}
                   Birds height: {}
                   Birds voice:  {}
                   Is that wild:    {}            
        """.format(self.type,self.gender,self.weight,self.height,self.voice,self.wild))

class Horse(Animal):
    def __init__(self,type,gender,weight,height,voice):
        super().__init__(type,gender,weight,height,voice)

    def showHorse(self):
        print("""
                    Horse type:   {}
                    Horse gender: {}
                    Horse weight: {}
                    Horse height: {}
                    Horse voice:  {}           
        """.format(self.type, self.gender, self.weight, self.height, self.voice))


dog1=Dog('Pitbull','female',35,95,'Hav Hav','No')
bird1=Birds('Crow','male',5,23,'Gak gakkk','Yes')
horse1=Horse('English Horse','female',145,223,'İghhg İghugu')

horse1.showHorse()
bird1.showBirds()
dog1.showDog()
print(len(horse1))