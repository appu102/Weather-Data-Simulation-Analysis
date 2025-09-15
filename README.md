# Weather-Data-Simulation-Analysis

## Overview

This Python project simulates daily temperature data for a user-specified number of days using **NumPy**. It calculates key statistical measures (minimum, maximum, average) and detects anomalies (extremely hot or cold days) using **Z-score** and **Interquartile Range (IQR)** methods. The program also identifies the day(s) on which these extreme temperatures occur.

## Features

* Generate random temperature data for `n` days.
* Calculate minimum, maximum, and average temperatures.
* Detect hottest and coldest temperature anomalies using **Z-score** and **IQR**.
* Display the day number of occurrence for anomalies.
* Nicely formatted output with **°C** symbol.

## How to Run

1. Ensure Python and NumPy are installed.
2. Run the script:

   ```bash
   python weather_simulation.py
   ```
3. Enter the number of days for the weather report.
4. Choose the metric to display (`min`, `max`, or `avg`).
5. Choose whether to detect anomalies (`Yes` or `No`).

## Dependencies

* Python 3.x
* NumPy

## Example Output

```
Enter how many days weather report you want: 10
Temperatures: [30.25 27.48 32.62 ...]

Select specific metric type 'min' or 'max' or 'avg': max
Maximum Temperature in 10 days in the city: 35.12 °C

Enter Yes if you want to know the temp anomalies: Yes
Hottest temperature in these 10 days is on Day 3: 35.12 °C
Coldest temperature in these 10 days is on Day 7: 24.88 °C
```

## Future Improvements

* Add a line graph visualization of temperatures using **matplotlib**.
* Include options to simulate other weather parameters like humidity or rainfall.
* Export results to a CSV or Excel file for further analysis.
