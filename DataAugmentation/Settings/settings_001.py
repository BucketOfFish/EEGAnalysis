original_filename = "../../Data/ECoG/Original/EC2_blocks_1_8_9_15_76_89_105_CV_HG_align_window_-0.5_to_0.79_file_nobaseline.h5"
new_filename = "../../Data/ECoG/001.h5"
overwrite = True # whether it's ok to overwrite an existing output file

n_isolated_samples = 5 # samples to keep separate and not use in augmentation (will later be used as test samples)
total_samples_per_class = 3000 # total number of samples we want to end up with for each CV pair

do_interpolation = True
do_gaussian_noise = True
gaussian_noise_sigma = 0.5
do_time_shift = True
max_steps_timeshift = 10
do_amplitude_scale = True
min_amplitude_scale = 0.5
max_amplitude_scale = 2

offset_scalar = 3
offset_multiplicative = 1

use_best_channels = True
best_channels = [34, 27, 37, 36, 25, 38, 42, 33, 24, 23] # (ordered worst to best, but doesn't matter)

trim = True
flatten_1D = False
downsample_factor = 2
