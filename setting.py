
SPI_BUS = 0
SPI_DEVICE = 0
SPI_SPEED_HZ = 1350000
SPI_MODE = 0

# SPI = {
#     "BUS": 0,
#     "DEVICE": 0,
#     "SPEED_HZ": 1350000,
#     "MODE": 0
# }

VREF = 5000    
V_MIN = 490   
V_MAX = 5000       
MAX_WATER_LEVEL = 5.0  
WATER_LEVEL_OFFSET = 0.30  

MUD_TURBIDITY_THRESHOLDS = {
    "0.00": (200, 200, 200),  
    "0.25": (0, 200, 200),
    "0.50": (0, 0, 200),
    "0.75": (0, 0, 0)
}

SAMPLES_PER_CYCLE = 100 
SAMPLE_DELAY = 0.05  
