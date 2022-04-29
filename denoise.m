%path = "/common/VIT/sem6/data_viz_theory/data_viz_project/2016_dataset/training/training_combined"
path = "/common/VIT/sem6/data_viz_theory/data_viz_project/2016_dataset/training/remaining_wav/"
files = dir(path)
for file = files'
  search = strfind(file.name, "wav")
  if(length(search) > 0)
    new_name = strcat("denoised_", file.name)
    [audio, sample_rate] = audioread(strcat(path, file.name))
    result = schmidt_spike_removal(audio, sample_rate)
    audiowrite(new_name, result, 2000)
  endif
end