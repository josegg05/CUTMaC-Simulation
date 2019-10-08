import datetime
import time

""" Timezones """
print("date1: " + datetime.datetime.now().isoformat())

print("date2: " + datetime.datetime.utcnow().isoformat())

print("date3: " + datetime.datetime.now().replace(microsecond=0).isoformat())

print("date4: " + datetime.datetime.utcnow().replace(microsecond=0).isoformat())  # correct

utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
print("date5: " + datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat())

""" SUMO """
import optparse
import os
import random
import sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=True, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


if __name__ == "__main__":
    options = get_options()
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    # generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "MicroDescongest/osm.sumocfg",
                 "--tripinfo-output", "tripinfo.xml"])

e2detList = traci.lanearea.getIDList()
print("Comienzo de prueba tamaño de nombres de e2det")
for x in range(0, len(e2detList)):
    e2detID = e2detList[x]
    if len(e2detID) != 32:
        print("Error en: ", x)
print("Fin de prueba tamaño de nombres de e2det")

print(len(e2detList))
print("DetectorTopic:     " + e2detID[0:25])
print("DetectorID:        " + e2detID[0:27])
print("DetectorDirection: " + e2detID[24] + "-" + e2detID[28:33])
