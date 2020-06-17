#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    cyberinterpreter.py
# @author  Jose Guzman
# @date    2019-10-25
# @version $Id$

from __future__ import absolute_import
from __future__ import print_function

import optparse
import os
import random
import sys
import paho.mqtt.client as mqtt
import json
import datetime
import time

# Import my classes


# we need to import python modules from the $SUMO_HOME/tools directory
# from paho.mqtt.client import Client

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

# def generate_routefile():
#     random.seed(42)  # make tests reproducible
#     N = 3600  # number of time steps
#     # demand per second from different directions
#     pWE = 1. / 10
#     pEW = 1. / 11
#     pNS = 1. / 30
#     with open("data/cross.rou.xml", "w") as routes:
#         print("""<routes>
#         <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" \
# guiShape="passenger"/>
#         <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>
#
#         <route id="right" edges="51o 1i 2o 52i" />
#         <route id="left" edges="52o 2i 1o 51i" />
#         <route id="down" edges="54o 4i 3o 53i" />""", file=routes)
#         vehNr = 0
#         for i in range(N):
#             if random.uniform(0, 1) < pWE:
#                 print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
#                     vehNr, i), file=routes)
#                 vehNr += 1
#             if random.uniform(0, 1) < pEW:
#                 print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
#                     vehNr, i), file=routes)
#                 vehNr += 1
#             if random.uniform(0, 1) < pNS:
#                 print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
#                     vehNr, i), file=routes)
#                 vehNr += 1
#         print("</routes>", file=routes)


# The program looks like this
#    <tlLogic id="0" type="static" programID="0" offset="0">
# the locations of the tls are      NESW
#        <phase duration="31" state="GrGr"/>
#        <phase duration="6"  state="yryr"/>
#        <phase duration="31" state="rGrG"/>
#        <phase duration="6"  state="ryry"/>
#    </tlLogic>

def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    with open("source/mqtt_tls_ids.txt", "r") as f:
        for line in f:
            line_fine = line.rstrip()
            #print(line_fine)
            client.subscribe(line_fine)

    # client.subscribe("intersection/0002/tls")
    # client.subscribe("intersection/0003/tls")
    # client.subscribe("intersection/0004/tls")
    # client.subscribe("intersection/0005/tls")
    # client.subscribe("intersection/0006/tls")
    # client.subscribe("intersection/0007/tls")
    # client.subscribe("intersection/0008/tls")
    # client.subscribe("intersection/0009/tls")
    # client.subscribe("intersection/0010/tls")
    # client.subscribe("intersection/0011/tls")
    # client.subscribe("intersection/0012/tls")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    msg_type = str(json.loads(msg.payload)["type"])

    if msg_type == "tlsControl":
        msg_command = str(json.loads(msg.payload)["command"])
        if msg_command == "setPhase" or msg_command == "setProgram" or msg_command == "setCompleteRedYellowGreenDefinition":
            print("Command arrived :" + str(msg_command))
            global msg_dic
            msg_dic.append(json.loads(msg.payload))


def mqtt_conf() -> mqtt.Client:
    broker_address = "localhost"  # "192.168.1.95"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address)  # connect to broker
    return client


def net_conf():
    e2det_list = traci.lanearea.getIDList()
    print(e2det_list)
    print("Lista de e2det_list cargada")

    tls_list = traci.trafficlight.getIDList()
    print(tls_list)
    print("Lista de tls cargada")

    for x in tls_list:
        state = []
        for i in range(len(traci.trafficlight.getRedYellowGreenState(x))):
            state.append('r')
        print("state " + str(x) + str(state))
        # traci.trafficlight.setRedYellowGreenState(x, "".join(state))

    # junctionList = traci.junction.getIDList()
    # print(junctionList)
    # print("Lista de junction cargada")

    return e2det_list, tls_list


