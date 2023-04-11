# Gene-ius

A containarized Flask application with persisting Redis NoSQL database integration for querying and returning interesting information from HGNC data published by The Human Genome Organization (HUGO). 

The REST API's repository includes Dockerfile for protability, and included Docker Compose to automate deployment. In addition, there are six yaml files to deploy the app on a kubernetes cluster.

## Data Description
The Human Genome Organization (HUGO) is a non-profit which oversees the HUGO Gene Nomenclature Committee (HGNC). The HGNC "approves a unique and meaningful name for every gene".

The complete HGNC dataset file, available in both tab separated and JSON formats, are archived monthly and quarterly. For this project, we are using the "Current JSON format hgnc_complete_set file". It contains a set of all approved gene symbol reports found on the GRCh38 reference and the alternative reference loci.

The data has 54 columns, and some columns are sparsely populated. Below are a brief overview of some fields:
| Field Name              | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| hgnc_id                 | HGNC ID. A unique ID created by the HGNC for every approved symbol. |
| symbol                  | The HGNC approved gene symbol. Equates to the "APPROVED SYMBOL" field within the gene symbol report. |
| name                    | HGNC approved name for the gene. Equates to the "APPROVED NAME" field within the gene symbol report. |
| locus_group             | A group name for a set of related locus types as defined by the HGNC (e.g. non-coding RNA). |
| locus_type              | The locus type as defined by the HGNC (e.g. RNA, transfer). |
| status                  | Status of the symbol report, which can be either "Approved" or "Entry Withdrawn". |
| location                | Cytogenetic location of the gene (e.g. 2q34). |
| location_sortable       | Same as "location" but single digit chromosomes are prefixed with a 0 enabling them to be sorted in correct numerical order (e.g. 02q34). |
| date_approved_reserved  | The date the entry was first approved. |

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

In addition, there are six files for kubernetes deployment:
* `dwi67-deployment-python-debug.yml`
* `dwi67-test-pvc.yml`
* `dwi67-test-flask-deployment.yml`
* `dwi67-test-redis-deployment.yml`
* `dwi67-test-flask-service.yml`
* `dwi67-test-redis-service.yml`

## Installation

You have the option to build this project from source, or use the provided Docker container on DockerHub. A Docker installation is required, as we build and run a Docker image.

We describe below the installation process using terminal commands, which are expected to run on a Ubuntu 20.04.5 machine with Python3. Installation may differ for other systems.

**Source build using docker-compose file provided in this repository is highly recommended as it automates your deployment process to a single step**

<details>
<summary><h3>Source build (option 1)</h3></summary>

Since this is a Docker build, the requirements need not be installed, as it will automatically be done on the Docker image. All commands, unless otherwise noted, are to be run in a terminal (in the `homework06` directory of the cloned repository).

