# Meteorite Landing Calculator
<p>Scenario: You are operating a robotic vehicle on Mars and tasked to investigate *five* meteorite landing sites in [Syrtis Major](https://en.wikipedia.org/wiki/Syrtis_Major_quadrangle). You need to calculate the time your robot takes to investigate the sites so that you can report to your supervisor.<br>
The Meteorite Landing Calculator helps you generate five random meteorite landing sites and calculate the travel time between each site, as well as the total time the robot takes to complete its mission.</p>

Author: Dhanny Indrakusuma (dwi67)

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example:

git clone


## Running the code

This project contains two python scripts:
1. `json_site_generator.py`
2. `parse_site_data.py`

### `json_site_generator.py`
The script randomly generates latitude, longitude, and compositions for the five meteorite landing sites. The resulting data is then saved as a JSON file `landing_sites.json`.

<p>Sample output:</p>
```
{
  "sites": [
    {
      "site_id": 1,
      "latitude": 17.795271946171578,
      "longtitude": 82.19931472557363,
      "composition": "stony"
    },
    {
      "site_id": 2,
      "latitude": 17.301824374018125,
      "longtitude": 82.93033957813942,
      "composition": "iron"
    },
    {
      "site_id": 3,
      "latitude": 16.059552877895584,
      "longtitude": 82.88479209806685,
      "composition": "iron"
    },
    {
      "site_id": 4,
      "latitude": 17.206813848802927,
      "longtitude": 83.48826073324663,
      "composition": "stony-iron"
    },
    {
      "site_id": 5,
      "latitude": 16.487375413374888,
      "longtitude": 82.13628879847755,
      "composition": "stony"
    }
  ]
}
```

### `parse_site_data.py`
The script reads in the meteorite site JSON file `landing_sites.json` generated from `json_site_generator.py` and calculates the time required to visit and take samples from the five sites in order.<br>
The script contains two functions:
* `calc_gcd()`
* `main()`

<p>Sample output using data generated from `json_site_generator.py`:</p>
```
leg = 1, time to travel = 10.68 hr, time to sample = 1 hr
leg = 2, time to travel = 5.05 hr, time to sample = 2 hr
leg = 3, time to travel = 7.35 hr, time to sample = 2 hr
leg = 4, time to travel = 7.6 hr, time to sample = 3 hr
leg = 5, time to travel = 8.76 hr, time to sample = 1 hr
===============================
number of legs = 5, total time to sample = 48.44 hr
```
