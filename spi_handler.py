import spidev
from setting import SPI_BUS, SPI_DEVICE, SPI_SPEED_HZ, SPI_MODE

class SPIHandler:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(SPI_BUS, SPI_DEVICE)
        self.spi.max_speed_hz = SPI_SPEED_HZ
        self.spi.mode = SPI_MODE

    def read_channel(self, channel):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        # print(f"SPI Read [Channel {channel}]: {data}")
        return data

    def close(self):
        self.spi.close()
