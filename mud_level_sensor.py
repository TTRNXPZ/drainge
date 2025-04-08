from setting import MUD_TURBIDITY_THRESHOLDS

class MudLevelSensor:
    def __init__(self, spi_handler):
        self.spi = spi_handler
        self.last_mud_level = None

    def get_mud_level(self, turbidity_channels=[0, 1, 2]):
        turbidity_values = [self.spi.read_channel(ch) for ch in turbidity_channels]
        # print(f"Turbidity Values: {turbidity_values}")  

        # for level, (t1, t2, t3) in MUD_TURBIDITY_THRESHOLDS.items():
        #           # print(f"Checking Level {level}: {t1}, {t2}, {t3}") 
        #     print(f"True Flase: {t1}|{turbidity_values[0]} {turbidity_values[0] <= t1} {t2}|{turbidity_values[1]} {turbidity_values[1] <= t2} {t3}|{turbidity_values[2]} {turbidity_values[2] <= t3}")
        #     if turbidity_values[0] <= t1 and turbidity_values[1] <= t2 and turbidity_values[2] <= t3:
        #         mud_level = f"{level}"
        #         print(f"Mud Level Changed: {level}") 
        #         break
        #     else:
        #         mud_level = "0.00"

        turbidity1, turbidity2, turbidity3 = turbidity_values

        if (turbidity1 <= 200) and (turbidity2 > 200) and (turbidity3 > 200):
            mud_level = "0.25"
        elif (turbidity1 <= 200) and (turbidity2 <= 200) and (turbidity3 > 200):
            mud_level = "0.50"
        elif (turbidity1 <= 200) and (turbidity2 <= 200) and (turbidity3 <= 200):
            mud_level = "0.75"
        elif (turbidity1 > 200) and (turbidity2 > 200) and (turbidity3 > 200):
            mud_level = "0.00"
        else:
            mud_level = "0.00"



        if mud_level != self.last_mud_level:
            print(f"Mud Level Changed: {mud_level}")  
            self.last_mud_level = mud_level

        return mud_level