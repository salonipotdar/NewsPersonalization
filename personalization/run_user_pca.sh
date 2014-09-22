num_cluster=5
pca_comp=6
python do_user_clustering_step0.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.user_cluster_using_ctr_as_fea ${pca_comp} ../temp_data/pca_tr_output
python do_user_clustering_step1.py ../temp_data/pca_tr_output ${num_cluster} ../temp_data/user_pca_clustering
python do_user_clustering_step2.py ../temp_data/user_pca_clustering ../temp_data/pca_tr_output ../temp_data/user_pca_results
sort -k2 -gr ../temp_data/user_pca_results | awk '{print $2}' | uniq -c
python count_number_of_instance_in_each_cluster.py ../temp_data/user_pca_results ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid
python ctr_per_cluster.py ../temp_data/ydata-fp-td-clicks-v1_0.20090501.with_uid ../temp_data/user_pca_results ../temp_data/user_pca_ctr 5
