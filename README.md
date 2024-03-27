
# ecoviztemplate

<!-- badges: start -->
<!-- badges: end -->

This is the use case template for the EcoViz+AI workshop.

## How to use the template

This should be done once by the project lead. After the project lead creates their copy of the repository on GitHub, everyone else in the group will create their own fork.

### Clone locally

To use this template, clone this repo and rename it.

From the directory where you keep git repositories (e.g., ~/Documents/GitHub/), run this command.

`git clone https://github.com/FlukeAndFeather/ecoviztemplate.git [your repo name]` 

Make sure to replace `[your repo name]` with the repo name you've chosen for your use case. Otherwise it'll be called "ecoviztemplate".

### Push to GitHub

Create a remote repository on GitHub with the same name.

Then, back at the command line, change the remote-url to match your new repository (replacing the username and repo name).

`git remote set-url origin https://github.com/[your username]/[your repo name].git`

Then push your local to the remote.

`git push -u origin main`

## What's in the template

The template is organized to accomplish the three goals of a research compendium.

1. Folders and files organized according to conventions
2. Modular organization of data, methods, and outputs
3. Record of the computational environment

This template supports analyses in Python, R, or a combination of the two.

### Folder structure

```
├── data
├── figs
├── notebooks
├── output
├── paper
├── pipeline
└── src
|   ├── Python
|   └── R
└── traintest
    ├── test
    └── train
```

* `data/` - raw data only
* `figs/` - static figures generated during pipeline
* `notebooks/` - literate programming files (e.g., Jupyter, Quarto) explaining the pipeline
* `output/` - derived data generated during pipeline
* `paper/` - the analysis manuscript (preferably in .md format)
* `pipeline/` - pipeline scripts
* `src/` - source files supporting the pipeline (e.g., functions, classes, constants)
* `traintest/` - specifies train/test splits for reproducibility

### Computational environment

```
├── DESCRIPTION
└── requirements.txt
```

These are conventional files used for recording package dependencies. 

`DESCRIPTION` is a file used by R packages to capture package metadata. It is useful for analyses because it records package dependencies following commonly used conventions. Add packages (with version numbers) to the `Imports` field. When other users clone your repo, they can install dependencies by calling `devtools::install_deps()` in R.

`requirements.txt` is a file used to record Python package dependencies. Users can install dependencies by running `pip install -r requirements.txt` at the command line.

### Pipeline components

```
├── data
├── figs
├── output
├── pipeline
│   ├── 00_download_data.R
│   ├── 00_download_data.py
│   ├── _run_pipeline.R
│   └── _run_pipeline.py
└── src
|   ├── Python
|   └── R
└── traintest
    ├── test
    └── train
```

The pipeline folder structure supports modular organization of your code. This modular organization makes it easier to:

* Distribute development among collaborators
* Document pipeline functionality
* Reuse or replace components over time

Here's how the pipeline flows.

1. `pipeline > _run_pipeline.R` or `pipeline > _run_pipeline.py` is a single script that runs the full pipeline.
2. `_run_pipeline.*` calls pipeline scripts in order e.g., `00_download_data.R`, `01_preprocess_data.R`, `02_fit_model.R`, ..., `10_render_notebooks.R`.
3. Pipeline scripts use functions, classes, and constant defined by the modules in `src/Python/` or scripts in `src/R/`.
4. Pipeline scripts generate processed data in `output/` and static visualizations in `figs/`.
5. Train/test splits for AI models use the identifiers in `traintest/train/` and `traintest/test/`.

`00_download_data.R` and `00_download_data.py` are provided as examples. Replace them and add additional pipeline scripts as appropriate.

The last pipeline script should render all literate programming documents (see next section).

### Use case interpretation

```
├── notebooks
└── paper
```

The literate programming documents in `notebooks/` explain the pipeline components. They should render relatively quickly, so keep long-running commands in the pipeline scripts. Keep rendering times short by using the processed data in `outputs/`.

Rendering the documents in `notebooks/` should be automated by the last pipeline script (e.g., `pipeline/10_render_notebooks.R`). For Jupyter notebooks, render them to HTML using `nbconvert`: `jupyter nbconvert --to html notebooks/your_notebook.ipynb`. For Quarto documents, use `quarto render notebooks/your_notebook.qmd --to html`.

`paper/` contains a manuscript describing your use case. It should preferably be in Markdown or a literate programming script.
