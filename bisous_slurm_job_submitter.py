#!/usr/bin/env python3

# Moorits Mihkel Muru 2021 Tartu Observatory
# Script for bootstrapping sbatch job of bisous ultimates processes with different inputs

# TODO: Generate log file

"""
Usage:
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

Folder structure:
    bisous
    ├── configs
    ├── data
    └── output
"""

import time
import subprocess as sp
import os

def usage():
    print('''
    Usage:
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
        e.g "test_"''')
    return

def create_config_new_input(original_config_file,
                            input_file_base,
                            irun,
                            run_name,
                            line_nr = 28):
    with open(os.path.join("configs", original_config_file), 'r') as file_in:
        config_contents = file_in.readlines()
    
    new_input_file = input_file_base + f'{irun}'.zfill(3) + '.txt'
    bisous_home_dir = os.getcwd()
    new_line = f"file_primary = {bisous_home_dir}/data/{new_input_file}\n"

    config_contents[line_nr-1] = new_line

    config_file = os.path.join("configs", f"configs_{run_name}",
                               original_config_file[:-4] + "_run" + f'{irun}'.zfill(3) + '.ini')

    with open(config_file, 'w') as file_out:
        file_out.writelines(config_contents)
    return os.path.join(bisous_home_dir, config_file)


def sbatchjob_command(output_folder,
                      config_file,
                      slurm_output,
                      slurm_jobname,
                      slurm_memory,
                      slurm_time):
    
    sbatchjob = 'sbatch --dependency=singleton --nodes=1 --ntasks=1 --partition=main'
    sbatchjob += f' --mem={slurm_memory}'
    sbatchjob += f' --time={slurm_time}'
    sbatchjob += f' --output={slurm_output}'
    sbatchjob += f' --job-name={slurm_jobname}'
    sbatchjob += f' bisous_ultimate_run.sh {config_file} {output_folder}'

    # If running test, just print the command to the terminal
    if slurm_jobname.startswith("test"):
        sbatchjob = "echo " + sbatchjob
    
    return sbatchjob


def submit_single_run(irun,
                      run_name,
                      original_config_file,
                      input_file_base,
                      slurm_output,
                      slurm_jobname,
                      slurm_memory,
                      slurm_time):

    output_folder = os.path.join("output", run_name, "run" + f"{irun}".zfill(3))
    if not os.path.exists(output_folder):
        os.mkdir(output_folder) # raises error, if directory already exists

    config_file = os.path.join("configs", original_config_file)
    # If input_file_base is not given, only one input (specified in config file) is used
    if input_file_base:
        config_file = create_config_new_input(original_config_file,
                                              input_file_base,
                                              irun,
                                              run_name)

    sbatchjob = sbatchjob_command(output_folder,
                                  config_file,
                                  slurm_output,
                                  slurm_jobname,
                                  slurm_memory,
                                  slurm_time)
    sp.run(sbatchjob.split())
    # print(f"Submitted bisous ultimate run job {slurm_jobname}.")
    return True


def submit_multiple_runs(maxruns,
                         run_name,
                         original_config_file,
                         slurm_jobname,
                         input_file_base = None,
                         slurm_memory = "2GB",
                         slurm_time = "8-00:00:00"):

    # Check if user is running the script from the correct folder
    if not os.getcwd().split("/")[-1] == "bisous":
        return print("Error: This script should be executed in the main bisous folder. See script header.")

    # If the output folder does exist ask user confirmation for continuation, else create it.
    output_dir = os.path.join("output", run_name)
    if os.path.exists(output_dir):
        cont = input("The output folder already exists. Do you want to continue? (y)/n: ")
        answers = ("y", "yes", "")
        if cont.lower() not in answers:
            return print("Exiting: Output folder already exists. Script halted by user.")
    else:
        os.makedirs(output_dir)

    # Create separate folder for logs in the logs folder.
    logfile_dir = os.path.join(os.getcwd(), "logs", run_name)
    if not os.path.exists(logfile_dir):
        os.mkdir(logfile_dir)
    
    # If the script is going to use multiple input files and
    # the configs folder does not exist, create it
    configs_dir = os.path.join("configs", f"configs_{run_name}")
    if input_file_base and not os.path.exists(configs_dir):
        os.mkdir(configs_dir)

    for irun in range(1,maxruns+1):
        slurm_jobname_current = slurm_jobname + f"{irun}".zfill(3)
        slurm_output = os.path.join(logfile_dir, f"bisous_ultimate_job_{slurm_jobname_current}-%J.txt")

        submit_single_run(irun,
                          run_name,
                          original_config_file,
                          input_file_base,
                          slurm_output,
                          slurm_jobname_current,
                          slurm_memory,
                          slurm_time,)
        time.sleep(0.1)
    print(f"Submitted {maxruns} bisous run jobs each with different input file.")
    return True