def generate_random_accident(e2det_list):
    e2det_index = random.randrange(len(e2det_list))
    e2det_id = e2det_list[e2det_index]
    accident_direction = e2det_id[0:25]
    for x in e2det_list:
        if accident_direction in x:
            lane_id = traci.lanearea.getLaneID(x)
            traci.lane.setMaxSpeed(lane_id, 0.0)  # option 1
            # traci.lane.setDisallowed(lane_id, [])  # option 2
            print(f"Trafico parado en {lane_id}")

    msg = {
        "id": e2det_id[0:27],
        "type": "AccidentObserved",
        "laneId": traci.lanearea.getLaneID(e2det_id),
        "location": traci.lanearea.getPosition(e2det_id),  # Location may be in "GeoProperty. geo:json."
        "dateObserved": datetime.datetime.utcnow().isoformat(),
        "accidentOnLane": True,  # It has to be configured
        "laneDirection": e2det_id[24] + "-" + e2det_id[28:33]
    }
    client_sumo.publish(e2det_id[0:25], json.dumps(msg))
    print(f"Accident in lane  '{e2det_id[0:25]}'")
    return e2det_id


def remove_accident(e2det_id, e2det_list):
    accident_direction = e2det_id[0:25]
    for x in e2det_list:
        if accident_direction in x:
            lane_id = traci.lanearea.getLaneID(x)
            traci.lane.setMaxSpeed(lane_id, 13.89)  # option 1
            # traci.lane.setAllowed(lane_id, [])  # option 2

    msg = {
        "id": e2det_id[0:27],
        "type": "AccidentObserved",
        "laneId": traci.lanearea.getLaneID(e2det_id),
        "location": traci.lanearea.getPosition(e2det_id),  # Location may be in "GeoProperty. geo:json."
        "dateObserved": datetime.datetime.utcnow().isoformat(),
        "accidentOnLane": False,  # It has to be configured
        "laneDirection": e2det_id[24] + "-" + e2det_id[28:33]
    }
    client_sumo.publish(e2det_id[0:25], json.dumps(msg))
    return


