# ISS Tracker App

Orbital Ephemeris Message (OEM) data containing ISS state vectors over a ~15 day period.




## Getting Started

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example: `git clone https://github.com/dhannywi/COE332.git`

<br>

After cloning `COE332`, change your directory to `homework04` sub-folder that contains the scripts and README for the ISS Tracker App. Execute the command `cd .\COE332\homework04\` on your terminal to change directory.

### Dependencies
The scripts was created using <b>Python 3.8.10</b>, please ensure that you have the same version or higher when running the scripts. You can download Python <a href="https://www.python.org/">here</a>.
<br>
You need to have the following libraries installed prior to running the scripts:
* `math`: Part of Python standard libraries
* `flask`: Execute `pip3 install --user flask` on your terminal to install
* `requests`: Execute `pip3 install --user requests` on your terminal to install
* `xmltodict`: Execute `pip3 install --user xmltodict` on your terminal to install

### Running the Flask App
The `iss_tracker.py` script contains the code needed to run the ISS Tracker App. To run the flask app, Execute the command `flask --app iss_tracker --debug run` on your terminal. Your server is up and running when you see the message similar to this:<br>

'''
[username]:~/COE332/homework04$ flask --app iss_tracker --debug run
 * Serving Flask app 'iss_tracker'
 * Debug mode: on                 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server in
stead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 602-054-580
'''

Since we need to keep the server running in order to make requests, open an additional shell and change your directory to the `homework04` folder. This time, we will make a request to the Flask app by executing the command curl localhost:5000` on your terminal.

## Authors

Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
