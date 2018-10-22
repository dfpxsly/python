import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal

while True:
    rw = RandomWalk(500)
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(10, 6))

    #point_numbers = list(range(rw.num_point))
    plt.plot(rw.x_values, rw.y_values, linewidth=2)

    #plt.scatter(0, 0, s=20, c='green', edgecolor='none')
    #plt.scatter(rw.x_values[-1], rw.y_values[-1], s=20, c='red', edgecolor='none')
    plt.show()

    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    XY = pygal.XY()
    XY._title = 'random walk!'
    #XY.x_labels = rw.x_values
    in_put = list(zip(rw.x_values, rw.y_values))
    XY.add('random',in_put)
    XY.render_to_file('rw_visual.svg')

    flag = input('continue? (y/n): ')
    if flag == 'n':
        break
