# Gene-ius

A containarized Flask application with persisting Redis NoSQL database integration for querying and returning interesting information from HGNC data published by The Human Genome Organization (HUGO). 

The REST API's repository includes Dockerfile for protability, and included Docker Compose to automate deployment.

## Data Description
`----------add description---------`
More details about the dataset used can be found in the [HGNC complete set archive](https://www.genenames.org/download/archive/) website.

## Implementation
The project uses **Python 3.8.10**, in particular **Flask 2.2.2**, **redis 4.5.1** and **Docker 20.10.12** for containerization. 

Specific Python3 libraries are used:
* `flask`
* `json`
* `redis`
* `requests`
* `pyyaml`

### Files
* `Dockerfile` -- commands for building a new image
* `docker-compose.yml` -- container application management
* `gene_api.py` -- python scripts for the Flask application
* `README.md` -- project documentation

## Installation

You have the option to build this project from source, or use the provided Docker container on DockerHub. A Docker installation is required, as we build and run a Docker image.

We describe below the installation process using terminal commands, which are expected to run on a Ubuntu 20.04.5 machine with Python3. Installation may differ for other systems.

<details>
<summary><h3>From Docker (option 1)</h3></summary>

**Install**

* To install the Docker container, first install Docker: `sudo apt-get install docker` or follow installation instructions for [Docker Desktop](https://www.docker.com/get-started/) for your system. We are using Docker 20.10.12

* Next, pull the images from the docker hub and install the containers: `docker pull dhannywi/gene-ius` and `docker pull redis:7`

* Check the docker images currently running in your computer by executing: `docker images`
The image you just installed would show up in the list of images:
```console
username:~/COE332/homework06$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED             SIZE
dhannywi/gene-ius      latest    ba82680f899d   8 minutes ago       903MB
redis                  7         dd786f66ff99   8 minutes ago       117MB
```

**Run**

* To run the code, execute: `add command` 
The terminal should return a link, which can be viewed via a browser or with the curl commands documented in the API reference section. Your local server is up and running when you see this message:
```console

```

</details>


<details>
<summary><h3>Source build (option 2)</h3></summary>

Since this is a Docker build, the requirements need not be installed, as it will automatically be done on the Docker image. All commands, unless otherwise noted, are to be run in a terminal (in the `homework06` directory of the cloned repository).

* First, install Docker: `sudo apt-get install docker` or follow installation instructions for [Docker Desktop](https://www.docker.com/get-started/) for your system. We are using **Docker 20.10.12**
* Next, install docker-compose: `sudo apt-get install docker-compose-plugin` or follow the instructions [here](https://docs.docker.com/compose/install/linux/). We are using **Docker Compose 1.25.0**
* Clone the  repository: `git clone https://github.com/dhannywi/COE332.git`
* Then, change directory into the `homework06` folder: `cd .\homework06\`
* The folder should contain four files: `Dockerfile`, `docker-compose.yml`, `gene_api.py`, and `README.md`


### **Option 1:** Automate deployment using `docker-compose`
The quickest way to get your services up and running is to use `docker-compose` to automate deployment.
* Create a `data` folder inside the `homework06` directory. Execute `mkdir data`. This allows redis to store data in the disk so that the data persist, even when the services are killed.
* Execute `docker-compose up --build`. Your images are built and services are up and running when you see this message:
```console
username::~/COE332/homework06$ docker-compose up --build
Creating network "homework06_default" with the default driver
Building flask-app
...
...
Successfully built ba82680f899d
Successfully tagged dhannywi/gene-ius:latest
Creating homework06_redis-db_1 ... done
Creating homework06_flask-app_1 ... done
Attaching to homework06_redis-db_1, homework06_flask-app_1
redis-db_1   | 1:C 29 Mar 2023 02:23:48.490 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
...
...
redis-db_1   | 1:M 29 Mar 2023 02:23:48.686 * Ready to accept connections
flask-app_1  |  * Serving Flask app 'gene_api'
flask-app_1  |  * Debug mode: on
flask-app_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
flask-app_1  |  * Running on all addresses (0.0.0.0)
flask-app_1  |  * Running on http://127.0.0.1:5000
flask-app_1  |  * Running on http://172.29.0.3:5000
flask-app_1  | Press CTRL+C to quit
flask-app_1  |  * Restarting with stat
flask-app_1  |  * Debugger is active!
flask-app_1  |  * Debugger PIN: 707-110-167
```

* Execute `docker ps -a`. You should see the containers running.
```console
username:~/COE332/homework06$ docker ps -a
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS                     PORTS
          NAMES
d1e8117bdd49   dhannywi/gene-ius   "python gene_api.py"     49 minutes ago   Up 49 minutes              0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   homework06_flask-app_1
90f7ace06c22   redis:7             "docker-entrypoint.s…"   49 minutes ago   Up 49 minutes              0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework06_redis-db_1
```

### **Option 2:** Build and run your own docker image
* First, create a `data` folder inside the `homework06` directory. Execute `mkdir data`. This allows redis to store data in the disk so that the data persist even when the services are killed.
* Now, build the image: `docker build -t dhannywi/gene-ius .`
This output shows that your build is successful:
```console

```

* Check the docker images currently running in your computer by executing: `docker images`. The image you just built would show up in the list of images:
```console
username:~/COE332/homework06$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED             SIZE
dhannywi/gene-ius      latest    ba82680f899d   8 minutes ago       903MB
redis                  7         dd786f66ff99   8 minutes ago       117MB
```

* Execute `docker run -d -p 6379:6379 -v <path/on/host>/data:/data:rw redis:7 --save 1 1` command, but replace the `</path/on/host>` with the present working directory of the `homework06` folder. You can fing the path by executing `pwd`

* Now, your services is up and running

##
**Killing the services**
If you madea any changes to the `gene_api.py` file, you will need to kill the existing services that's running and rebuild. Execute `docker-compose down`. The services are removed when you see the following message:
```console
username:~/COE332/homework06$ docker-compose down
Removing homework06_flask-app_1 ... done
Removing homework06_redis-db_1  ... done
Removing network homework06_default
```

</details>
<br>

## Usage
Once you have the docker image running with dependencies installed and the local server running, we can start querying using the REST API in the Flask app.

There are thirteen routes for you to request data from:

|    | Route | Method | What it returns |
| -- | ----- | ------ | --------------------- |
| 1. | `/data`   | POST | Put data into Redis   |
| 2. | `/data` | GET | Return all data from Redis |
| 3. | `/data` | DELETE | Delete data in Redis |
| 4. | `/genes` | GET | Return json-formatted list of all hgnc_ids |
| 5. | `/genes/<hgnc_id>` | GET | Return all data associated with <hgnc_id> |


### Querying HGNC data using the REST API
Since we need to keep the server running in order to make requests, open an additional shell and change your directory to the same directory your server is running. The data has been automatically loaded and you can start querying. Keep in mind that if you accidentally queried using the `DELETE` method, you will need to query using the `POST` method first in order to re-load the dataset into the database. Otherwise, when data has not been loaded/ has been deleted, you will receive an error message. For example:
```console
username:~/COE332/homework06$ curl localhost:5000/genes
No data in db
```

The `/data` route has 3 methods: `GET`, `POST`, and `DELETE`. The first time you are running the services you will need to use the `POST` method to load data into the database. 

#### 1. Route `/data` with `POST` method
Execute the command `curl localhost:5000/data -X POST` on your terminal. This may take a while, data has been successfully loaded into db when you see the message:
```console
username: :~/COE332/homework06$ curl localhost:5000/data -X POST
Data loaded
```

#### 2. Route `/data` with `GET` method
If you want the App to return all the available data in the database, execute `curl localhost:5000/data`. Your output will be similar to below:
```console
username: :~/COE332/homework06$ curl localhost:5000/data
[
  ...,
  {
    "_version_": 1761599366515130368,
    "agr": "HGNC:2769",
    "alias_symbol": [
      "DRP",
      "DRP1",
      "SMAP-3"
    ],
    "ccds_id": [
      "CCDS45003"
    ],
    "date_approved_reserved": "1999-06-17",
    "date_modified": "2023-01-20",
    "date_name_changed": "2016-07-04",
    "ena": [
      "AF038554"
    ],
    "ensembl_gene_id": "ENSG00000139726",
    "entrez_id": "8562",
    "hgnc_id": "HGNC:2769",
    "location": "12q24.31",
    "location_sortable": "12q24.31",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "mane_select": [
      "ENST00000280557.11",
      "NM_003677.5"
    ],
    "mgd_id": [
      "MGI:1915434"
    ],
    "name": "density regulated re-initiation and release factor",
    "omim_id": [
      "604550"
    ],
    "prev_name": [
      "density-regulated protein"
    ],
    "pubmed_id": [
      9628587,
      16982740,
      20713520,
      27239039
    ],
    "refseq_accession": [
      "NM_003677"
    ],
    "rgd_id": [
      "RGD:1584200"
    ],
    "status": "Approved",
    "symbol": "DENR",
    "ucsc_id": "uc001uda.4",
    "uniprot_ids": [
      "O43583"
    ],
    "uuid": "e4eba18a-f927-44a7-83f3-85dd42410234",
    "vega_id": "OTTHUMG00000168844"
  }
]
```
#### 3. Route `/data` with `DELETE` method
When you wish to delete existing data in the database, execute `curl localhost:5000/data -X DELETE`

Database is cleared when you see the message:
```console
username:~/COE332/homework06$ curl localhost:5000/data -X DELETE
Data deleted, there are 0 keys in the db
```

#### 4. Route `/genes`
Next, we will query for a list of all the available `hgnc_id` in the data set. Execute the command `curl localhost:5000/genes` on your terminal. You should get output similar to this:

```console
username::~/COE332/homework06$ curl localhost:5000/genes
[ ....,
  "HGNC:31407",
  "HGNC:1434",
  "HGNC:23105",
  "HGNC:28587",
  "HGNC:35487",
  "HGNC:55215",
  "HGNC:149",
  "HGNC:26445",
  "HGNC:13012",
  "HGNC:25762"
]
```

#### 3. Route `/genes/<hgnc_id>`
We can query for the gene data of a specific `hgnc_id` in the dataset. To do this, execute the command `curl localhost:5000/genes/<hgnc_id>` on your terminal, but replace `<hgnc_id>` with a particular id you are interested in.

For example, `curl localhost:5000/genes/HGNC:33843` results in output below:

```console
username:~/COE332/homework06$ curl localhost:5000/genes/HGNC:33843
{
  "_version_": 1761599382604480512,
  "agr": "HGNC:33843",
  "alias_symbol": [
    "MGC61598"
  ],
  "ccds_id": [
    "CCDS35188"
  ],
  "date_approved_reserved": "2008-10-15",
  "date_modified": "2023-01-20",
  "date_name_changed": "2017-05-12",
  "ensembl_gene_id": "ENSG00000198435",
  "entrez_id": "441478",
  "gene_group": [
    "Ankyrin repeat domain containing"
  ],
  "gene_group_id": [
    403
  ],
  "hgnc_id": "HGNC:33843",
  "location": "9q34.3",
  "location_sortable": "09q34.3",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000356628.4",
    "NM_001004354.3"
  ],
  "mgd_id": [
    "MGI:1914372"
  ],
  "name": "NOTCH regulated ankyrin repeat protein",
  "omim_id": [
    "619987"
  ],
  "pubmed_id": [
    11485984,
    21998026
  ],
  "refseq_accession": [
    "NM_001004354"
  ],
  "rgd_id": [
    "RGD:1591939"
  ],
  "status": "Approved",
  "symbol": "NRARP",
  "ucsc_id": "uc004cmo.3",
  "uniprot_ids": [
    "Q7Z6K4"
  ],
  "uuid": "b2384d06-afcc-482a-aafd-cbfb6b11e357",
  "vega_id": "OTTHUMG00000156150"
}
```

However, if you request an invalid id, for example `:~/COE332/homework06$ curl localhost:5000/genes/abc`, you will get:
```console
username:~/COE332/homework06$ curl localhost:5000/genes/abc
hgnc_id requested is invalid.
```

## Additional Resources

* [HGNC complete set archive](https://www.genenames.org/download/archive/)

## Authors

Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
