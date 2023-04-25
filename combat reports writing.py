import time
import json
import os

localtime = time.asctime(time.localtime(time.time()))
fighting_places = []
number_places = int(input("How many specific places have your troop reached? Please enter a number: "))
killed_tank = []
sky = []
density = []
killed_soldiers = []
death = []
rate = []
specific_time = []
etwas_terrain = []

for i in range(number_places):
    fighting_places.append(input(f"Your {i+1} location of fighting: "))
    killed_tank.append(input(f"How many tanks did you destroy here? "))
    sky.append(input(f"How many enemy planes did you destroy? "))
    density.append(input(f"What was the weather like here? "))
    killed_soldiers.append(input(f"How many soldiers did your troop kill? "))
    death.append(input(f"How many deaths did you have? "))
    rate.append(input(f"How would you rate the battle here? "))
    specific_time.append(input(f"What was the specific time of the battle here? "))
    etwas_terrain.append(input(f"Please describe the terrain here (e.g. 'terrain is describe'): "))

for i in range(number_places):
    data = (f"According to the military officer, in {str(specific_time[i])}, " 
            f"we had contact with the enemy. {str(etwas_terrain[i])} "
            f"The battle was {str(rate[i])} and lasted for a while. "
            f"We killed about {str(killed_soldiers[i])} soldiers and destroyed about {str(killed_tank[i])} tanks. "
            f"At the same time, we destroyed {str(sky[i])} enemy warplanes in {str(density[i])} weather. "
            f"However, at the same time, we lost {str(death[i])} men.")
    with open(f'report{i+1}.json', 'w') as report_file:
        json.dump(data, report_file)

with open('file.txt', mode="w", encoding='utf-8') as f:
    f.write(f'Today is {localtime}\n')
    f.write(f'We have battles in {fighting_places}\n')

    for i in range(1, number_places+1):
        filename = f'report{i}.json'
        with open(filename) as f_report:
            content = json.load(f_report)
            f.write(content + '\n')

os.startfile('file.txt')

