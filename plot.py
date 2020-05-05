from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('web/data.csv')
    x = data['R1']
    y1 = data['R2']
    y2 = data['R3']

    plt.cla()

    plt.plot(x,y1,'or')
    

    plt.legend(loc='upper left')
    plt.tight_layout()
    #plt.xlabel('meters')
    #plt.ylabel('meters')


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.title('Location')
plt.tight_layout()
plt.show()