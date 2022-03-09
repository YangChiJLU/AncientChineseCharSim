CHARACTER_NUM=55  #甲骨文数量（全部：2543，sample：55）
SAMPLE_NUM=100 #(全部：2913)
INFOR_PATH="../data/20210520_oracle-radica_sample100.xlsx"#甲骨文文字、部件、标注信息
#INFOR_PATH='../data/20210520_oracle-radical.xlsx'

IMAGE_PATH='../data/oracle_images_sample/' #用于训练PICSIM的甲骨文图片
PIC_LABEL_PATH='../data/jia_train.csv' #用于训练PICSIM的甲骨文图片和对应文字（label）
PIC_MODEL_PATH='../data/weights/modelresnet18_200_epoch90transdata.bin'#训练好的模型
IMAGE_EMB_PATH='../data/output_epoth90_15174_2543.npy' #image的embedding
GLYPH_EMB_PATH="../data/cfid2vec_epoch90_2895_2543.txt"#glyph的embedding
ALPHA=0.4

THETA=0.7

NET_PATH="../data/radicalcharacterNet.txt"#用于生成embedding
GRAPHSIM_EMB_PATH="../data/character_node2vec.txt" #graphsim的甲骨文embedding文件

W_RLCS_1=0.5
W_GRAPH_1=0.5
W_RLCS_2=0.5
W_PIC_2=0.5
W_RLCS_3=0.4
W_GRAPH_3=0.4
W_PIC_3=0.3

#results
GRAPHSIM_MATRIX_PATH='../data/results/jia_graph_simi_np.npy' #GraphSim甲骨文相似度矩阵
RLCSSIM_MATRIX_PATH='../data/results/jia_RLCS_simi_np.npy' #RLCSSim甲骨文相似度矩阵
PICSIM_MATRIX_PATH='../data/results/jia_pic_simi_np.npy' #PICSim甲骨文相似度矩阵

RLCSSIM_TOP500_PATH='../data/results/jia_RLCSsim_500.xls'#RLCSsim方法甲骨文每个字的top-500推荐
PICSIM_TOP500_PATH='../data/results/jia_picsim_500.xls'
GLYPHSIM_TOP500_PATH='../data/results/jia_Graphsim_500.xls'
RLCSSIM_PICSIM_TOP500_PATH='../data/results/jia_RLCS_picsim_500.xls'
RLCSSIM_GLYPHSIM_TOP500_PATH='../data/results/jia_RLCS_Graphsim_500.xls'
RLCSSIM_PICSIM_GLYPHSIM_TOP500_PATH='../data/results/jia_RLCS_Pic_Graphsim_500.xls'



