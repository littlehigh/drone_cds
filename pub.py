from time import sleep

# Updating the system path is not required if you have pip-installed
# rticonnextdds-connector
import rticonnextdds_connector as rti
from dronekit import connect, VehicleMode
import time

# Connect to SITL_Drone
IP_addr = "127.0.0.1:14550" #Local 端測試, Port: 14550
vehicle = connect(IP_addr, wait_ready=True)
# 起始時間戳記
current_time = time.time()

with rti.open_connector(
        config_name="MyParticipantLibrary::MyPubParticipant",
        url="test.xml") as connector: 

    output = connector.get_output("MyPublisher::MyDroneWriter")

    print("Waiting for subscriptions...")
    output.wait_for_subscriptions()

    print("Writing...")
    
    while True:
        #無人機 已經運行的時間
        running_time = time.time() - current_time

        #無人機 三軸
        drone_pitch = vehicle.attitude.pitch
        drone_yaw = vehicle.attitude.yaw
        drone_roll = vehicle.attitude.roll

        #無人機 GPS 經度、緯度跟高度
        drone_lat = vehicle.location.global_frame.lat
        drone_lon = vehicle.location.global_frame.lon
        drone_alt = vehicle.location.global_frame.alt

        #GPS訊號量(可見衛星數量)
        GPS_signal_strength = vehicle.gps_0.satellites_visible

        #無人機 飛機狀態
        drone_status = vehicle.mode.name
        
        #無人機 垂直速度
        drone_speed = vehicle.groundspeed
        
        #無人機 距離
        takeoff_location_lat = vehicle.location.global_frame.lat
        takeoff_location_lon = vehicle.location.global_frame.lon
        current_location_lat = vehicle.location.global_frame.lat
        current_location_lon = vehicle.location.global_frame.lon
        flight_distance = pow(pow(abs(current_location_lat - takeoff_location_lat), 2) + pow(abs(current_location_lon - takeoff_location_lon), 2), 1/2)
        
        #無人機 電池相關資訊
        battery_voltage = vehicle.battery.voltage #電壓
        battery_level = vehicle.battery.level #剩餘電量
        battery_current = vehicle.battery.current #電流(>0 放電；<0 充電)

        output.instance.set_number("running_time", running_time)
        output.instance.set_number("drone_pitch", drone_pitch)
        output.instance.set_number("drone_yaw", drone_yaw)
        output.instance.set_number("drone_roll", drone_roll)
        output.instance.set_number("drone_lon", drone_lon)
        output.instance.set_number("drone_lat", drone_lat)
        output.instance.set_number("drone_alt", drone_alt)
        output.instance.set_number("GPS_signal_strength", GPS_signal_strength)
        output.instance.set_number("drone_speed", drone_speed)
        output.instance.set_string("drone_status", drone_status)
        output.instance.set_number("flight_distance", flight_distance)
        output.instance.set_number("battery_voltage", battery_voltage)
        output.instance.set_number("battery_level", battery_level)
        output.instance.set_number("battery_current", battery_current)

        output.write()
        sleep(1)
        output.wait() # Wait for all subscriptions to receive the data before exiting
