class Room:
    def __init__(self, width, length, height, temperature):
        self.width = width
        self.lenght = length
        self.height = height
        self.temperature = temperature

#Ширина Кухни
    def get_width(self):
        return self._width

    def set_width(self, value):
        if value < 0 or value > 100:
            print("Error value width !!!")
            self._width = 1
        else:
            self._width = value

    width = property(get_width, set_width)

#Длина Кухни
    def get_lenght(self):
        return self._lenght

    def set_lenght(self, value):
        if value < 0 or value > 100:
            print("Error value lenght !!!")
            self._lenght = 1
        else:
            self._lenght = value

    lenght = property(get_lenght, set_lenght)

#Высота Кухни
    def get_height(self):
        return self._height

    def set_height(self, value):
        if value < 0 or value > 5:
            print("Error value height !!!")
            self._height = 1
        else:
            self._height = value

    height = property(get_height, set_height)

# Температура Кухни
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -10 or value > 40:
            print("Error value width !!!")
            self._temperature = 1
        else:
            self._temperature = value

    temperature = property(get_temperature, set_temperature)

#Двери
    def doors(self):
        while True:
            question = input('Open the door ? [(Y/n)]: ')
            if question == "Y" or question == "y":
                print("Door is open !!!")
                break
            elif question == "N" or question == "n":
                print("Door is closed !!!")
                break
            else:
                continue

room = Room(width=5, length=3.5, height=3, temperature=20)
print("Room options :")
print("Width :", room.width, "Lenght :", room.lenght, "Height :", room.height)
print("Temperature in room :", room.temperature)
room.doors()
print("")


#Работа телевизора
class TV_set:
    def __init__(self, mark, diagonal):
        self.mark = mark
        self.diagonal = diagonal

    def TV_works(self):
        while True:
            question = input('Turn on  the TV ? [(Y/n)]: ')
            if question == "Y" or question == "y":
                print("TV works !!!")
                break
            elif question == "N" or question == "n":
                print("TV switched off !!!")
                break
            else:
                continue

tv = TV_set(mark="LG", diagonal=55)

print("Mark TV :", tv.mark)
print("Diagonal TV :", tv.diagonal)
tv.TV_works()
print("")


#Параметры дивана
class Sofa:
    def __init__(self, manufactured, lenght, width):
        self.manufactuted = manufactured
        self.lenght = lenght
        self.width = width

    def get_lenght(self):
        return self._lenght

    def set_lenght(self, value):
        if value < 0 or value > 5 or value > room.lenght:
            print("Error value lenght !!!")
            self._lenght = 1
        else:
            self._lenght = value

    lenght = property(get_lenght, set_lenght)

    def get_width(self):
        return self._width

    def set_width(self, value):
        if value < 0 or value > 2 or value > room.width:
            print("Error value width !!!")
            self._width = 1
        else:
            self._width = value

    width = property(get_width, set_width)

options_sofa = Sofa(manufactured="IKEA", lenght= 3, width= 1)
print("Manufactuted sofa :", options_sofa.manufactuted)
print("Lenght sofa :", options_sofa.lenght)
print("Width sofa :",  options_sofa.width)
print("")


#Климатконтроль
class Climatу_control:

    def works_climate_control(self):
        if room.temperature < 18:
            print("Climatу control turn on the heating !")
        elif room.temperature > 23:
            print("Climatу control turn  on the cooling !")
        elif room.temperature in range (18, 24):
            print("Ideal temperature !")

climate = Climatу_control()
climate.works_climate_control()