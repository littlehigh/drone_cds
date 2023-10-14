###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

from __future__ import print_function

# Updating the system path is not required if you have pip-installed
# rticonnextdds-connector
import rticonnextdds_connector as rti
import time
with rti.open_connector(
        config_name="MyParticipantLibrary::MySubParticipant",
        url="test.xml") as connector:

    input = connector.get_input("MySubscriber::MyDroneReader")

    print("Waiting for publications...")
    input.wait_for_publications() # wait for at least one matching publication

    print("Waiting for data...")
    while True:

        # Topic 傳送無人機相關資訊
        input.wait()
        input.take()
        for sample in input.samples.valid_data_iter:
            data = sample.get_dictionary()
            running_time = data['running_time']
            drone_pitch = data['drone_pitch']
            drone_yaw = data['drone_yaw']
            drone_roll = data['drone_roll']
            drone_lon = data['drone_lon']
            drone_lat = data['drone_lat']
            drone_alt = data['drone_alt']
            GPS_signal_strength = data['GPS_signal_strength']
            drone_speed = data['drone_speed']
            drone_status = data['drone_status']
            flight_distance = data['flight_distance']
            battery_voltage = data['battery_voltage']
            battery_level = data['battery_level']
            battery_current = data['battery_current']

            print("running_time: " + repr(running_time) + "\n"
                  "drone_pitch: " + repr(drone_pitch) + "\n" 
                  "drone_yaw: " + repr(drone_yaw) + "\n"
                  "drone_roll: " + repr(drone_roll) + "\n"
                  "drone_lon: " + repr(drone_lon) + "\n"
                  "drone_lat: " + repr(drone_lat) + "\n"
                  "drone_alt: " + repr(drone_alt) + "\n"
                  "GPS_signal_strength: " + repr(GPS_signal_strength) + "\n"
                  "drone_speed: " + repr(drone_speed) + "\n"
                  "drone_status: " + repr(drone_status) + "\n"
                  "flight_distance: " + repr(flight_distance) + "\n"
                  "battery_voltage: " + repr(battery_voltage) + "\n"
                  "battery_level: " + repr(battery_level) + "\n"
                  "battery_current: " + repr(battery_current))

        print("================== Next Round ======================")
        time.sleep(0.5)
