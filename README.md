
# Bisous cluster run script

*Moorits Mihkel Muru, 2021 UT Tartu Observatory*

A script to submit slurm jobs to cluster to run Bisous model.
Requires Python 3, `bisous_ultimate` binary, bash script `run_bisous.sh`, and specific folder structure.

```
Folder structure:
    bisous
    ├── configs
    ├── data
    └── output
```

User has to specify the number of runs, output folder name, config file name, slurm job name.
In addition, user can provide specific slurm memory and time limits.
If the script is used to submit Bisous jobs each with a different input file, then the input file base name has to be provided.
The script is creates folders for output, and logs, but prompts when the output folder already exists to avoid accidental overwriting.
If different input files are used, the script also creates speparate folders for generated config files.
## Usage/Examples

```
submit_multiple_run(maxruns,
                    run_name,
                    original_config_file,
                    slurm_jobname,
                    input_file_base = None,
                    slurm_memory = "2GB",
                    slurm_time = "8-00:00:00")

maxruns - number of last run (starts from 1)
run_name - name used for output and configs folder
    e.g "testrun"
original_config_file - name of base config file in configs folder
    e.g "bisous_ultimate_testrun_config.ini"
input_file_base - name of input file without the number (001) and file extension in data folder,
                  if left empty, script will use only one original config file
    e.g "testinputs/test_input_"
slurm_jobname - name of the slurm jobs (max length 5 chars)
    e.g "test_"
```
If the job name starts with "test" the script prints the sbatch commands instead of acctually submitting them.

For example:

```python
from slurm_bisous_run import submit_multiple_runs

submit_multiple_runs(2,
                     "test",
                     "bisous_ultimate_config_zdisp_sigma1_03mar21.ini",
                     "s1_",
                     "zdisp_inputs_sigma1/input_gal_random_zdisp_sigma1_run")
```

  