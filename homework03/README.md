# Water Turbidity Analyzer

<b>Scenario:</b> Your robot has finished collecting its five meteorite samples and has taken them back to the Mars lab for analysis. In order to analyze the samples, however, you need clean water. You must check the latest water quality data to assess whether it is safe to analyze samples, or if the Mars lab should go on a boil water notice.

The Water Turbidity Analyzer reads in water quality data and analyze the 5 most recent readings to get an average turbidity value. It outputs to the user the current water turbidity (taken as the average of the most recent five data points), information whether turbidity is below the safe threshold, and minimum time required for turbidity to fall below the safe threshold.

You can find the water quality data used <a href="https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json">here</a>.

## Getting Started

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example: <br>

`git clone https://github.com/dhannywi/COE332.git`

<br>

After cloning `COE332`, change your directory to `homework03` sub-folder that contains the scripts and README for the Water Turbidity Analyzer. Execute below command on your terminal to change directory: <br>
`cd .\COE332\homework03\`


### Dependencies

The scripts was created using <b>Python 3.8.10</b>, please ensure that you have the same version or higher when running the scripts. 
You can download Python <a href= "https://www.python.org/">here</a>.<br> 
You need to have the following libraries installed prior to running the scripts:
* `math`: Part of Python standard libraries
* `pytest`: Execute `pip3 install --user pytest` on your terminal to install. The version used is `pytest 7.2.1`.
* `requests`: Execute `pip3 install --user requests` on your terminal to install

### Executing program

This project contains two python scripts:

1.  `analyze_water.py`
2.  `test_analyze_water.py`

#### 1. `analyze_water.py`
This script reads in water quality data and analyze the 5 most recent readings to get an average turbidity value. It outputs to the user the current water turbidity (taken as the average of the most recent five data points), information whether turbidity is below the safe threshold, and minimum time required for turbidity to fall below the safe threshold.

The script contains three functions:
* `turbidity()` calculates water turbidity based on readings taken by a nephelometer.
* `min_return_time()` calculates minimum time to return below a safe threshold.
* `main()` fetches water quality data and outputs appropriate information.

Execute the command `python3 analyze_water.py` on your terminal to run the script.
<p>The output might look similar to one of the following sample outputs, depending on whether turbidity is above or below the safe threshold:</p>

```
Average turbidity based on most recent five measurements = 0.6631 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
```

```
Average turbidity based on most recent five measurements = 1.1539 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.09 hours
```

#### 2. `test_analyze_water.py`
The script utilize `pytest` to test if the two functions `turbidity()` `min_return_time()` from `analyze_water` module returns the expected values.

This script contains two functions:
* `test_turbidity()` Tests `turbidity()` function from `analyze_water` module for correct calculation result and correct output type.
* `test_min_return_time()` Tests `min_return_time()` function from `analyze_water` module for correct calculation results and correct output types, for cases when average turbidity is above or below normal threshold.

Execute the command `pytest` on your terminal to run the test.
When you pass all the test cases, your output will look similar to this: <br>

```
========================================================== test session starts ===========================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/dwi67/COE332/homework03
collected 2 items

test_analyze_water.py ..                                                                                                           [100%]

=========================================================== 2 passed in 0.07s ============================================================
```

## Additional Resources

* <a href='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json'>Water quality data</a>
* <a href='https://www.fondriest.com/environmental-measurements/measurements/measuring-water-quality/turbidity-sensors-meters-and-methods/'>Water turbidity equations</a>

## Authors
Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
