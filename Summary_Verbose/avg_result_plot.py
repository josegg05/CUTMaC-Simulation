import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


csv_opt_names_list = ["timed", "coord", "webster", "collab_pi", "collab_p"]
csv_sdg_names_list = ["s_timed", "s_coord", "s_webster", "s_collab_pi", "s_collab_p"]
average_labels = ["Free", "Low", "Moderate", "High"]
csv_opt_data_list = []
csv_sdg_data_list = []

data_labels = ["Speed", "Trip Duration", "Waiting Time", "Time Loss", "Depart Delay"]
data_units = ["m/s", "s", "s", "s", "s"]
#omitted_val = data_labels[3]
selection = int(input("Select a variable to plot:\n"
                                    "0: Speed\n"
                                    "1: Trip Duration\n"
                                    "2: Waiting Time\n"
                                    "3: Time Loss\n"
                                    "4: DepartDelay\n"
                                    "5: All\n"
                                    "Selection: "))
if selection == 5:
    val_plotted = "All"
    omitted_val = data_labels[int(input("Select a omitted variable to plot:\n"
                                        "0: Speed\n"
                                        "1: Trip Duration\n"
                                        "2: Waiting Time\n"
                                        "3: Time Loss\n"
                                        "4: DepartDelay\n"
                                        "Selection: "))]
else:
    val_plotted = data_labels[selection]

x = np.arange(len(average_labels))  # the label locations
width = 0.1  # the width of the bars
if val_plotted == "All":
    size = 5
    fig_opt, ax_opt = plt.subplots(nrows=1, ncols=4, constrained_layout=False, figsize=(size * 4, size * 1))
    fig_sdg, ax_sdg = plt.subplots(nrows=1, ncols=4, constrained_layout=False, figsize=(size * 4, size * 1))
else:
    fig, ax = plt.subplots(2)


print("\nIdeal variables calculation")
file_count = 0
for csv_name in csv_opt_names_list:
    with open(f"csv_files/{csv_name}_vc.csv") as csv_file:
        csv_opt_data_list.append([])
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            else:
                csv_opt_data_list[file_count].append(row)
            line_count += 1
    file_count += 1
    #print(csv_opt_data_list)

print("\nSan Diego variables calculation")
file_count = 0
for csv_name in csv_sdg_names_list:
    with open("csv_files/" + csv_name + '.csv') as csv_file:
        csv_sdg_data_list.append([])
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                pass
            else:
                csv_sdg_data_list[file_count].append(row)
            line_count += 1
    file_count += 1
    #print(csv_sdg_data_list)

if val_plotted == "All":
    y_pos = 0
    for val_plotted in data_labels:
        if val_plotted != omitted_val:
            timed_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[0]]
            print("timed: ", timed_means)
            coord_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[1]]
            print("coordinated: ", coord_means)
            webster_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[2]]
            print("webster: ", webster_means)
            collab_pi_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[3]]
            print("collab_pi: ", collab_pi_means)
            collab_p_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[4]]
            print("collab_p: ", collab_p_means)

            rects1_opt = ax_opt[y_pos].bar(x - 2*width, timed_means, width, label='Timed')
            rects2_opt = ax_opt[y_pos].bar(x - width, coord_means, width, label='Coordinated')
            rects3_opt = ax_opt[y_pos].bar(x, webster_means, width, label='Webster')
            rects4_opt = ax_opt[y_pos].bar(x + width, collab_pi_means, width, label='Collaborative PI')
            rects5_opt = ax_opt[y_pos].bar(x + 2*width, collab_p_means, width, label='Collaborative P')

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax_opt[y_pos].set_ylabel(f"Avg. {val_plotted} ({data_units[data_labels.index(val_plotted)]})")
            #ax_opt[y_pos].set_title("Ideal Network")
            ax_opt[y_pos].set_xticks(x)
            ax_opt[y_pos].set_xticklabels(average_labels)
            ax_opt[y_pos].legend()

            timed_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[0]]
            print("timed: ", timed_means)
            coord_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[1]]
            print("coordinated: ", coord_means)
            webster_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[2]]
            print("webster: ", webster_means)
            collab_pi_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[3]]
            print("collab_pi: ", collab_pi_means)
            collab_p_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[4]]
            print("collab_p: ", collab_p_means)

            rects1_sdg = ax_sdg[y_pos].bar(x - 2 * width, timed_means, width, label='Timed')
            rects2_sdg = ax_sdg[y_pos].bar(x - width, coord_means, width, label='Coordinated')
            rects3_sdg = ax_sdg[y_pos].bar(x, webster_means, width, label='Webster')
            rects4_sdg = ax_sdg[y_pos].bar(x + width, collab_pi_means, width, label='Collaborative PI')
            rects5_sdg = ax_sdg[y_pos].bar(x + 2 * width, collab_p_means, width, label='Collaborative P')

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax_sdg[y_pos].set_ylabel(f"Avg. {val_plotted} ({data_units[data_labels.index(val_plotted)]})")
            # ax_sdg[y_pos].set_title("San Diego: " + val_plotted + ' by control strategy')
            ax_sdg[y_pos].set_xticks(x)
            ax_sdg[y_pos].set_xticklabels(average_labels)
            ax_sdg[y_pos].legend()

            y_pos += 1

    fig_opt.suptitle('Ideal Network Results')
    fig_sdg.suptitle('San Diego Network Results')
    fig_opt.savefig('plots/results_opt_plot.svg')
    fig_sdg.savefig('plots/results_sdg_plot.svg')

