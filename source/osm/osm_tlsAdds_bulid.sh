python "$SUMO_HOME/tools/tlsCycleAdaptation.py" -n osm.net.xml -r osm.passenger.rou.xml osm.truck.rou.xml osm.bus.rou.xml osm.motorcycle.rou.xml osm.bicycle.rou.xml --o tls_webster.add.xml
python "$SUMO_HOME/tools/tlsCoordinator.py" -n osm.net.xml -r osm.passenger.rou.xml osm.truck.rou.xml osm.bus.rou.xml osm.motorcycle.rou.xml osm.bicycle.rou.xml --o tlsOffsets.add.xml