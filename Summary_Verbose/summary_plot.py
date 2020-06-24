import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

summary_keys = ["meanWaitingTime", "meanTravelTime", "meanSpeed", "meanSpeedRelative", "duration"]
summary_labels = ["meanWaitingTimeToDepart", "meanTravelTime", "meanSpeed", "meanSpeedRelative", "duration"]
summary_units = ["s", "s", "m/s", "m/s", "s"]
key = int(input("Select a variable to plot:\n"
                "0: WaitingTimeToDepart\n"
                "1: TravelTime\n"
                "2: meanSpeed\n"
                "3: meanSpeedRelative\n"
                "4: duration\n"
                "Selection: "))
xml_opt_names_list = ["timed", "webster", "coord", "collab_pi", "collab_p"]
xml_sdg_names_list = ["s_timed", "s_webster", "s_coord", "s_collab_pi", "s_collab_p"]

sum_variable_opt = []
sum_variable_sdg = []

file_cont = 0
for file_name in xml_opt_names_list:
    sum_variable_opt.append([])
    tree = ET.parse(f'summary/summary_{file_name}.xml')
    summary_export = tree.getroot()
    for time_step in summary_export:
        sum_variable_opt[file_cont].append(float(time_step.attrib[summary_keys[key]]))
    file_cont += 1

file_cont = 0
for file_name in xml_sdg_names_list:
    sum_variable_sdg.append([])
    tree = ET.parse(f'summary/summary_{file_name}.xml')
    summary_export = tree.getroot()
    for time_step in summary_export:
        sum_variable_sdg[file_cont].append(float(time_step.attrib[summary_keys[key]]))
    file_cont += 1

for idx in range(len(sum_variable_opt)):
    # print(f"{idx} before: ", len(sum_variable[idx]))
    extension = list(np.zeros(len(sum_variable_opt[0]) - len(sum_variable_opt[idx])))
    sum_variable_opt[idx].extend(extension)
    # print(f"{idx} after: ", len(sum_variable[idx]))

for idx in range(len(sum_variable_sdg)):
    # print(f"{idx} before: ", len(sum_variable[idx]))
    extension = list(np.zeros(len(sum_variable_sdg[0]) - len(sum_variable_sdg[idx])))
    sum_variable_sdg[idx].extend(extension)
    # print(f"{idx} after: ", len(sum_variable[idx]))

t_opt = np.arange(0, len(sum_variable_opt[0]), 1)
t_sdg = np.arange(0, len(sum_variable_sdg[0]), 1)

plt.figure(1)
for idx in range(len(sum_variable_opt)):
    plt.plot(t_opt, sum_variable_opt[idx], label=xml_opt_names_list[idx])
plt.ylabel(f'{summary_labels[key]} ({summary_units[key]})')
plt.xlabel(f'time (s)')
plt.title(f'Ideal Network: {summary_labels[key]} summary')
plt.legend()
plt.savefig(f'plots/summary_opt_{summary_labels[key]}_plot.svg')

plt.figure(2)
for idx in range(len(sum_variable_sdg)):
    plt.plot(t_sdg, sum_variable_sdg[idx], label=xml_opt_names_list[idx])
plt.ylabel(f'{summary_labels[key]} ({summary_units[key]})')
plt.xlabel(f'time (s)')
plt.title(f'San Diego Network: {summary_labels[key]} summary')
plt.legend()
plt.savefig(f'plots/summary_sdg_{summary_labels[key]}_plot.svg')

plt.show()
