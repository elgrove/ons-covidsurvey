# ONS Covid Survey Website

A Flask app that processes data from the weekly UK ONS coronavirus infection survey and plots the headline prevalence in a chart, deployed using Docker and Nginx on a Linode server at [covid.elgrove.xyz](https://covid.elgrove.xyz).

## Description

The Office for National Statistics COVID-19 Infection Survey is the largest regular survey of SARS-CoV-2 infections, taking samples from 300,000 people at random and modelling using Bayesian techniques.

These are, along with REACT by Imperial and the ZOE study by King's College London, the best numbers for understanding SARS-CoV-2 prevalence in the UK community.

The headline daily testing numbers rely on self-selection for testing, or mandatory testing programmes in schools and other instituions and can fluctuate with days of the week among other seasonal noise.

I had been wanting to make this for most of the pandemic but had other projects to focus on, in the end I got a push and made it in about 6 hours, most of which on flights between London and Vienna.

## Getting Started

### Dependencies

* Flask web framework, Jinja2 templates
* Plotly.py and Plotly.js for visualisation
* APScheduler for task scheduling
* pandas and NumPy
* Docker for deployment


### Executing program

* Clone this repository
* Install requirements.txt
* Run `gunicorn app:app' to run on localhost port 5000
* Dockerfile included for use with a linuxserver.io SWAG container for example

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
