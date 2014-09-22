num_cluster=5
mf_dimension=10
python generate_mf_data.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid ../temp_data/ydata-fp-td-clicks-v1_0.20090501.user_freq 50 ../temp_data/mf_train ../temp_data/mf_uid_map ../temp_data/mf_did_map
cd ../libmf/libmf-1.1/
./libmf convert ../../temp_data/mf_train yh.data.bin
./libmf train --tr-rmse --obj -k ${mf_dimension} -t 1000 -s 1 -p 0.05 -q 0.05 -g 0.003 -ub -1 -ib -1 --no-use-avg --rand-shuffle -v yh.data.bin yh.data.bin model
mv user_latent_fea ../../temp_data/mf_model
cd ../../code
python do_user_clustering_step1.py ../temp_data/mf_model ${num_cluster} ../temp_data/mf_clustering
python do_user_clustering_step2.py ../temp_data/mf_clustering ../temp_data/mf_model ../temp_data/mf_results
sort -k2 -gr ../temp_data/mf_results | awk '{print $2}' | uniq -c
python count_number_of_instance_in_each_cluster.py ../temp_data/mf_results ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid
python ctr_per_cluster.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid ../temp_data/mf_results ../temp_data/mf_ctr 5
