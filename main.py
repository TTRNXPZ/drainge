import asyncio
from setting import SAMPLES_PER_CYCLE, SAMPLE_DELAY
from spi_handler import SPIHandler
from water_level_sensor import WaterLevelSensor
from mud_level_sensor import MudLevelSensor
from api import SendAPI

class SensorMonitor:
    def __init__(self):
        self.spi_handler = SPIHandler()
        self.water_sensor = WaterLevelSensor(self.spi_handler)
        self.mud_sensor = MudLevelSensor(self.spi_handler)
        self.api = SendAPI()

    async def read_sensors(self):
        water_level_readings = []

        for _ in range(SAMPLES_PER_CYCLE):
            water_level = self.water_sensor.get_water_level()
            mud_level = self.mud_sensor.get_mud_level()

            water_level_readings.append(water_level)
            await asyncio.sleep(SAMPLE_DELAY)

        average_water_level = sum(water_level_readings) / len(water_level_readings)

        return average_water_level, mud_level

    async def send_data(self, water_level, mud_level):
        data = {
            "water_level": water_level,
            "mud_level": mud_level
        }
        response = await self.api.send_api_request(data)

        print(f"API Response: {response}")

    async def start_monitoring(self):
        try:
            while True:
                water_level, mud_level = await self.read_sensors()
                print(f"Final Water Level: {water_level:.2f}, Mud Level: {mud_level}")  # ?? Debug ??????
                await self.send_data(f"{float(water_level):.2f}", f"{float(mud_level):.2f}")
        except KeyboardInterrupt:
            print("\n Exiting...")
            self.spi_handler.close()


if __name__ == "__main__":
    monitor = SensorMonitor()
    asyncio.run(monitor.start_monitoring())
