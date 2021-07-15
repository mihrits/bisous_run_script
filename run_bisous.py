#!/usr/bin/env python3

# Moorits Mihkel Muru, 2022 UT Tartu Observatory

from bisous_slurm_job_submitter import submit_multiple_runs

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

if __name__ == "__main__":
    submit_multiple_runs(80, "sigma5_spec10_12jul21", "bisous_ultimate_config_zdisp_sigma5_spec10percent_12jul21.ini", "5f10_", "zdisp_inputs_sigma5_spec10percent/input_gal_random_zdisp_sigma5_specobj10percent_run") 
    submit_multiple_runs(80, "sigma5_spec20_12jul21", "bisous_ultimate_config_zdisp_sigma5_spec20percent_12jul21.ini", "5f20_", "zdisp_inputs_sigma5_spec20percent/input_gal_random_zdisp_sigma5_specobj20percent_run") 
    submit_multiple_runs(80, "sigma5_spec30_12jul21", "bisous_ultimate_config_zdisp_sigma5_spec30percent_12jul21.ini", "5f30_", "zdisp_inputs_sigma5_spec30percent/input_gal_random_zdisp_sigma5_specobj30percent_run") 
    submit_multiple_runs(80, "sigma5_spec40_12jul21", "bisous_ultimate_config_zdisp_sigma5_spec40percent_12jul21.ini", "5f40_", "zdisp_inputs_sigma5_spec40percent/input_gal_random_zdisp_sigma5_specobj40percent_run") 
    submit_multiple_runs(80, "sigma5_spec50_12jul21", "bisous_ultimate_config_zdisp_sigma5_spec50percent_12jul21.ini", "5f50_", "zdisp_inputs_sigma5_spec50percent/input_gal_random_zdisp_sigma5_specobj50percent_run") 
#    submit_multiple_runs(80,"sigma5_14may21","bisous_ultimate_config_zdisp_sigma5_14may21.ini", "s5_", "zdisp_inputs_sigma5/input_gal_random_zdisp_sigma5_run")
#    submit_multiple_runs(80,"sigma7_14may21","bisous_ultimate_config_zdisp_sigma7_14may21.ini", "s7_", "zdisp_inputs_sigma7/input_gal_random_zdisp_sigma7_run")
#    submit_multiple_runs(80,"sigma10_14may21","bisous_ultimate_config_zdisp_sigma10_14may21.ini", "s10_", "zdisp_inputs_sigma10/input_gal_random_zdisp_sigma10_run")
#    submit_multiple_runs(80,"sigma2_31mar21","bisous_ultimate_config_zdisp_sigma2_31mar21.ini", "s2_", "zdisp_inputs_sigma2/input_gal_random_zdisp_sigma2_run")
#    submit_multiple_runs(80,"sigma3_31mar21","bisous_ultimate_config_zdisp_sigma3_31mar21.ini", "s3_", "zdisp_inputs_sigma3/input_gal_random_zdisp_sigma3_run")
#    submit_multiple_runs(80, "sigma0_25mar21", "bisous_ultimate_config_zdisp_sigma0_25mar21.ini", "s0_")
#    submit_multiple_runs(80,"sigma1_04mar21","bisous_ultimate_config_zdisp_sigma1_03mar21.ini",    "s1_", "zdisp_inputs_sigma1/input_gal_random_zdisp_sigma1_run")
#    submit_multiple_runs(2, "test", "bisous_ultimate_config_zdisp_sigma1_03mar21.ini", "s1_", "zdisp_inputs_sigma1/input_gal_random_zdisp_sigma1_run")
