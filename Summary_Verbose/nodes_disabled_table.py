import numpy as np
import pandas as pd
import csv

csv_opt_names_list = ["webster", "collab_p_nd", "collab_p"]
csv_sdg_names_list = ["s_webster", "s_collab_p_nd", "s_collab_p"]
labels = ["Free", "Low", "Moderate", "High"]
control_labels = ["webster", "col_p_nd", "col_p"]
data_labels = ["Speed", "Trip Duration", "Waiting Time", "Time Loss", "Depart Delay"]
net_labels = ["Ideal Network", "San Diego Network"]
csv_opt_data_list = []
csv_sdg_data_list = []

print("\nIdeal variables calculation")
file_count = 0
for csv_name in csv_opt_names_list:
    with open(f"csv_files/{csv_name}_vc.csv") as csv_file:
        csv_opt_data_list.append([])
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                pass
            else:
                csv_opt_data_list[file_count].append(row)
            line_count += 1
    file_count += 1
    # print(csv_opt_data_list)

print("\nSan Diego variables calculation")
file_count = 0
for csv_name in csv_sdg_names_list:
    with open(f"csv_files/{csv_name}.csv") as csv_file:
        csv_sdg_data_list.append([])
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                pass
            else:
                csv_sdg_data_list[file_count].append(row)
            line_count += 1
    file_count += 1
    # print(csv_sdg_data_list)

