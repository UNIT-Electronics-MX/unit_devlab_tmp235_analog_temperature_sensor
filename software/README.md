# TMP235 Temperature Sensor

**Arduino & MicroPython Examples – Pulsar C6 (ESP32-C6)**

## Overview

This repository provides **reference test code** for the **TMP235 analog temperature sensor**, validated on the **Pulsar C6 (ESP32-C6)** platform.
Both **Arduino** and **MicroPython** implementations are included, following the **official linear voltage–temperature curve** of the sensor.

The goal of this project is to offer a **simple, reliable, and well-documented baseline** for temperature measurements using the ESP32 ADC.

## Sensor Characteristics (TMP235)

The TMP235 is a **linear analog temperature sensor** with the following behavior:

* Linear output: **10 mV / °C**
* Output offset: **500 mV at 0 °C**
* Operating range (typical): **–40 °C to +150 °C**
* Supply voltage: **3.0 – 5.5 V** (3.3 V recommended)

### Ideal Linear Curve

| Temperature (°C) | Output Voltage (mV) |
| ---------------- | ------------------- |
| 0                | 500                 |
| 25               | 750                 |
| 50               | 1000                |
| 100              | 1500                |
| 150              | 2000                |

### Conversion Formula

```
Temperature (°C) = (Vout_mV − 500) / 10
```



## Hardware Connection (Pulsar C6)

| TMP235 Pin | Pulsar C6    |
| ---------- | ------------ |
| VCC        | 3.3 V        |
| GND        | GND          |
| VOUT       | GPIO 6 (ADC) |



## Arduino Version

### Features

* Uses ESP32 ADC with 12-bit resolution
* ADC attenuation set for 0–3.3 V
* Averaged readings for stability
* Temperature calculation based on TMP235 curve

### Core Code Snippet

```cpp
float voltage = (raw / 4095.0) * 3.3;
float temperatureC = (voltage - 0.5) * 100.0;
```

### Expected Output (Serial Monitor)

```
Raw: 930 | Voltage: 0.750 V | Temp: 25.0 °C
Raw: 990 | Voltage: 0.800 V | Temp: 30.0 °C
```



## MicroPython Version

### Features

* Native MicroPython ADC usage
* 12-bit ADC resolution
* Software averaging
* Same linear conversion model as Arduino

### Core Code Snippet

```python
voltage_mv = (raw / 4095) * 3300
temperature_c = (voltage_mv - 500) / 10
```

### Example Output

```
ADC: 930 | Voltage: 750.0 mV | Temp: 25.0 °C
ADC: 985 | Voltage: 800.4 mV | Temp: 30.0 °C
```

## Validation & Debugging Guide

### Quick Sanity Check

| Condition                 | Expected Voltage |
| ------------------------- | ---------------- |
| Room temperature (~25 °C) | ~750 mV          |
| Touching sensor           | Voltage rises    |
| Cold environment          | <700 mV          |

### Common Issues

| Symptom           | Likely Cause                                 |
| ----------------- | -------------------------------------------- |
| Always ~10 °C     | Environment really cold or wrong expectation |
| Noisy readings    | Missing capacitors                           |
| Very low voltage  | Wrong pin or wiring                          |
| Wrong temperature | Using TMP36 formula instead of TMP235        |


## Notes on ESP32 ADC

* ESP32 ADC is **not perfectly linear**
* For relative and ambient measurements, this approach is sufficient
* For precision applications:

  * Use calibration
  * Consider an external ADC
  * Perform two-point calibration in software

## Applications

* Embedded temperature monitoring
* Environmental sensing
* Board thermal validation
* DevLab / Pulsar module testing
* Educational ADC examples


## Compatibility

* Pulsar C6 (ESP32-C6)
* Arduino-ESP32 core
* MicroPython (ESP32 build)


## License

MIT License
Feel free to use, modify, and integrate into DevLab or UNIT Electronics projects.