def run():
    """execute the TraCI control loop"""
    step = 0
    jamLengthVehicle = [[0, 0]]
    vehicleNumber = [[0, 0]]
    occupancy = [[0, 0]]
    meanSpeed = [[0, 0]]

    e2det_list, tls_list = net_conf()
    # for x in range(len(e2det_list)):
    #     print(e2det_list[x])
    # print(tls_list)

    # set jamLengthVehicle and vehicleNumber variables
    for x in range(len(e2det_list) - 1):
        jamLengthVehicle.append([0, 0])
        vehicleNumber.append([0, 0])
        occupancy.append([0, 0])
        meanSpeed.append([0, 0])

    with open("log_files/sumo_detect_%d.log" % run_num, "w") as f:
        f.write("time; time_det; detect_id; cars_number; occupancy; jam; mean_speed\n")

    with open("log_files/tls_state_%d.log" % run_num, "w") as f:
        f.write("time; movement_id; state\n")

    # Send the start signal
    client_sumo.publish(start_topic, "start")

    # Start the Simulation
    print("Start Simulation")
    time_0 = time.perf_counter()
    time_current = 0.0
    time_step = 0.0
    sample_period = 2  # Most be >= 1
    sample_cycle = 1  # Most be 1 to reset
    #while time_current < 45:
    while traci.simulation.getMinExpectedNumber() > 0:
        print("Time:[%s] " % time_current)
        if sample_cycle == sample_period:
            sample_cycle = 1
            for x in range(len(e2det_list)):
                e2det_id = e2det_list[x]
                # print(e2det_id)
                jamLengthVehicle[x][0] = traci.lanearea.getJamLengthVehicle(e2det_id)
                vehicleNumber[x][0] = traci.lanearea.getLastStepVehicleNumber(e2det_id)
                occupancy[x][0] = traci.lanearea.getLastStepOccupancy(e2det_id)
                meanSpeed[x][0] = traci.lanearea.getLastStepMeanSpeed(e2det_id)
                if (jamLengthVehicle[x][0] != jamLengthVehicle[x][1]) or (vehicleNumber[x][0] != vehicleNumber[x][1]) or (
                        occupancy[x][0] != occupancy[x][1]) or (meanSpeed[x][0] != meanSpeed[x][1]):
                    jamLengthVehicle[x][1] = jamLengthVehicle[x][0]
                    vehicleNumber[x][1] = vehicleNumber[x][0]
                    occupancy[x][1] = occupancy[x][0]
                    meanSpeed[x][1] = meanSpeed[x][0]

                    # Fiware data model
                    # https://fiware-datamodels.readthedocs.io/en/latest/Transportation/TrafficFlowObserved/doc/spec/index.html
                    msg = {
                        "id": e2det_id[0:27],
                        "type": "TrafficFlowObserved",
                        "laneId": traci.lanearea.getLaneID(e2det_id),
                        "location": traci.lanearea.getPosition(e2det_id),  # Location may be in "GeoProperty. geo:json."
                        "dateObserved": time_current,
                        "jamLengthVehicle": jamLengthVehicle[x][0],
                        "occupancy": occupancy[x][0],
                        "meanSpeed": meanSpeed[x][0],
                        "vehicleNumber": vehicleNumber[x][0],
                        # "accidentOnLane": False,  # It has to be configured
                        "laneDirection": e2det_id[24] + "-" + e2det_id[28:33]
                    }

                    # print("jamLengthVehicle: ", jamLengthVehicle[x][0], "; vehicleNumber: ", vehi[x][1])
                    # print(e2det_id[0:25])
                    # print(msg)
                    client_sumo.publish(e2det_id[0:25], json.dumps(msg))
                    if "intersection/0002/" in e2det_id[0:27]:
                        with open("log_files/sumo_detect_%d.log" % run_num, "a") as f:
                            f.write(str(time_current) + "; " +
                                    str(time_current) + "; " +
                                    str(e2det_id[0:27]) + "; " +
                                    str(vehicleNumber[x][0]) + "; " +
                                    str(occupancy[x][0]) + "; " +
                                    str(jamLengthVehicle[x][0]) + "; " +
                                    str(meanSpeed[x][0]) + "\n")
        else:
            sample_cycle += 1
        # generate a random accident
        # if step == 20:
        #     accident_e2det = generate_random_accident(e2det_list)
        # if step == 300:
        #     remove_accident(accident_e2det, e2det_list)

        # print(traci.trafficlight.getCompleteRedYellowGreenDefinition(tls_list[0]))
        traci.simulationStep()
        time_step += 1.0
        while time.perf_counter() < time_0 + time_step:  # --> DON'T SEND MSGS TO THE NODES IN THIS PART
            # TLS management
            # print("Phase:", traci.trafficlight.getPhase(tls_list[0]))
            # print(msg_dic)
            if msg_dic:
                msg_in = msg_dic.pop(0)
                if msg_in["command"] == "setPhase":
                    traci.trafficlight.setRedYellowGreenState(msg_in["tls_id"], msg_in["data"])
                    print("Traci changed to", str(msg_in["data"]))
                if msg_in["command"] == "setProgram":
                    traci.trafficlight.setProgram(msg_in["tls_id"], msg_in["data"])
                if msg_in["command"] == "setCompleteRedYellowGreenDefinition":
                    traci.trafficlight.setCompleteRedYellowGreenDefinition(msg_in["tls_id"], msg_in["data"])
                if "intersection/0002/" in str(msg_in["tls_id"]):
                    with open("log_files/tls_state_%d.log" % run_num, "a") as f:
                        f.write(str(time_current) + "; " + str(msg_in["tls_id"]) + "; " + str(msg_in["data"]) + "\n")
                # traci.trafficlight.setRedYellowGreenState("intersection/0008/tls", "rrrrrrrrr")
                # there is a vehicle from the north, switch
                # traci.trafficlight.setPhase(tls_list[0], 0)
        time_current += 1.0
        step += 1
    print("Simulation Finished")
    # Send the stop signal
    client_sumo.publish(start_topic, "stop")


# this is the main entry point of this script
if __name__ == "__main__":
    # time.sleep(900)
    # Define the global variables
    run_num = 0
    start_topic = "intersection/all/start"
    random.seed(5)
    options = get_options()
    client_sumo = mqtt_conf()
    client_sumo.loop_start()  # Necessary to maintain connection

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    # generate_routefile()

    while run_num < 5:
        msg_dic = []
        # this is the normal way of using traci. sumo is started as a
        # subprocess and then the python script connects and runs
        traci.start([sumoBinary, "-c", "source/osm/osm.sumocfg",
                     #"--tripinfo-output", "log_files/tripinfo_%d.xml" % run_num,
                     "--summary", "log_files/summary_%d.xml" % run_num,
                     "--emission-output", "log_files/emission_%d.xml" % run_num,
                     "--verbose",
                     "--log", "log_files/verbose_%d.xml" % run_num,
                     "--start", "--quit-on-end"])

        run()

        traci.close()
        sys.stdout.flush()
        run_num += 1
        time.sleep(300)
