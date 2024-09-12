# LAMP-LWFA
Template for new LAMP based LWFA experiment.

Once cloned, rename _local.toml to local.toml, and edits its contents to fit the experiment.

You will also have to edit global.toml to suit the specific experiment. At least choose the correct DAQ.

Currently assumes there is a local copy of LAMP in the root directory (i.e. ./LAMP/). Most likely via a git hub repo. This folder has been added to .gitignore. Alternatively you could have LAMP installed as a package... but I haven't went down that route YET as it is still under heavy development.