else:
    timed_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[0]]
    print("timed: ", timed_means)
    coord_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[1]]
    print("coordinated: ", coord_means)
    webster_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[2]]
    print("webster: ", webster_means)
    collab_pi_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[3]]
    print("collab_pi: ", collab_pi_means)
    collab_p_means = [float(row[data_labels.index(val_plotted)]) for row in csv_opt_data_list[4]]
    print("collab_p: ", collab_p_means)

    rects1_opt = ax[0].bar(x - 2 * width, timed_means, width, label='Timed')
    rects2_opt = ax[0].bar(x - width, coord_means, width, label='Coordinated')
    rects3_opt = ax[0].bar(x, webster_means, width, label='Webster')
    rects4_opt = ax[0].bar(x + width, collab_pi_means, width, label='Collaborative PI')
    rects5_opt = ax[0].bar(x + 2 * width, collab_p_means, width, label='Collaborative P')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax[0].set_ylabel(f"Avg. {val_plotted} ({data_units[data_labels.index(val_plotted)]})")
    ax[0].set_title("Ideal Network: " + val_plotted + ' by control strategy')
    ax[0].set_xticks(x)
    ax[0].set_xticklabels(average_labels)
    ax[0].legend()

    autolabel(rects1_opt, ax[0])
    autolabel(rects2_opt, ax[0])
    autolabel(rects3_opt, ax[0])
    autolabel(rects4_opt, ax[0])
    autolabel(rects5_opt, ax[0])

    timed_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[0]]
    print("timed: ", timed_means)
    coord_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[1]]
    print("coordinated: ", coord_means)
    webster_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[2]]
    print("webster: ", webster_means)
    collab_pi_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[3]]
    print("collab_pi: ", collab_pi_means)
    collab_p_means = [float(row[data_labels.index(val_plotted)]) for row in csv_sdg_data_list[4]]
    print("collab_p: ", collab_p_means)

    rects1_sdg = ax[1].bar(x - 2*width, timed_means, width, label='Timed')
    rects2_sdg = ax[1].bar(x - width, coord_means, width, label='Coordinated')
    rects3_sdg = ax[1].bar(x, webster_means, width, label='Webster')
    rects4_sdg = ax[1].bar(x + width, collab_pi_means, width, label='Collaborative PI')
    rects5_sdg = ax[1].bar(x + 2*width, collab_p_means, width, label='Collaborative P')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax[1].set_ylabel(f"Avg. {val_plotted} ({data_units[data_labels.index(val_plotted)]})")
    ax[1].set_title("San Diego Network: " + val_plotted + ' by control strategy')
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(average_labels)
    ax[1].legend()

    autolabel(rects1_sdg, ax[1])
    autolabel(rects2_sdg, ax[1])
    autolabel(rects3_sdg, ax[1])
    autolabel(rects4_sdg, ax[1])
    autolabel(rects5_sdg, ax[1])

    fig.tight_layout()
    fig.savefig('plots/results_plot.svg')

plt.show()
