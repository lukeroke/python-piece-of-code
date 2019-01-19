def draw_graph(tput_file_name='tput_list'):
    import numpy as np
    import matplotlib.pyplot as plt
    # tput_file_name = 'tput_list'
    npzfile = np.load(tput_file_name + '.npz')
    tput = npzfile['arr_0']

    plt.subplot(3, 1, 1)
    plt.plot(tput, '.')
    plt.xlabel("num of episode")
    plt.ylabel("throughput")
    plt.title("Throughput for all episodes")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    window_size = 100
    average_tput = np.convolve(tput, np.ones(window_size, dtype=int), 'valid') / window_size
    plt.plot(average_tput, '-')
    plt.xlabel("num of episode")
    plt.ylabel("average throughput")
    plt.title("Average throughput within window of %d" % window_size)
    plt.grid(True)

    plt.subplot(3, 1, 3)
    window_size = 100
    nonopt_bool = tput < tput.max()
    nonopt = np.convolve(nonopt_bool, np.ones(window_size, dtype=int), 'valid')
    plt.plot(nonopt, '-')
    plt.xlabel("num of episode")
    plt.ylabel("count of non-optimal")
    plt.title("Count of non-optimal decisions within window of %d" % window_size)
    plt.grid(True)

    plt.tight_layout()
    fig=plt.gcf()
    fig.set_size_inches(10,10)
    fig.savefig(tput_file_name+'.png')
    # plt.show()

def draw_graph_compare():
    import numpy as np
    import matplotlib.pyplot as plt
    # Input Parameters
    OUTPUT_NAME= "compare-v101-v101_2-v102-v103-v104"
    tput_file_list = ['tput_list.v101-2', 'tput_list.v101-3', 'tput_list.v102', 'tput_list.v103', 'tput_list.v104']
    label_name_list = ['[64,128]','[64,128,256]','no_rsrc-[64,128]','no_rsrc-[64,128,256]','no_rsrc-[128,256]']

    # Inner Parameters
    plot_mark_list = ['^','*','+','.','1']
    # https://matplotlib.org/api/markers_api.html
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF']
    # colors = ['b','g','r','c','y']
    # https://matplotlib.org/gallery/lines_bars_and_markers/markevery_prop_cycle.html#sphx-glr-gallery-lines-bars-and-markers-markevery-prop-cycle-py
    SKIP = 1
    DPI = 500

    average_tput_list = []
    total_num = len(tput_file_list)
    for i in range(total_num):
        npzfile = np.load(tput_file_list[i] + '.npz')
        tput = npzfile['arr_0']
        window_size = 100
        average_tput = np.convolve(tput, np.ones(window_size, dtype=int), 'valid') / window_size
        plt.plot(average_tput[0:len(average_tput):SKIP], plot_mark_list[i], color=colors[i], label=label_name_list[i])

    plt.xlabel("num of episode (x%d)" % SKIP)
    plt.ylabel("average throughput")
    plt.title("Average throughput within window of %d" % window_size)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    fig=plt.gcf()
    fig.set_size_inches(10,5)
    fig.savefig( OUTPUT_NAME + ('(x%d).png' % SKIP), dpi=DPI)
        # plt.show()

if __name__ == "__main__":
    import sys
    tput_file_name=sys.argv[1].split('.npz')[0] # remove ".npz"
    draw_graph(tput_file_name)
