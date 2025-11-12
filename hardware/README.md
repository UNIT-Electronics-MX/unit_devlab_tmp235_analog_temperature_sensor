# Hardware

<div align="center">
<a href="{{schematic_url}}"><img src="resources/Schematics_icon.jpg?raw=false" width="200px"><br/>Schematic</a>
</div>

## Technical Specifications

<div align="center">

| **Parameter** |            **Description**            | **Min** |  **Typ**   |    **Max**    | **Unit** |
|:-------------:|:-------------------------------------:|:-------:|:----------:|:-------------:|:--------:|
|      Vcc      | Input voltage to power on the module  |   2.3   |     -      |      5.5      |    V     |
|      Idd      |           Operating current           |    -    | 9(Ta=25°C) | 17 (Ta=150°C) |    uA    |
|     Tacy*     |         Temperature accuracy          |   -2    |    ±0.5    |      +2       |    °C    |
|      V0℃     |     Output voltage offset at 0°C      |    -    |    500     |       -       |    mV    |
|      Tc       | Temperature coefficient (sensor gain) |    -    |     10     |       -       |  mv/°C   |
|     Iout      |            Output current             |    -    |     -      |      500      |    uA    |

</div>

*The accuracy may change with the temperature.

### Transfer table
<div align="center">

| TEMPERATURE (°C) | VOUT (mV) Ideal linear values  |
|:----------------:|:------------------------------:|
|        –40       |               100              |
|        –35       |               150              |
|        –30       |               200              |
|        –25       |               250              |
|        –20       |               300              |
|        –15       |               350              |
|        –10       |               400              |
|        –5        |               450              |
|         0        |               500              |
|         5        |               550              |
|        10        |               600              |
|        15        |               650              |
|        20        |               700              |
|        25        |               750              |
|        30        |               800              |
|        35        |               850              |
|        40        |               900              |
|        45        |               950              |
|        50        |              1000              |
|        55        |              1050              |
|        60        |              1100              |
|        65        |              1150              |
|        70        |              1200              |
|        75        |              1250              |
|        80        |              1300              |
|        85        |              1350              |
|        90        |              1400              |
|        95        |              1450              |
|        100       |              1500              |
|        105       |              1550              |
|        110       |              1600              |
|        115       |              1650              |
|        120       |              1700              |
|        125       |              1750              |
|        130       |              1800              |
|        135       |              1850              |
|        140       |              1900              |
|        145       |              1950              |
|        150       |              2000              |

</div>

## 🔌 Pinout

<div align="center">
    <a href="#"><img src="resources/unit_pinout_v_0_0_1_ue0094_icp10111_barometric_pressure_sensor_en.jpg" width="500px"><br/>Pinout</a>
    <br/>
    <br/>
    <br/>
    

| Pin Label | Function    | Notes                             |
|-----------|-------------|-----------------------------------|
| VCC       | Power Supply| 3.3V or 5V                       |
| GND       | Ground      | Common ground for all components  |

</div>

## 📃 Topology

<div align="center">
<a href="./resources/unit_topology_v_1_0_ue0101_TEMP235.png"><img src="./resources/unit_topology_v_1_0_ue0101_TEMP235.png" width="500px"><br/> Topology</a>
<br/>
<br/>
<br/>

| Ref. | Description                                                                |
|------|----------------------------------------------------------------------------|
| IC1  | TEMP235 Temperature Sensor                                                 |
| L1   | Power On LED                                                               | 
| JP1  | 2.54 mm Header                                                             |
| J1   | JST 1 mm pitch for Input Signals                                           |
| J2   | JST 2 mm pitch (Pads) for Input Signals, Compatible with Gravity Connector |

</div>

## Pin & Connector Layout

<div align="center">

| Pin    | Voltage Level | Function                                                  |
|--------|---------------|-----------------------------------------------------------|
| VCC    | 3.3 V – 5.5 V | Provides power to the on-board regulator and sensor core. |
| GND    | 0 V           | Common reference for power and signals.                   |
| Signal | 100 mV - 2V   | Sensor output signal.                                     |

</div>

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

## 📏 Dimensions

<div align="center">
<a href="./resources/unit_dimensions_v_1_0_ue0101_TEMP235.png"><img src="./resources/unit_dimensions_v_1_0_ue0101_TEMP235.png" width="500px"><br/> Dimensions</a>
</div>

# References

- <a href="https://www.ti.com/lit/ds/symlink/tmp235.pdf?ts=1762988208357&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252Fes-mx%252FTMP235"> TMP235 Datasheet </a>
