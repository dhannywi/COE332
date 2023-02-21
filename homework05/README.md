# ISS Tracker App
**Scenario**: The previous API developed for the ISS positional and velocity data in [homework 04](https://github.com/dhannywi/COE332/tree/main/homework04) is a great start! But, we have made improvements to make the API more useful and  *portable*.

**Scenario:** There is an abundance of interesting positional and velocity data for the International Space Station (ISS), though it is a challenge to sift through the data manually to find what you are looking for.
ISS Tracker is a Flask application for querying and returning interesting information from the ISS data set.

You can find more information about the dataset used in the [ISS Trajectory Data](https://spotthestation.nasa.gov/trajectory_data.cfm) website. The Orbital Ephemeris Message (OEM) data used contains ISS state vectors over a ~15 day period.

## Getting Started

Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example: `git clone https://github.com/dhannywi/COE332.git`

After cloning `COE332`, change your directory to `homework05` sub-folder that contains the scripts and README for the ISS Tracker App. Execute the command `cd .\COE332\homework05\` on your terminal to change directory.

### Dependencies
The scripts was created using **Python 3.8.10**, please ensure that you have the same version or higher when running the scripts. You can download Python [here](https://www.python.org/).

You need to have the following libraries installed prior to running the scripts:
* `math`: Part of Python standard libraries
* `flask`: Execute `pip3 install --user flask` on your terminal to install
* `requests`: Execute `pip3 install --user requests` on your terminal to install
* `xmltodict`: Execute `pip3 install --user xmltodict` on your terminal to install

### Running the Flask App
The `iss_tracker.py` script contains the code needed to run the ISS Tracker App. To run the flask app, Execute the command `flask --app iss_tracker --debug run` on your terminal. Your local server is up and running when you see the message similar to this:

```console
username:~/COE332/homework04$ flask --app iss_tracker --debug run
 * Serving Flask app 'iss_tracker'
 * Debug mode: on                 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server in
stead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 602-054-580
```

### Querying ISS data
Once you get the server running, there are four routes that you can request data from:

|    | Route | Method | What it should return |
| -- | ----- | ------ | --------------------- |
| 1. | `/`   | GET | The entire data set   |
| 2. | `/epochs` | GET | A list of all Epochs in the data set |
| 3. | `/epochs?limit=int&offset=int` | GET | Return modified list of Epochs given query parameters |
| 4. | `/epochs/<epoch>` | GET | State vectors for a specific Epoch from the data set |
| 5. | `/epochs/<epoch>/speed` | GET | Instantaneous speed for a specific Epoch in the data set |
| 6. | `/help` | GET | Return help text (as a string) that briefly describes each route |
| 7. | `/delete-data` | DELETE | Delete all data from the dictionary object |
| 8. | `/post-data` | POST | Reload the dictionary object with data from the web |


#### 1. Route `/`
Since we need to keep the server running in order to make requests, open an additional shell and change your directory to the `homework04` folder. Now we will make a request to the Flask app by executing the command `curl localhost:5000` on your terminal. The output should be similar as below:

```console
username:~/COE332/homework04$ curl localhost:5000
{ .....
              {
                "EPOCH": "2023-061T12:00:00.000Z",
                "X": {
                  "#text": "3578.8574821437401",
                  "@units": "km"
                },
                "X_DOT": {
                  "#text": "5.03904352218286",
                  "@units": "km/s"
                },
                "Y": {
                  "#text": "-5454.7252313410299",
                  "@units": "km"
                },
                "Y_DOT": {
                  "#text": "1.32725609415084",
                  "@units": "km/s"
                },
                "Z": {
                  "#text": "1908.4598652639199",
                  "@units": "km"
                },
                "Z_DOT": {
                  "#text": "-5.6136727354188301",
                  "@units": "km/s"
                }
              }
            ]
          },
          "metadata": {
            "CENTER_NAME": "EARTH",
            "OBJECT_ID": "1998-067-A",
            "OBJECT_NAME": "ISS",
            "REF_FRAME": "EME2000",
            "START_TIME": "2023-046T12:00:00.000Z",
            "STOP_TIME": "2023-061T12:00:00.000Z",
            "TIME_SYSTEM": "UTC"
          }
        }
      },
      "header": {
        "CREATION_DATE": "2023-047T00:51:05.746Z",
        "ORIGINATOR": "JSC"
      }
    }
  }
}
```

#### 2. Route `/epochs`
Next, we will query for a list of all Epochs in the data set. Execute the command `curl localhost:5000/epochs` on your terminal, and you should get output similar to this:

```console
username:~/COE332/homework04$ curl localhost:5000/epochs
[ ....,
  "2023-061T11:35:00.000Z",
  "2023-061T11:39:00.000Z",
  "2023-061T11:43:00.000Z",
  "2023-061T11:47:00.000Z",
  "2023-061T11:51:00.000Z",
  "2023-061T11:55:00.000Z",
  "2023-061T11:59:00.000Z",
  "2023-061T12:00:00.000Z",
  ....
]
```

#### 3. Route `/epochs?limit=int&offset=int`

#### 4. Route `/epochs/<epoch>`
Since we now know the epochs in the data set, we can query for the state vectors for a specific Epoch. To do this, Execute the command `curl localhost:5000/epochs/<epoch>` on your terminal, but replace `<epoch>` with a particular epoch you are interested in.
For example: `curl localhost:5000/epochs/2023-061T08:09:00.000Z`

The resulting output will be similar to below:

```console
username:~/COE332/homework04$ curl localhost:5000/epochs/2023-061T08:09:00.000Z
{
  "EPOCH": "2023-061T08:09:00.000Z",
  "X": {
    "#text": "-3961.79394994832",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "-4.7028919269355596",
    "@units": "km/s"
  },
  "Y": {
    "#text": "5298.7862135964297",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "-1.8472846937741301",
    "@units": "km/s"
  },
  "Z": {
    "#text": "-1545.43747234906",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "5.7616942719771602",
    "@units": "km/s"
  }
}
```

However, if you request an invalid epoch, for example `curl localhost:5000/epochs/xyz`, you will get:
```console
username:~/COE332/homework04$ curl localhost:5000/epochs/xyz
The epoch you requested is not in the data.
```

#### 5. Route `/epochs/<epoch>/speed`
Lastly, we can also query for the instantaneous speed for a specific Epoch in the data set by executing the command `curl localhost:5000/epochs/<epoch>/speed` on your terminal, but replace `<epoch>` with a particular epoch you are interested in.
For example: `curl localhost:5000/epochs/2023-061T08:09:00.000Z/speed`

It will output the resulting speed calculation as below:
```console
username:~/COE332/homework04$ curl localhost:5000/epochs/2023-061T08:09:00.000Z/speed
The instantaneous speed for the epoch you requested is 7.6633 km/s.
```

However, if you request an invalid epoch, for example `curl localhost:5000/epochs/xyz/speed`, you will get:
```console
username:~/COE332/homework04$ curl localhost:5000/epochs/xyz/speed
We are unable to calculate speed as the epoch you requested is not in the data.
```

#### 6. Route `/help`

#### 7. Route `/delete-data`

#### 8. Route `/post-data`

## Additional Resources

* [NASA Data Set](https://spotthestation.nasa.gov/trajectory_data.cfm)

## Authors

Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
