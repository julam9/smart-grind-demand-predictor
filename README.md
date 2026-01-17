smart-grind-demand-predictor
==============================

Project to predict energy consumption in certain area

Project Organization
--------------------

├── LICENSE
├── README.md
├── Makefile                 <- Common project commands (train, test, ingest, serve)
├── pyproject.toml           <- Poetry dependency & project config
├── poetry.lock              <- Locked dependencies for reproducibility
│
├── data/                    <- Data artifacts (never imported as code)
│   ├── raw/                 <- Original, immutable data
│   ├── processed/           <- Cleaned / validated data
│   ├── features/            <- Feature-ready datasets
│   └── checkpoints/         <- Ingestion & training checkpoints
│
├── notebooks/               <- EDA & experiments (non-production)
│
├── models/                  <- Stored trained models & predictions
│
├── src/
│   └── smart_predictor/     <- Main Python package
│       ├── data/            <- Data ingestion & validation logic
│       ├── features/        <- Feature engineering logic
│       ├── models/          <- Training & evaluation code
│       ├── inference/       <- Prediction & serving logic
│       ├── monitoring/      <- Drift & performance monitoring
│       └── pipelines/       <- End-to-end training & retraining workflows
│
├── tests/                   <- Unit & integration tests
└── docs/ (optional)         <- Sphinx documentation


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
