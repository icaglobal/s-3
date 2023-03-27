S3 - Premature Device Failures
==========================

### Description

Problem identified and compared to age of device.

### Our Solution

The tool will capture the age of a device at failure by linking the MDR and GUDID tables via device and subtract the MDR date of event from both the GUDID date of manufacturer and the GUDID date of first use. The tool will then statistically compare device age at failure to typical age at failure across similar devices to discern whether the device failure qualifies as a threshold-identified 'premature failure' to alert to the reviewer.

### Technologies

- ARIMA

    Although it is early to assume the right approach to the problem, ARIMA models seem to generalize well when using dates to forecast events.

- Streamlit

    Python library used to host web applications. Our mockups use this library to give the client a way to interactively analyze the work done and give a feedback if requirements are met.


------------

```


├── data
│   ├── external             <- Data from third party sources.
│   ├── processed            <- The final, canonical data sets for modeling.
│   └── raw                  <- The original, immutable data dump.
│
├── docs                      <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                  <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks                <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                the creator's initials, and a short `-` delimited description, e.g.
│                                `1.0-jqp-initial-data-exploration`.
│
├── references               <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                  
│   └── figures              <- Generated graphics and figures to be used in reporting
│
├── src                      <- Source code for use in this project.
│   ├── __init__.py          <- Makes src a Python module
│   │
│   ├── data                 <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features             <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models               <- Scripts to train models and then use trained models to make
│   │   │                        predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization        <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
|
├── CHANGELOG.md             <- Track project versions
├── CONDUCT.md               <- Guidelines for interaction between developers
├── CONTRIBUTING.md          <- Guidelines for code contribution
├── Dockerfile               <- Empty Dockerfile as placeholder
├── Makefile                 <- Makefile with commands like `make environemnt` or `make requirements`
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
└──                             generated with `pip freeze > requirements.txt`
```

### Version

0.1.0

### Contributors

Jonathan Oak

### Links
- Jira Epic - [Link](https://icaglobal.atlassian.net/jira/software/projects/TS/boards/25?selectedIssue=TS-503)
- Project page on Confluence - [Link](https://icaglobal.atlassian.net/wiki/spaces/MDEAI/pages/22808192/Y1+-+S-3)
- Project documentation page - [Link](https://icaglobal.github.io/s-3/)
- Project documents on Sharepoint - [Link](https://icaglobalco.sharepoint.com/sites/MDEAIProgram/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FMDEAIProgram%2FShared%20Documents%2FBusiness%20Analysis%2FYear%201%2FS%2FS%2D03&viewid=8fde4734%2Dc151%2D4c78%2D83d9%2D1df238e1c082)
- UI Dynamic Mockup - [Link](https://jonathanoakica-s3-ui-mockup-app-wxdxwf.streamlit.app/)





