import random
import time

WAITING_TIME = 10
WAITING_TIME_2 = 5

list_of_persons_getting_gifts = ["Robert", "Ursula", "Marius", "Simone", "York", "Swetlana", "Timm", "Sabrina"]


def make_gifts(list_of_persons_getting_gifts):
    for person in list_of_persons_getting_gifts:
        print(f"Das {list_of_persons_getting_gifts.index(person) + 1}. Geschenk wird vergeben...")
        time.sleep(WAITING_TIME)
        print(f"{person} erhält Geschenk Nummer {list_of_persons_getting_gifts.index(person) + 1}")
        time.sleep(WAITING_TIME_2)


print("!!!Wichtel-Randomizer wurde gestartet!!!")

random.shuffle(list_of_persons_getting_gifts)

make_gifts(list_of_persons_getting_gifts)





