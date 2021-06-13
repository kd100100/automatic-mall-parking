#led testing phase2

# from operation import led_data
from led import led_on

#red, green, blue = led_data()
red, green, blue ={'wing': 'A', 'slot': 3} , {'wing': 'A', 'slot': 3},{'wing': 'A', 'slot': 3}
led_on(red, green, blue)
print(red, green, blue)
