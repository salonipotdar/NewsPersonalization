num_cluster=5
python do_user_clustering_step1.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.user_fea.user_freq_gt_50 ${num_cluster} ../temp_data/user_ctr_clustering
python do_user_clustering_step2.py ../temp_data/user_ctr_clustering ../temp_data/ydata-fp-td-clicks-v1_0.20090501.user_fea.user_freq_gt_50 ../temp_data/user_ctr_results
sort -k2 -gr ../temp_data/user_ctr_results | awk '{print $2}' | uniq -c
python count_number_of_instance_in_each_cluster.py ../temp_data/user_ctr_results ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid
python ctr_per_cluster.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid ../temp_data/user_ctr_results ../temp_data/user_ctr_ctr 5