table_all = pd.DataFrame(
    {(net_labels[0], labels[0], csv_opt_names_list[0]): {data_labels[0]: csv_opt_data_list[0][0][0],
                                                         data_labels[1]: csv_opt_data_list[0][0][1],
                                                         data_labels[2]: csv_opt_data_list[0][0][2],
                                                         data_labels[3]: csv_opt_data_list[0][0][3]},
     (net_labels[0], labels[0], csv_opt_names_list[1]): {data_labels[0]: csv_opt_data_list[1][0][0],
                                                         data_labels[1]: csv_opt_data_list[1][0][1],
                                                         data_labels[2]: csv_opt_data_list[1][0][2],
                                                         data_labels[3]: csv_opt_data_list[1][0][3]},
     (net_labels[0], labels[1], csv_opt_names_list[0]): {data_labels[0]: csv_opt_data_list[0][1][0],
                                                         data_labels[1]: csv_opt_data_list[0][1][1],
                                                         data_labels[2]: csv_opt_data_list[0][1][2],
                                                         data_labels[3]: csv_opt_data_list[0][1][3]},
     (net_labels[0], labels[1], csv_opt_names_list[1]): {data_labels[0]: csv_opt_data_list[1][1][0],
                                                         data_labels[1]: csv_opt_data_list[1][1][1],
                                                         data_labels[2]: csv_opt_data_list[1][1][2],
                                                         data_labels[3]: csv_opt_data_list[1][1][3]},
     (net_labels[0], labels[2], csv_opt_names_list[0]): {data_labels[0]: csv_opt_data_list[0][2][0],
                                                         data_labels[1]: csv_opt_data_list[0][2][1],
                                                         data_labels[2]: csv_opt_data_list[0][2][2],
                                                         data_labels[3]: csv_opt_data_list[0][2][3]},
     (net_labels[0], labels[2], csv_opt_names_list[1]): {data_labels[0]: csv_opt_data_list[1][2][0],
                                                         data_labels[1]: csv_opt_data_list[1][2][1],
                                                         data_labels[2]: csv_opt_data_list[1][2][2],
                                                         data_labels[3]: csv_opt_data_list[1][2][3]},
     (net_labels[0], labels[3], csv_opt_names_list[0]): {data_labels[0]: csv_opt_data_list[0][3][0],
                                                         data_labels[1]: csv_opt_data_list[0][3][1],
                                                         data_labels[2]: csv_opt_data_list[0][3][2],
                                                         data_labels[3]: csv_opt_data_list[0][3][3]},
     (net_labels[0], labels[3], csv_opt_names_list[1]): {data_labels[0]: csv_opt_data_list[1][3][0],
                                                         data_labels[1]: csv_opt_data_list[1][3][1],
                                                         data_labels[2]: csv_opt_data_list[1][3][2],
                                                         data_labels[3]: csv_opt_data_list[1][3][3]},
     (net_labels[1], labels[0], csv_opt_names_list[0]): {data_labels[0]: csv_sdg_data_list[0][0][0],
                                                         data_labels[1]: csv_sdg_data_list[0][0][1],
                                                         data_labels[2]: csv_sdg_data_list[0][0][2],
                                                         data_labels[3]: csv_sdg_data_list[0][0][3]},
     (net_labels[1], labels[0], csv_opt_names_list[1]): {data_labels[0]: csv_sdg_data_list[1][0][0],
                                                         data_labels[1]: csv_sdg_data_list[1][0][1],
                                                         data_labels[2]: csv_sdg_data_list[1][0][2],
                                                         data_labels[3]: csv_sdg_data_list[1][0][3]},
     (net_labels[1], labels[1], csv_opt_names_list[0]): {data_labels[0]: csv_sdg_data_list[0][1][0],
                                                         data_labels[1]: csv_sdg_data_list[0][1][1],
                                                         data_labels[2]: csv_sdg_data_list[0][1][2],
                                                         data_labels[3]: csv_sdg_data_list[0][1][3]},
     (net_labels[1], labels[1], csv_opt_names_list[1]): {data_labels[0]: csv_sdg_data_list[1][1][0],
                                                         data_labels[1]: csv_sdg_data_list[1][1][1],
                                                         data_labels[2]: csv_sdg_data_list[1][1][2],
                                                         data_labels[3]: csv_sdg_data_list[1][1][3]},
     (net_labels[1], labels[2], csv_opt_names_list[0]): {data_labels[0]: csv_sdg_data_list[0][2][0],
                                                         data_labels[1]: csv_sdg_data_list[0][2][1],
                                                         data_labels[2]: csv_sdg_data_list[0][2][2],
                                                         data_labels[3]: csv_sdg_data_list[0][2][3]},
     (net_labels[1], labels[2], csv_opt_names_list[1]): {data_labels[0]: csv_sdg_data_list[1][2][0],
                                                         data_labels[1]: csv_sdg_data_list[1][2][1],
                                                         data_labels[2]: csv_sdg_data_list[1][2][2],
                                                         data_labels[3]: csv_sdg_data_list[1][2][3]},
     (net_labels[1], labels[3], csv_opt_names_list[0]): {data_labels[0]: csv_sdg_data_list[0][3][0],
                                                         data_labels[1]: csv_sdg_data_list[0][3][1],
                                                         data_labels[2]: csv_sdg_data_list[0][3][2],
                                                         data_labels[3]: csv_sdg_data_list[0][3][3]},
     (net_labels[1], labels[3], csv_opt_names_list[1]): {data_labels[0]: csv_sdg_data_list[1][3][0],
                                                         data_labels[1]: csv_sdg_data_list[1][3][1],
                                                         data_labels[2]: csv_sdg_data_list[1][3][2],
                                                         data_labels[3]: csv_sdg_data_list[1][3][3]}})

