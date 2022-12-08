## Daimler Fuso Truck & Insight ETA prediction project

*How to use
To start process, you must run "python main.py vehicleCode Journey" on prompt
- vehicleCode : vehicleCode
- Journey : Order of driving journey

ex) vehicleCode is W102 and this vehicle go to target 3 through 1,2 then you should give it with list.
In list the first value must be 0.

ex) python main.py W102 [0,1,2,3]


Once you run above command. then ETA process will be started.
From now on, you should deliver (lat, lng, distance, timestamp) values which are directly collected from gps data.

ex) 35.3515354 126.41515 4.23 2022-05-12T06:41:13+09:00

If vehicle arrive final destination, this process will be closed.