from machine import ADC, Pin
import time

# TMP235 on GPIO 6
adc = ADC(Pin(6))
adc.atten(ADC.ATTN_11DB)   # 0–3.3V range
adc.width(ADC.WIDTH_12BIT)

def read_temperature(samples=20):
    total = 0
    for _ in range(samples):
        total += adc.read()
        time.sleep_ms(5)

    raw = total / samples

    # Convert raw ADC to millivolts
    # ESP32 ADC: 12-bit -> 0..4095
    voltage_mv = (raw / 4095.0) * 3300.0

    # TMP235 conversion (your curve)
    temperature_c = (voltage_mv - 500.0) / 10.0

    return raw, voltage_mv, temperature_c


print("TMP235 MicroPython test started")

while True:
    raw, mv, temp = read_temperature()

    print(
        "ADC:", int(raw),
        "| Voltage:", round(mv, 1), "mV",
        "| Temp:", round(temp, 2), "°C"
    )

    time.sleep(1)
