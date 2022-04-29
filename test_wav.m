clc;
clear all;

load B_matrix.mat;
load pi_vector.mat;
load('pcg_0_training_mat7.mat');
% load('pcg_1_training_mat7.mat');
% load('pcg_2_training_mat7.mat');
% load('pcg_3_training_mat7.mat');
% load('pcg_4_training_mat7.mat');
% load('pcg_5_training_mat7.mat');
% load('pcg_6_training_mat7.mat');
wav_cell = num2cell(pcg_0_training.wav_data, 1);
test_recordings = wav_cell([1:409]);
%test_recordings = pcg_1_training.wav_data;
%test_recordings = pcg_2_training.wav_data;
%test_recordings = pcg_3_training.wav_data;
%test_recordings = pcg_4_training.wav_data;
%test_recordings = pcg_5_training.wav_data;
%test_recordings = pcg_6_training.wav_data;
% test_annotations = pcg_a_training.annotations([21:50],:);
size(test_recordings)
%% Run the HMM on an unseen test recording:
% And display the resulting segmentation
numPCGs = length(test_recordings);
saved_states = [];
errors = [];
for PCGi = 1:numPCGs
    try
        [assigned_states] = runSchmidtSegmentationAlgorithm(test_recordings{PCGi}, 2000, B_matrix, pi_vector, true);
        saved_states(PCGi,:) = assigned_states;
    catch
        errors(end+1) = PCGi;
        fprintf('Inconsistent data in iteration %d, skipped.\n', PCGi);
    end
end

save("saved_states_0_training_a.mat", "saved_states");
csvwrite("saved_states_0_training_a.csv", saved_states);
csvwrite("errors0_training_a.csv", errors);
% save("saved_states_1.mat", "saved_states");
% save("saved_states_2.mat", "saved_states");
% save("saved_states_3.mat", "saved_states");
% save("saved_states_4.mat", "saved_states");
% save("saved_states_5.mat", "saved_states");
% save("saved_states_6.mat", "saved_states");