* First, install Docker: `sudo apt-get install docker` or follow installation instructions for [Docker Desktop](https://www.docker.com/get-started/) for your system. We are using **Docker 20.10.12**
* Next, install docker-compose: `sudo apt-get install docker-compose-plugin` or follow the instructions [here](https://docs.docker.com/compose/install/linux/). We are using **Docker Compose 1.25.0**
* Clone the  repository: `git clone https://github.com/dhannywi/COE332.git`
* Then, change directory into the `homework07` folder: `cd ./homework07/`


### **Option 1:** Automate deployment using `docker-compose`
The quickest way to get your services up and running is to use `docker-compose` to automate deployment.
* Create a `data` folder inside the `homework07` directory. Execute `mkdir data`. This allows redis to store data in the disk so that the data persist, even when the services are killed.
* Execute `docker-compose up --build`. Your images are built and services are up and running when you see this message:
```console
username:~/COE332/homework07$ docker-compose up --build
Creating network "homework07_default" with the default driver
Building flask-app
...
...
Successfully built ba82680f899d
Successfully tagged dhannywi/gene-ius:latest
Creating homework07_redis-db_1 ... done
Creating homework07_flask-app_1 ... done
Attaching to homework07_redis-db_1, homework06_flask-app_1
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
username:~/COE332/homework07$ docker ps -a
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS                     PORTS
          NAMES
d1e8117bdd49   dhannywi/gene-ius   "python gene_api.py"     49 minutes ago   Up 49 minutes              0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   homework07_flask-app_1
90f7ace06c22   redis:7             "docker-entrypoint.s…"   49 minutes ago   Up 49 minutes              0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   homework07_redis-db_1
```

### **Option 2:** Build and run your own docker image
* First, create a `data` folder inside the `homework07` directory. Execute `mkdir data`. This allows redis to store data in the disk so that the data persist even when the services are killed.
* Pull docker image for redis, execute `docker pull redis:7`
* Now, build the image: `docker build -t dhannywi/gene-ius .`
This output shows that your build is successful:
```console
username:~/COE332/homework07$ docker build -t dhannywi/gene-ius .
Sending build context to Docker daemon  58.37kB
...
...
Successfully built 54af1d1a71c4
Successfully tagged dhannywi/gene-ius:latest
```

* Check the docker images currently running in your computer by executing: `docker images`. The image you just built would show up in the list of images:
```console
username:~/COE332/homework07$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED             SIZE
dhannywi/gene-ius      latest    ba82680f899d   8 minutes ago       903MB
redis                  7         dd786f66ff99   8 minutes ago       117MB
```

* Execute `docker-compose up` and your services is up and running when you see the message:
```console
username:~/COE332/homework07$ docker-compose up
Creating network "homework07_default" with the default driver
Creating homework07_redis-db_1 ... done
Creating homework07_flask-app_1 ... done
Attaching to homework07_redis-db_1, homework06_flask-app_1
redis-db_1   | 1:C 29 Mar 2023 12:47:46.640 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
...
...
redis-db_1   | 1:M 29 Mar 2023 12:47:46.641 * Ready to accept connections
flask-app_1  |  * Serving Flask app 'gene_api'
flask-app_1  |  * Debug mode: on
...
...
flask-app_1  | Press CTRL+C to quit
flask-app_1  |  * Restarting with stat
flask-app_1  |  * Debugger is active!
flask-app_1  |  * Debugger PIN: 255-629-791
```

##
**Killing the services**

If you madea any changes to the `gene_api.py` file, you will need to kill the existing services that's running and rebuild. Execute `docker-compose down`. The services are removed when you see the following message:
```console
username:~/COE332/homework07$ docker-compose down
Removing homework07_flask-app_1 ... done
Removing homework07_redis-db_1  ... done
Removing network homework07_default
```
</details>

<details>
<summary><h3>From Docker Hub (option 2)</h3></summary>

**Install**

* To install the Docker container, first install Docker: `sudo apt-get install docker` or follow installation instructions for [Docker Desktop](https://www.docker.com/get-started/) for your system. We are using Docker 20.10.12

* Next, pull the images from the docker hub and install the containers: `docker pull dhannywi/gene-ius` and `docker pull redis:7`

* Check the docker images currently running in your computer by executing: `docker images`
The image you just installed would show up in the list of images:
```console
username:~/COE332/homework07$ docker images
REPOSITORY             TAG       IMAGE ID       CREATED             SIZE
dhannywi/gene-ius      latest    ba82680f899d   8 minutes ago       903MB
redis                  7         dd786f66ff99   8 minutes ago       117MB
```

**Run**

* Create a `data` folder inside the directory you are working on. Execute `mkdir data`. This allows redis to store data in the disk so that the data persist, even when the services are killed.
* First run the Redis image and bind mount to the data folder you just created, execute: `docker run -d -p 6379:6379 -v </path/on/host>:/data redis:7 --save 1 1`.
You can use the `$(pwd)` shortcut for the present working directory. For example:
```console
username:~$ docker run -p 6379:6379 -v /home/ubuntu/data:/data redis:7 --save 1 1
1:C 29 Mar 2023 11:58:04.482 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 29 Mar 2023 11:58:04.482 # Redis version=7.0.10, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 29 Mar 2023 11:58:04.482 # Configuration loaded
1:M 29 Mar 2023 11:58:04.482 * monotonic clock: POSIX clock_gettime
1:M 29 Mar 2023 11:58:04.483 * Running mode=standalone, port=6379.
1:M 29 Mar 2023 11:58:04.483 # Server initialized
1:M 29 Mar 2023 11:58:04.483 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
1:M 29 Mar 2023 11:58:04.484 * Ready to accept connections
```
* This will take over your terminal, so open a new terminal to move on to the next step.
* To run the code, execute: `docker run -it --rm -p 5000:5000 dhannywi/gene-ius` 
The terminal should return a link, which can be viewed via a browser or with the curl commands documented in the API reference section. Your local server is up and running when you see this message:
```console
username:~$ docker run -it --rm -p 5000:5000 dhannywi/gene-ius
 * Serving Flask app 'gene_api'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 463-886-503
```
* Check that all the services are running by executing `docker ps -a`
* when you want to kill the services, execute `docker rm -f <container id you want to kill>`
</details>

<br>

## Kubernetes Deployment
To run this app on a Kubernetes cluster, enter the following commands in the console from which you have Kubernetes access:
* `kubectl apply -f dwi67-test-redis-deployment.yml`
* `kubectl apply -f dwi67-test-pvc.yml`
* `kubectl apply -f dwi67-test-flask-deployment.yml`
* `kubectl apply -f dwi67-test-redis-service.yml`
* `kubectl apply -f dwi67-test-flask-service.yml`
* `kubectl apply -f dwi67-test-python-debug.yml`

You will see a confirmation message after running each command. For example:
```console
username:~/COE332/homework07$ kubectl apply -f dwi67-test-flask-deployment.yml
deployment.apps/dwi67-test-flask-deployment configured
```
**NOTE:** if you wish to use your own Flask API in the kubernetes cluster, you must change the image being pulled in `dwi67-test-flask-deployment` to your preferred image on Docker Hub and then re-apply the kubernetes depolyment.


* To check if your pods are running and discover the IP address of your redis pod, execute the command `kubectl get pods -o wide`
```console
username:~/COE332/homework07$ kubectl get pods -o wide
NAME                                           READY   STATUS    RESTARTS        AGE     IP              NODE            NOMINATED NODE   READINESS GATES
dwi67-test-flask-deployment-6b66d4f7fd-9tksm   1/1     Running   0               5m56s   10.233.86.58    kube-worker-2   <none>           <none>
dwi67-test-flask-deployment-6b66d4f7fd-cxthz   1/1     Running   0               6m1s    10.233.116.82   kube-worker-1   <none>           <none>
dwi67-test-redis-deployment-7689988fd-pkk4x    1/1     Running   0               10m     10.233.86.55    kube-worker-2   <none>           <none>
py-debug-deployment-f484b4b99-vj8qx            1/1     Running   0               9m25s   10.233.85.197   kube-worker-2   <none>           <none>
```

* Note the python debug deployment name to access it:
`kubectl exec -it py-debug-deployment-f484b4b99-vj8qx -- /bin/bash`
* It will allow you to use a bash terminal similar to:
`root@py-debug-deployment-f484b4b99-vj8qx:/#`


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
username:$ curl localhost:5000/genes
No data in db
```

The `/data` route has 3 methods: `GET`, `POST`, and `DELETE`. The first time you are running the services you will need to use the `POST` method to load data into the database. 

#### 1. Route `/data` with `POST` method
Execute the command `curl localhost:5000/data -X POST` on your terminal. This may take a while, data has been successfully loaded into db when you see the message:
```console
username:$ curl localhost:5000/data -X POST
Data loaded
```

#### 2. Route `/data` with `GET` method
If you want the App to return all the available data in the database, execute `curl localhost:5000/data`. Your output will be similar to below:
```console
username:$ curl localhost:5000/data
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
username:$ curl localhost:5000/data -X DELETE
Data deleted, there are 0 keys in the db
```

#### 4. Route `/genes`
Next, we will query for a list of all the available `hgnc_id` in the data set. Execute the command `curl localhost:5000/genes` on your terminal. You should get output similar to this:

```console
username:$ curl localhost:5000/genes
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

#### 5. Route `/genes/<hgnc_id>`
We can query for the gene data of a specific `hgnc_id` in the dataset. To do this, execute the command `curl localhost:5000/genes/<hgnc_id>` on your terminal, but replace `<hgnc_id>` with a particular id you are interested in.

For example, `curl localhost:5000/genes/HGNC:33843` results in output below:

```console
username:$ curl localhost:5000/genes/HGNC:33843
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

However, if you request an invalid id, for example `curl localhost:5000/genes/abc`, you will get:
```console
username:$ curl localhost:5000/genes/abc
hgnc_id requested is invalid.
```

## Additional Resources

* [HGNC complete set archive](https://www.genenames.org/download/archive/)

## Authors

Dhanny W Indrakusuma<br>
dhannywi@utexas.edu
