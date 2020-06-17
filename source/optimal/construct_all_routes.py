with open("all.rou.xml", "w") as f:

    with open("optimal.passenger.rou.xml", "r") as f_pass:
        for line in f_pass:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
    with open("optimal.truck.rou.xml", "r") as f_truck:
        for line in f_truck:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
    with open("optimal.bus.rou.xml", "r") as f_bus:
        for line in f_bus:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
                
    print("\nConstruction of all.route done\n")