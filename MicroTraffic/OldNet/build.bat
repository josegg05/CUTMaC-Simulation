#!/bin/bash
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 1 -p 3.117738 -o osm.pedestrian.trips.xml -e 3600 -r osm.pedestrian.rou.xml --vehicle-class pedestrian --pedestrians --prefix ped --max-distance 2000
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 2 -p 6.383641 -o osm.bicycle.trips.xml -e 3600 --vehicle-class bicycle --vclass bicycle --prefix bike --fringe-start-attributes 'departSpeed="max"' --max-distance 8000 --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 2 -p 11.551093 -o osm.motorcycle.trips.xml -e 3600 --vehicle-class motorcycle --vclass motorcycle --prefix moto --fringe-start-attributes 'departSpeed="max"' --max-distance 1200 --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 5 -p 3.388321 -o osm.passenger.trips.xml -e 3600 --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes 'departLane="best"' --fringe-start-attributes 'departSpeed="max"' --allow-fringe.min-length 1000 --lanes --validate
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 5 -p 16.941603 -o osm.bus.trips.xml -e 3600 --vehicle-class bus --vclass bus --prefix bus --min-distance 600 --fringe-start-attributes 'departSpeed="max"' --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n osm.net.xml --seed 42 --fringe-factor 5 -p 21.177004 -o osm.truck.trips.xml -e 3600 --vehicle-class truck --vclass truck --prefix truck --min-distance 600 --fringe-start-attributes 'departSpeed="max"' --trip-attributes 'departLane="best"' --validate
