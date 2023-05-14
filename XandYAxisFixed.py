import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd


def animate(i):
    print(i)
    xs.append(origin_data_x[i])
    ys.append(origin_data_y[i])

    # ax1.clear()
    ax1.plot(xs, ys, color="black", linewidth='1')


if __name__ == "__main__":

    df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    origin_data_x = []
    origin_data_y = []
    for i in df.values:
        origin_data_x.append(i[0])
        origin_data_y.append(i[1])

    num_of_frames = len(origin_data_x)
    min_origin_data_y = min(origin_data_y)
    max_origin_data_y = max(origin_data_y)

    # set the height of the canvas
    ylim_lower_bound = (max_origin_data_y + min_origin_data_y) / 2 - 1.2 * (max_origin_data_y - min_origin_data_y) / 2
    ylim_upper_bound = (max_origin_data_y + min_origin_data_y) / 2 + 1.2 * (max_origin_data_y - min_origin_data_y) / 2

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_xlim([0, num_of_frames + 2])
    ax1.set_ylim([ylim_lower_bound, ylim_upper_bound])
    ax1.set_xlabel("Time ($\mathregular{s}$)", fontsize=18)
    ax1.set_ylabel("Lac Area Density ($\mathregular{nmol\ cm^{-2}}$)", fontsize=18)

    xs = []
    ys = []

    anim = animation.FuncAnimation(fig, animate, blit=False, interval=1000,
                                   repeat=True, save_count=num_of_frames)

    anim.save('LiveLineChart.mp4',
              writer='ffmpeg', fps=1)
    plt.close()
