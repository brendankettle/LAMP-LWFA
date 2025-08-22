# LAMP-LWFA

## Template Guidance
This is a template for new LAMP based LWFA experiments. It should be used to set up a new experiment repository.
You will have to edit global.toml at least to suit the specific experiment. I.e. choosing the correct DAQ.
From there you can edit the diagnostics.toml list, and then the various calibrations for the diagnostics.

## LAMP Guidance
Please see the full LAMP documentation at [https://github.com/brendankettle/LAMP/blob/main/docs/](https://github.com/brendankettle/LAMP/blob/main/docs/).
Once cloned, rename _local.toml to local.toml, and edits its contents to fit your local setup for experiment analysis (i.e. define your local data path).
This currently assumes there is a local copy of LAMP in the root directory (i.e. ./LAMP/). Most likely via a git hub repo. This folder has been added to .gitignore. Alternatively you could have LAMP installed as a package... but I haven't went down that route YET as it is still under heavy development.
