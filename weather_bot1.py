import pyowm

owm = pyowm.OWM('58e7f93e74e24c88a096481301bf4c51')
mgr = owm.weather_manager()
place = input("В каком городе/стране?:  ")
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']
print("In the city " + place + " now is " + w.detailed_status)
print("Temperature now is about " + str(temp))

if temp < 10:
    print("Now it`s too cold, wear the warm clothes!")
elif temp < 20:
    print("It`s cold, don`t forget the scarf :) ")
else:
    print("So good outside :) ")



