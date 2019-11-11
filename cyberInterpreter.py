#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26
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

# Define the global variable of command_received
command_received = False
msg_dic = []


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
    client.subscribe("intersection/0002/tls")
    client.subscribe("intersection/0003/tls")
    client.subscribe("intersection/0004/tls")
    client.subscribe("intersection/0005/tls")
    client.subscribe("intersection/0006/tls")
    client.subscribe("intersection/0007/tls")
    client.subscribe("intersection/0008/tls")
    client.subscribe("intersection/0009/tls")
    client.subscribe("intersection/00010/tls")
    client.subscribe("intersection/00011/tls")
    client.subscribe("intersection/00012/tls")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    msg_type = str(json.loads(msg.payload)["type"])

    if msg_type == "tlsControl":
        msg_command = str(json.loads(msg.payload)["command"])
        if msg_command == "setPhase" or msg_command == "setProgram" or msg_command == "setCompleteRedYellowGreenDefinition":
            print("Command arrived :" + str(msg_command))
            global msg_dic
            global command_received
            msg_dic.append(json.loads(msg.payload))
            command_received = True


def mqtt_conf() -> mqtt.Client:
    broker_address = "192.168.5.95"   # "192.168.1.95"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address)  # connect to broker
    return client


def net_conf():
    e2detList = traci.lanearea.getIDList()
    print(e2detList)
    print("Lista de e2detList cargada")

    tlsList = traci.trafficlight.getIDList()
    print(tlsList)
    print("Lista de tls cargada")

    for x in tlsList:
        state = []
        for i in range(len(traci.trafficlight.getRedYellowGreenState(x))):
            state.append('r')
        print("stare " + str(x) + str(state))
        #traci.trafficlight.setRedYellowGreenState(x, "".join(state))

    # junctionList = traci.junction.getIDList()
    # print(junctionList)
    # print("Lista de junction cargada")

    return e2detList, tlsList


def generate_random_accident(e2detList):
    # TODO generate an accident on all channels of a random Street
    #  I can generate a random number x between 0 and the e2detList length and create an accident in the edge of
    #  e2detList[x]. To do that I can put dead cars in all the channels of the edge.
    #  Finally I have to send the accident msg to the correspondent node
    return


def run():
    """execute the TraCI control loop"""
    step = 0
    jam = [[0, 0]]
    vehicles = [[0, 0]]
    global command_received
    global msg_dic

    e2detList, tlsList = net_conf()
    # for x in range(len(e2detList)):
    #     print(e2detList[x])
    # print(tlsList)

    # set jam and vehicles variables
    for x in range(len(e2detList)-1):
        jam.append([0, 0])
        vehicles.append([0, 0])

    # we start with phase 2 where EW has green
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        # if traci.trafficlight.getPhase("gneJ1") == 2:
        # we are not already switching
        # if traci.inductionloop.getLastStepVehicleNumber("gneJ1") > 0:

        for x in range(len(e2detList)):
            e2detID = e2detList[x]
            # print(e2detID)
            jam[x][0] = traci.lanearea.getJamLengthVehicle(e2detID)
            vehicles[x][0] = traci.lanearea.getLastStepVehicleNumber(e2detID)
            if vehicles[x][0] != vehicles[x][1]:
                vehicles[x][1] = vehicles[x][0]

                # Fiware data model
                # https://fiware-datamodels.readthedocs.io/en/latest/Transportation/TrafficFlowObserved/doc/spec/index.html
                msg = {
                    "id": e2detID[0:27],
                    "type": "TrafficFlowObserved",
                    "laneId": traci.lanearea.getLaneID(e2detID),
                    "location": traci.lanearea.getPosition(e2detID),  # Location may be in "GeoProperty. geo:json."
                    "dateObserved": datetime.datetime.utcnow().isoformat(),
                    "intensity": jam[x][0],
                    "occupancy": traci.lanearea.getLastStepOccupancy(e2detID),
                    "averageVehicleSpeed": traci.lanearea.getLastStepMeanSpeed(e2detID),
                    "carsInLane": vehicles[x][0],
                    "accidentOnLane": False,    # It has to be configured
                    "laneDirection": e2detID[24] + "-" + e2detID[28:33]
                }

                # print("jam: ", jam[x][0], "; vehicles: ", vehi[x][1])
                # print(e2detID[0:25])
                print(msg)
                client_sumo.publish(e2detID[0:25], json.dumps(msg))

        # tls management
        print("Phase:", traci.trafficlight.getPhase(tlsList[0]))
        print(command_received)
        print(msg_dic)
        if command_received:
            for x in msg_dic:
                if x["command"] == "setPhase":
                    traci.trafficlight.setRedYellowGreenState(x["tlsID"], x["data"])
                if x["command"] == "setProgram":
                    traci.trafficlight.setProgram(x["tlsID"], x["data"])
                if x["command"] == "setCompleteRedYellowGreenDefinition":
                    traci.trafficlight.setCompleteRedYellowGreenDefinition(x["tlsID"], x["data"])
            command_received = False
            msg_dic = []
            # traci.trafficlight.setRedYellowGreenState("intersection/0008/tls", "rrrrrrrrr")
            # there is a vehicle from the north, switch
            # traci.trafficlight.setPhase(tlsList[0], 0)

        # print(traci.trafficlight.getCompleteRedYellowGreenDefinition(tlsList[0]))
        step += 1
    traci.close()
    sys.stdout.flush()


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    client_sumo = mqtt_conf()
    client_sumo.loop_start()    # Necessary to maintain connection

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
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
    run()
