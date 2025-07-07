import asyncio
import copy
from device_info import build_device_info
from sensors import measure_hcsr04, read_uart_sensor, cleanup
from send_api import SendAPI

async def main():
    sender = SendAPI()
    info = build_device_info()

    hcsr04 = measure_hcsr04()
    uart = read_uart_sensor()

    water_lv = f"{hcsr04} cm" if hcsr04 is not None else "N/A"
    mud_lv = f"{uart} mm" if uart is not None else "N/A"

    sensorData = {
        "water_lv": water_lv,
        "mud_lv": mud_lv
    }

    # merged = {**info, **sensorData}


    merged = copy.deepcopy(info)
    merged.update(sensorData)

    payload = merged

    print("📤 Sending payload:", payload)
    response = await sender.send_api_request(payload)
    print("✅ Server Response:", response)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⛔️ Interrupted by user")
    finally:
        cleanup()
