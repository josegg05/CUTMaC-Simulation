python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 1 -p 4.676607 -o optimal.pedestrian.trips.xml -e 1800 -r optimal.pedestrian.rou.xml --vehicle-class pedestrian --pedestrians --prefix ped --max-distance 2000
python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 2 -p 9.575461 -o optimal.bicycle.trips.xml -e 1800 -r optimal.bicycle.rou.xml --vehicle-class bicycle --vclass bicycle --prefix bike --fringe-start-attributes 'departSpeed="max"' --max-distance 8000 --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 2 -p 16.941603 -o optimal.motorcycle.trips.xml -e 1800 -r optimal.motorcycle.rou.xml --vehicle-class motorcycle --vclass motorcycle --prefix moto --fringe-start-attributes 'departSpeed="max"' --max-distance 1200 --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 5 -p 5.082481 -o optimal.passenger.trips.xml -e 1800 -r optimal.passenger.rou.xml --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes 'departLane="best"' --fringe-start-attributes 'departSpeed="max"' --allow-fringe.min-length 1000 --lanes --validate
python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 5 -p 25.412405 -o optimal.bus.trips.xml -e 1800 -r optimal.bus.rou.xml --vehicle-class bus --vclass bus --prefix bus --min-distance 600 --fringe-start-attributes 'departSpeed="max"' --trip-attributes 'departLane="best"' --validate
python "$SUMO_HOME/tools/randomTrips.py" -n optimal.net.xml --seed 42 --fringe-factor 5 -p 31.765506 -o optimal.truck.trips.xml -e 1800 -r optimal.truck.rou.xml --vehicle-class truck --vclass truck --prefix truck --min-distance 600 --fringe-start-attributes 'departSpeed="max"' --trip-attributes 'departLane="best"' --validate
