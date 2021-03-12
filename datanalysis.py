import matplotlib.pyplot as plt
import os


plt.style.use('ggplot')

class BarChart():

    def __init__(self, x_axis, y_axis):

        self.x_axis = x_axis
        self.y_axis = y_axis

    def create_graph(self):

        x_pos = [i for i, _ in enumerate(self.x_axis)]

        plt.bar(x_pos, self.y_axis, color='blue')
        plt.xlabel("Audio Features")
        plt.ylabel("Track Data")
        plt.title("Audio Analysis of Track")
        plt.xticks(x_pos, self.x_axis)
        plt.savefig('static/photos/track-data.png')


'''
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'daddy p', 'tensor flow']
energy = [5, 6, 15, 22, 24, 8,8]

x_pos = [i for i, _ in enumerate(x)]
print(x_pos)
plt.bar(x_pos, energy, color='blue')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x_pos, x)

plt.savefig('static/photos/track-data.png')
'''