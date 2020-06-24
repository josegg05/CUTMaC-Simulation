import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

emission_keys = ["CO2", "CO", "HC", "NOx", "PMx", "fuel", "electricity", "noise", ]
emission_units = ["mg/s", "mg/s", "mg/s", "mg/s", "mg/s", "ml/s", "Wh/s", "dB"]
key = int(input("Select a variable to plot:\n"
                "0: CO2\n"
                "1: CO\n"
                "2: HC\n"
                "3: NOx\n"
                "4: PMx\n"
                "5: fuel\n"
                "6: electricity\n"
                "7: noise\n"
                "Selection: "))
xml_opt_names_list = ["timed", "webster", "coord", "collab_pi", "collab_p"]
xml_sdg_names_list = ["s_timed", "s_webster", "s_coord", "s_collab_pi", "s_collab_p"]

contamination_opt = []
contamination_sdg = []

file_cont = 0
for file_name in xml_opt_names_list:
    contamination_opt.append([])
    tree = ET.parse(f'emissions/emission_{file_name}_vc.xml')
    emission_export = tree.getroot()
    # # one specific item attribute
    # print('Item #2 attribute:')
    # print(emission_export[0][1].attrib[emission_keys[key]])
    for time_step in emission_export:
        step_contamination = 0
        for vehicle in time_step:
            # print(vehicle.attrib[emission_keys[key]])
            step_contamination += float(vehicle.attrib[emission_keys[key]])
        contamination_opt[file_cont].append(step_contamination)
    file_cont += 1

file_cont = 0
for file_name in xml_sdg_names_list:
    contamination_sdg.append([])
    tree = ET.parse(f'emissions/emission_{file_name}.xml')
    emission_export = tree.getroot()
    # # one specific item attribute
    # print('Item #2 attribute:')
    # print(emission_export[0][1].attrib[emission_keys[key]])
    for time_step in emission_export:
        step_contamination = 0
        for vehicle in time_step:
            # print(vehicle.attrib[emission_keys[key]])
            step_contamination += float(vehicle.attrib[emission_keys[key]])
        contamination_sdg[file_cont].append(step_contamination)
    file_cont += 1

for idx in range(len(contamination_opt)):
    # print(f"{idx} before: ", len(contamination[idx]))
    extension = list(np.zeros(len(contamination_opt[0]) - len(contamination_opt[idx])))
    contamination_opt[idx].extend(extension)
    # print(f"{idx} after: ", len(contamination[idx]))

for idx in range(len(contamination_sdg)):
    # print(f"{idx} before: ", len(contamination[idx]))
    extension = list(np.zeros(len(contamination_sdg[0]) - len(contamination_sdg[idx])))
    contamination_sdg[idx].extend(extension)
    # print(f"{idx} after: ", len(contamination[idx]))

t_opt = np.arange(0, len(contamination_opt[0]), 1)
t_sdg = np.arange(0, len(contamination_sdg[0]), 1)

plt.figure(1)
for idx in range(len(contamination_opt)):
    plt.plot(t_opt, contamination_opt[idx], label=xml_opt_names_list[idx])
plt.ylabel(f'{emission_keys[key]} ({emission_units[key]})')
plt.xlabel(f'time (s)')
plt.title(f'Optimal Network: {emission_keys[key]} emission')
plt.legend()
plt.savefig(f'plots/emission_opt_{emission_keys[key]}_plot.svg')

plt.figure(2)
for idx in range(len(contamination_sdg)):
    plt.plot(t_sdg, contamination_sdg[idx], label=xml_opt_names_list[idx])
plt.ylabel(f'{emission_keys[key]} ({emission_units[key]})')
plt.xlabel(f'time (s)')
plt.title(f'San Diego Network: {emission_keys[key]} emission')
plt.legend()
plt.savefig(f'plots/emission_sdg_{emission_keys[key]}_plot.svg')

plt.show()
