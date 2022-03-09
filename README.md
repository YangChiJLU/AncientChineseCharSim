# AncientChineseCharSim
古文字字形相似度计算/Glyph similarity measurement for ancient Chinese characters

More information see this paper: "ZiNet: Linking Chinese Characters Spanning Three Thousand Years"


## Code

Through code in pic_simi; RLCS_simi and graph_simi, you can obtain the character similarity matrix respectively calculated by three methods. The length of row/col is the number of characters. Through mix_simi, you can get combinations of three methods.

## Data

We currently provide 100 samples of oracle glyphs information and images.

**20210520_oracle-radica_sample100.xlsx:** glyph and radical information of Oracle characters (100 samples), as well as the char pairs manually marked for verification.

glyph_id: oc_01_1_0001_1: "oc" indicates oracle bone inscriptions; "01" indicates the volume number (the character in《说文解字》); "1" / "2" indicates deciphered character / undeciphered character; "0001" Oracle character_id; The last "1" represents the first/second/... glyph of the character.

**oracle_images_sample:** Rubbing images of oracle glyphs (100 samples), image name is consistent with the glyph_id

**jia_train.csv:**  image-character parallelism for training PicSim model
