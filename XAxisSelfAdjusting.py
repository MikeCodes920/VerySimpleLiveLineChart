import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd


def animate(i):
    print(i)
    xs.append(origin_data_x[i])
    ys.append(origin_data_y[i])

    ax1.clear()
    ax1.plot(xs, ys)


if __name__ == "__main__":
    df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    origin_data_x = []
    origin_data_y = []
    for i in df.values:
        origin_data_x.append(i[0])
        origin_data_y.append(i[1])

    num_of_frames = len(origin_data_x)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    xs = []
    ys = []

    anim = animation.FuncAnimation(fig, animate, blit=False, interval=10,
                                   repeat=True, save_count=num_of_frames)
    # plt.show()
    anim.save('continuousSineWave.mp4',
              writer='ffmpeg', fps=1)
    plt.close()
