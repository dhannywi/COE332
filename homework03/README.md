# Water Analyzer


You can find the water quality data used <a href="https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json">here</a>

## Getting Started

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example: <br>

`git clone https://github.com/dhannywi/COE332.git`

<br>

After cloning `COE332`, change your directory to `homework03` sub-folder that contains the scripts and README for the Water Analyzer. Execute below command on your terminal to change directory: <br>
`cd .\COE332\homework03\`


### Dependencies

The scripts was created using <b>Python 3.8.10</b>, please ensure that you have the same version or higher when running the scripts. 
You can download Python <a href= "https://www.python.org/">here</a>.<br> 
You need to have the following libraries installed prior to running the scripts:
* `math`: Part of Python standard libraries
* `requests`: Execute `pip3 install --user requests` on your terminal to install

### Executing program

This project contains two python scripts:

1.  `analyze_water.py`
2.  `test_analyze_water.py`

#### 1. `analyze_water.py`

The script contains three functions:
* `turbidity()`
* `min_return_time()`
* `main()` fetches water quality data and analyze the 5 most recent readings to get an average turbidity value. 

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

## Additional Resources

* <a href='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json'>Water quality data</a>
* <a href='https://www.fondriest.com/environmental-measurements/measurements/measuring-water-quality/turbidity-sensors-meters-and-methods/'>Water turbidity equations</a>

## Authors
Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
