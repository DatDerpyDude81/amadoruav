import asyncio
from mavsdk import System
import mavsdk
import mavsdk.telemetry

async def safetycheck(drone):
    if(mavsdk.telemetry.Health(True,True,True,True,True,True,True)==False):
        #yo drones boutta crash
        await asyncio.sleep(30)
        if(mavsdk.telemetry.Health(True,True,True,True,True,True,True)==False):
            await drone.action.return_to_launch()
            await asyncio.sleep(180)
            if(mavsdk.telemetry.Health(True,True,True,True,True,True,True)==False):
                drone.action.kill()
                
            
            
            
            
        




async def run():
    drone = System()
    await drone.connect(system_address="ADDRESS")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position state is good enough for flying.")
            break

    print("Fetching amsl altitude at home location....")
    async for terrain_info in drone.telemetry.home():
        absolute_altitude = terrain_info.absolute_altitude_m
        break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()
    await safetycheck(drone)
    await asyncio.sleep(1)
    # To fly drone 20m above the ground plane
    flying_alt = absolute_altitude + 20.0
    await safetycheck(drone)
    # goto_location() takes Absolute MSL altitude
    await drone.action.goto_location("GPSX", "GPSY", flying_alt, 0)
    await safetycheck(drone)
    await asyncio.sleep(1)
    print("dropping payload")
    #drop payload
    mavsdk.telemetry.ActuatorControlTarget(1, 1)
    await asyncio.sleep(1)
    mavsdk.telemetry.ActuatorControlTarget(1, -1)
    await asyncio.sleep(1)
    
    
    await safetycheck(drone)
    


    # start manual control
    print("-- Starting manual control")
    await drone.manual_control.start_position_control()
    while True:
        await safetycheck(drone)
        await drone.manual_control.set_manual_control_input("PITCH","ROLL","THROTTLE","YAW")

        await asyncio.sleep(1)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())