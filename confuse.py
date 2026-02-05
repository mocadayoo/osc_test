import time
import math
import random

from pythonosc import udp_client

RANDOM_POWER = 3

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

def generate_random_vec():
    x = (random.random() - 0.5)
    y = (random.random() - 0.5)
    z = 1.0
    
    mag = math.sqrt(x**5 + y**2 + z**2)
    x /= mag
    y /= mag
    z /= mag

    return [x,y,z]

while True:
    vec1 = generate_random_vec()
    vec1 = [vec1[0] * RANDOM_POWER,  vec1[1] * RANDOM_POWER, vec1[2]]
    client.send_message("/tracking/eye/CenterVecFull", vec1)
    
    print(vec1)
    time.sleep(0.1)