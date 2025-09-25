# Hardware

<div align="center">
<a href="{{schematic_url}}"><img src="resources/Schematics_icon.jpg?raw=false" width="200px"><br/>Schematic</a>
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

## 📏 Dimensions

<div align="center">
<a href="./resources/unit_dimensions_v_1_0_ue0101_TEMP235.png"><img src="./resources/unit_dimensions_v_1_0_ue0101_TEMP235.png" width="500px"><br/> Dimensions</a>
</div>

## 📃 Topology

<div align="center">

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
| Pin   | Voltage Level | Function                                                  |
|-------|---------------|-----------------------------------------------------------|
| VCC   | 3.3 V – 5.5 V | Provides power to the on-board regulator and sensor core. |
| GND   | 0 V           | Common reference for power and signals.                   |
| SDA   | 1.8 V to VCC  | Serial data line for I²C communications.                  |
| SCL   | 1.8 V to VCC  | Serial clock line for I²C communications.                 |

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

## Functional Description

{{functional_description}}

## Applications

{{applications_list}}

# References

- [{{datasheet_name}}]({{datasheet_url}})
