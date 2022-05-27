
<p align="center">

  <h1 align="center">Order! Order!: A Comparison of Topic Models based on Plenary Sessions of the Bundestag</h1>

  <p align="center">
    Angular based web app that presents public transport analysis results 
  </p>
</p>

## About The Project

This repository contains all necessary files to reproduce the results presented in the thesis "Order! Order!: A Comparison of Topic Models based on Plenary Sessions of the Bundestag"

The folder 'corpus' contains raw, prepared and pre-processed data needed to train the models

The folder 'pre-processing' contains the notebooks to complete all necessary pre-processing steps

The folder 'models' contains the notebooks related to modeling, analysis, and evaluation as well as the models and model outputs


## Installation

Install all packages by running

```
pip install -r requirements.txt
```

Download dataset from Harvard Dataverse by running

```
python download-corpus.py
```