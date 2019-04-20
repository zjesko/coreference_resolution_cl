# Coreference Resolution (In Hindi)

Coreference resolution is the task of linking different mentions
of same entity in text. Here we explore rule based and
statistical methods for coreference resolution in Hindi.

## Getting Started

### Prerequisites

You need to have python 2.7 installed on your system.

### Installing

- Run `git clone https://github.com/akshatcx/coreference_resolution_cl` to clone this repository.
- Run `cd coreference_resolution_cl` to enter the project directory
- Run `virtualenv -p python=/usr/bin/python2.7 env` to create a virtual environment for the project.
- Run `source env/bin/activate` to activate the environment
- Run `pip install -r requirements.txt` to install all the dependencies.

## Running the tests

- Run `python coref.py` to generate the coreference output


### Output

We will be getting our data as the output with its respective analysis. It shows the individual pronouns and the word their possible referents.


## Authors

* **Akshat Gahoi** - IIIT Hyderabad
* **Akshat Chhajer** - IIIT Hyderabad


## Acknowledgments

* Thanks to Dr. Dipti Misra Sharma (LTRC IIIT Hyderabad)
* Mentored by Anirudh Dahiya (LTRC IIIT Hyderabad)
* Inspired from paper "A Hybrid Approach for Anaphora Resolution in Hindi"(https://www.aclweb.org/anthology/I13-1130)

