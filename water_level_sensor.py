from setting import VREF, V_MIN, V_MAX, MAX_WATER_LEVEL, WATER_LEVEL_OFFSET

class WaterLevelSensor:
    def __init__(self, spi_handler):
        self.spi = spi_handler

    def get_water_level(self, channel=7):
        adc_value = self.spi.read_channel(channel)
        voltage = (adc_value / 1023.0) * VREF  
        # print(f"ADC Value: {adc_value}, Voltage: {voltage:.2f} mV")  

        if voltage < V_MIN:
            water_level = 0.0  
        elif voltage > V_MAX:
            water_level = MAX_WATER_LEVEL  
        else:
            water_level = ((voltage - V_MIN) / (V_MAX - V_MIN)) * MAX_WATER_LEVEL * 0.9  

        water_level += WATER_LEVEL_OFFSET
        # print(f"Calculated Water Level: {water_level:.2f}")  
        return max(0.0, min(water_level, MAX_WATER_LEVEL))