table_short = pd.DataFrame({(net_labels[0], labels[1], control_labels[0]):
                                {data_labels[0]: csv_opt_data_list[0][1][0],
                                 data_labels[1]: csv_opt_data_list[0][1][1],
                                 data_labels[2]: csv_opt_data_list[0][1][2],
                                 data_labels[3]: csv_opt_data_list[0][1][3],
                                 data_labels[4]: csv_opt_data_list[0][1][4]},
                            (net_labels[0], labels[1], control_labels[1]):
                                {data_labels[0]: csv_opt_data_list[1][1][0],
                                 data_labels[1]: csv_opt_data_list[1][1][1],
                                 data_labels[2]: csv_opt_data_list[1][1][2],
                                 data_labels[3]: csv_opt_data_list[1][1][3],
                                 data_labels[4]: csv_opt_data_list[1][1][4]},
                            (net_labels[0], labels[1], control_labels[2]):
                                {data_labels[0]: csv_opt_data_list[2][1][0],
                                 data_labels[1]: csv_opt_data_list[2][1][1],
                                 data_labels[2]: csv_opt_data_list[2][1][2],
                                 data_labels[3]: csv_opt_data_list[2][1][3],
                                 data_labels[4]: csv_opt_data_list[2][1][4]},
                            (net_labels[0], labels[3], control_labels[0]):
                                {data_labels[0]: csv_opt_data_list[0][3][0],
                                 data_labels[1]: csv_opt_data_list[0][3][1],
                                 data_labels[2]: csv_opt_data_list[0][3][2],
                                 data_labels[3]: csv_opt_data_list[0][3][3],
                                 data_labels[4]: csv_opt_data_list[0][3][4]},
                            (net_labels[0], labels[3], control_labels[1]):
                                {data_labels[0]: csv_opt_data_list[1][3][0],
                                 data_labels[1]: csv_opt_data_list[1][3][1],
                                 data_labels[2]: csv_opt_data_list[1][3][2],
                                 data_labels[3]: csv_opt_data_list[1][3][3],
                                 data_labels[4]: csv_opt_data_list[1][3][4]},
                            (net_labels[0], labels[3], control_labels[2]):
                                {data_labels[0]: csv_opt_data_list[2][3][0],
                                 data_labels[1]: csv_opt_data_list[2][3][1],
                                 data_labels[2]: csv_opt_data_list[2][3][2],
                                 data_labels[3]: csv_opt_data_list[2][3][3],
                                 data_labels[4]: csv_opt_data_list[2][3][4]},
                            (net_labels[1], labels[1], control_labels[0]):
                                {data_labels[0]: csv_sdg_data_list[0][1][0],
                                 data_labels[1]: csv_sdg_data_list[0][1][1],
                                 data_labels[2]: csv_sdg_data_list[0][1][2],
                                 data_labels[3]: csv_sdg_data_list[0][1][3],
                                 data_labels[4]: csv_sdg_data_list[0][1][4]},
                            (net_labels[1], labels[1], control_labels[1]):
                                {data_labels[0]: csv_sdg_data_list[1][1][0],
                                 data_labels[1]: csv_sdg_data_list[1][1][1],
                                 data_labels[2]: csv_sdg_data_list[1][1][2],
                                 data_labels[3]: csv_sdg_data_list[1][1][3],
                                 data_labels[4]: csv_sdg_data_list[1][1][4]},
                            (net_labels[1], labels[1], control_labels[2]):
                                {data_labels[0]: csv_sdg_data_list[2][1][0],
                                 data_labels[1]: csv_sdg_data_list[2][1][1],
                                 data_labels[2]: csv_sdg_data_list[2][1][2],
                                 data_labels[3]: csv_sdg_data_list[2][1][3],
                                 data_labels[4]: csv_sdg_data_list[2][1][4]},
                            (net_labels[1], labels[3], control_labels[0]):
                                {data_labels[0]: csv_sdg_data_list[0][3][0],
                                 data_labels[1]: csv_sdg_data_list[0][3][1],
                                 data_labels[2]: csv_sdg_data_list[0][3][2],
                                 data_labels[3]: csv_sdg_data_list[0][3][3],
                                 data_labels[4]: csv_sdg_data_list[0][3][4]},
                            (net_labels[1], labels[3], control_labels[1]):
                                {data_labels[0]: csv_sdg_data_list[1][3][0],
                                 data_labels[1]: csv_sdg_data_list[1][3][1],
                                 data_labels[2]: csv_sdg_data_list[1][3][2],
                                 data_labels[3]: csv_sdg_data_list[1][3][3],
                                 data_labels[4]: csv_sdg_data_list[1][3][4]},
                            (net_labels[1], labels[3], control_labels[2]):
                                {data_labels[0]: csv_sdg_data_list[2][3][0],
                                 data_labels[1]: csv_sdg_data_list[2][3][1],
                                 data_labels[2]: csv_sdg_data_list[2][3][2],
                                 data_labels[3]: csv_sdg_data_list[2][3][3],
                                 data_labels[4]: csv_sdg_data_list[2][3][4]}
                            })

print(table_short.to_latex(index=True))
