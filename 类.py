class Car():

    def _init_(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

#if __name__ == '__main__':
#my_new_car=Car('audi','a4',2016)
#print(my_new_car.get_descriptive_name())