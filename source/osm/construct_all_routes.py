with open("all.rou.xml", "w") as f:
    # f.write('<?xml version="1.0" encoding="UTF-8"?>'
    #         '<!-- generated on 06/16/20 18:27:19 by Eclipse SUMO duarouter Version 1.6.0'
    #         '<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/duarouterConfiguration.xsd">'
    #         '   <input>'
    #         '       <net-file value="osm.net.xml"/>'
    #         '       <route-files value="osm.passenger.trips.xml"/>'
    #         '   </input>'
    #         '   <output>'
    #         '       <output-file value="osm.passenger.rou.xml"/>'
    #         '       <alternatives-output value="osm.passenger.rou.alt.xml"/>'
    #         '   </output>'
    #         '   <time>'
    #         '       <begin value="0"/>'
    #         '       <end value="1800.0"/>'
    #         '   </time>'
    #         '   <report>'
    #         '       <no-warnings value="true"/>'
    #         '       <ignore-errors value="true"/>'
    #         '       <no-step-log value="true"/>'
    #         '   </report>'
    #         '</configuration>'
    #         '-->'
    #         ''
    #         '<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">')

    with open("osm.passenger.rou.xml", "r") as f_pass:
        for line in f_pass:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
    with open("osm.truck.rou.xml", "r") as f_truck:
        for line in f_truck:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
    with open("osm.bus.rou.xml", "r") as f_bus:
        for line in f_bus:
            if "<vehicle " or "<route " or "</vehicle>" in line:
                f.write(line)
                
    #f.write("</routes>")
    print("\nConstruction of all.route done\n")