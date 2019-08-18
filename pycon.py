import random, time

def dynamic_indicator(str):
    char = ''
    while char is not str:
        time.sleep(0.005)
        char = chr(random.choice([32] + list(range(65, 123))))
        print(f"{char}", end='\n' if char is str else '\r')

for c in 'CONNECT THE PYTHONISTAS': dynamic_indicator(c)

