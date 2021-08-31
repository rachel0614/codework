# compare detection result to ground truth
base_path = "D:/LYIT/repository/runs/detection/"

gen_correct <- function(expIndex, seprator, ground_true_file){
  # ground truth
  ground_truth_file <- paste(base_path,ground_true_file,sep='') #paste(base_path,"exp", expIndex, "_ground_truth.txt", sep="")
  df0 <- read.csv(ground_truth_file, na = "", sep=seprator, stringsAsFactors = FALSE, header=T)
  # recognition result
  file1 <- paste(base_path,"exp", expIndex, "_result.txt", sep="")
  df1 <- read.csv(file1, na = "", sep=",", stringsAsFactors = FALSE, header=T)
  ground_truth_file
  #file1
  # merge by image name
  df <- merge(x = df0, y = df1, 
              by.x = "ImageId", 
              by.y = "name",
              all = TRUE)
  print(paste0(nrow(df0),' rows of ground truth'))
  print(paste0(nrow(df1[df1$overlap == TRUE, ]),' out of ',nrow(df1), ' overlapped result'))
  #str(df0)
  df <- subset(df, select=c(ImageId,result,Read,overlap))
  dfNew <- df[df$Read==df$result , 
              c("Read", "result", "ImageId","overlap") ]
  # join ground true to detection result and save to compare.txt
  output_file = paste(base_path,expIndex,"_compare.txt",sep='')
  #output_file
  write.csv(dfNew, 
            fileEncoding="UTF-8", 
            file = output_file)
  
  df <- read.csv(output_file, na = "", sep=",", stringsAsFactors = FALSE, header=T)
  
  dfResult <- df[df$ImageId!='NA', ]
  # save true result to true_result.txt
  print(paste0(nrow(dfResult),' correct result of which ', nrow(dfResult[dfResult$overlap==TRUE,]), 'overlapped'))
  write.csv(dfResult, fileEncoding="UTF-8", 
            file = paste(base_path,"exp",expIndex,"_true_result.txt",sep=""))
}
###############################################################
gen_correct("1073",";",'ground_truth_100_full.txt')
gen_correct("1074",";",'ground_truth_100_full.txt')
gen_correct("1075",";",'ground_truth_100_full.txt')
gen_correct("1076",";",'ground_truth_153_146.txt')
gen_correct("1077",";",'ground_truth_153_146.txt')

gen_correct("1079",";",'ground_truth_632.txt')
gen_correct("1080",";",'ground_truth_632.txt')
gen_correct("1081",";",'ground_truth_632.txt')
gen_correct("1082",";",'ground_truth_632.txt')

gen_correct("1083",";",'ground_truth_100_full.txt')
gen_correct("1084",";",'ground_truth_100_full.txt')
gen_correct("1085",";",'ground_truth_100_full.txt')
gen_correct("1086",";",'ground_truth_100_full.txt')
gen_correct("1090",";",'ground_truth_632.txt')

gen_correct("1087",";",'ground_truth_153_146.txt')
gen_correct("1088",";",'ground_truth_632.txt')
gen_correct("1089",";",'ground_truth_632.txt')

###############################################################




# gen_correct("1003",";",'ground_truth_153_146.txt') # counter153_146 iou.5 confthres 0.5 imgsz 512

gen_correct("1007",";",'ground_truth_153_146.txt') # counter153_146 iou.7 confthres 0.5 imgsz 512
gen_correct("1008",";",'ground_truth_153_146.txt') # counter153_146 iou.5 confthres 0.5 imgsz 512
gen_correct("1009",";",'ground_truth_153_146.txt') # counter153_146 iou.3 confthres 0.5 imgsz 512
gen_correct("1011",";",'ground_truth_72.txt') # counter153_146 iou.3 confthres 0.5 imgsz 512


#gen_correct("976",";",'ground_truth_72.txt') # counter72 iou.5 confthres 0.55
#gen_correct("985",";",'ground_truth_25.txt') # counter153_146 iou.5 confthres 0.5 imgsz 512
gen_correct("936",";",'ground_truth_140.txt') # counter153_146 iou.5 confthres 0.5 imgsz 512


# generate true result for the two experiments
#gen_correct("1","\t")
# gen_correct("2",";",'ground_truth_100_full.txt')
# gen_correct("3",";",'ground_truth_100_full.txt')
# gen_correct("4",";",'ground_truth_100_full.txt')
# gen_correct("5",";",'ground_truth_100_full.txt')
# gen_correct("6",";",'ground_truth_100_full.txt')
# 
# gen_correct("8",";",'ground_truth_100_full.txt')
# gen_correct("9",";",'ground_truth_100_full.txt')
# gen_correct("10",";",'ground_truth_100_full.txt')
# 
# gen_correct("11",";",'ground_truth_100_full.txt')
# 
# gen_correct("95",";",'ground_truth_100_full.txt')
# gen_correct("9515",";",'ground_truth_100_full.txt')
# gen_correct("9521",";",'ground_truth_100_full.txt')
# gen_correct("92",";",'ground_truth_100_full.txt')
# gen_correct("90",";",'ground_truth_100_full.txt')
# gen_correct("94",";",'ground_truth_100_full.txt')

gen_correct("927",";",'ground_truth_632.txt')
gen_correct("94",";",'ground_truth_100_full.txt')
gen_correct("92",";",'ground_truth_100_full.txt') # best 75 full recognition 0.5 0.5 conf

gen_correct("921",";",'ground_truth_100_full.txt') # best 75 full recognition 0.5 0.5 conf
gen_correct("922",";",'ground_truth_100_full.txt') # best 75 full recognition 0.5 0.5 conf
gen_correct("923",";",'ground_truth_100_full.txt') # best 75 full recognition conf-thres=0.55 iou-thres=0.5 conf
#NMS后有提高 nms.offset0.5
gen_correct("924",";",'ground_truth_100_full.txt') # best 75 full recognition conf-thres=0.55 iou-thres=0.5 conf
gen_correct("929",";",'ground_truth_632.txt') #  conf-thres=0.6 iou-thres=0.5 conf
gen_correct("931",";",'ground_truth_632.txt') #  conf-thres=0.7 iou-thres=0.5 conf

gen_correct("933",";",'ground_truth_632.txt') #  conf-thres=0.55 iou-thres=0.5 conf
gen_correct("934",";",'ground_truth_632.txt') #  conf-thres=0.6 iou-thres=0.55 conf

gen_correct("935",";",'ground_truth_150.txt') # counter159(150 images) iou.55 confthres 0.6

gen_correct("936",";",'ground_truth_140.txt') # counter159(150 images) iou.55 confthres 0.6

gen_correct("937",";",'ground_truth_140.txt') # counter159(150 images) iou.5 confthres 0.6
gen_correct("942",";",'ground_truth_38.txt') # counter159(150 images) iou.5 confthres 0.6

gen_correct("943",";",'ground_truth_38.txt') # counter159(150 images) iou.5 confthres 0.5
gen_correct("944",";",'ground_truth_38.txt') # counter159(150 images) iou.5 confthres 0.55

gen_correct("945",";",'ground_truth_38.txt') # counter38_unskewed iou.5 confthres 0.55
gen_correct("947",";",'ground_truth_38.txt') # counter38 iou.5 confthres 0.55

gen_correct("948",";",'ground_truth_38.txt') # counter38 iou.5 confthres 0.55

gen_correct("98",";",'ground_truth_25.txt') # counter25 iou.5 confthres 0.5
gen_correct("985",";",'ground_truth_25.txt') # counter25 iou.5 confthres 0.5

gen_correct("987",";",'ground_truth_153_146.txt') # counter153_146 iou.5 confthres 0.5 imgsz 512

gen_correct("1013",";",'ground_truth_153_146.txt') 
gen_correct("1014",";",'ground_truth_153_146.txt') 
gen_correct("1015",";",'ground_truth_632.txt') 
gen_correct("1016",";",'ground_truth_632.txt') 
gen_correct("1017",";",'ground_truth_632.txt') 
gen_correct("1018",";",'ground_truth_632.txt') 
gen_correct("1019",";",'ground_truth_632.txt') 
gen_correct("1059",";",'ground_truth_632.txt') 

gen_correct("1064",";",'ground_truth_140.txt') 
gen_correct("1019",";",'ground_truth_140.txt') 
gen_correct("1061",";",'ground_truth_20.txt') 
gen_correct("1059",";",'ground_truth_153_146.txt') 


get_correct <- function(expIndex){
  ground_truth_file <- paste(base_path,"exp", expIndex, "_ground_truth.txt", sep="")
  df0 <- read.csv(ground_truth_file, na = "", sep="\t", stringsAsFactors = FALSE, header=T)
  df0 = subset(df0,select=c('ImageId','Read'))
  #df0 <- df0[df0$Read!=0, ]
  # total valid rows
  #nrow(df0)
  
  result_file <- paste(base_path,"exp", expIndex, "_result.txt", sep="")
  result_file
  df1 <- read.csv(result_file, na = "", sep="\t", stringsAsFactors = FALSE, header=T)
  df1 = subset(df1,select=c('name','result'))
  
  dfMerge <- merge(df0,df1,by.x = 'ImageId', by.y = 'name')
  #df_correct <- dfMerge[dfMerge$result==dfMerge$Read, ]
  return(dfMerge)
}
# experiment1 has 17 correct result
df_merge <- get_correct(1)
str(df_merge)
str(dfMerge[dfMerge$result==dfMerge$Read, ])
df_merge[length(str(df_merge$Read))>5, ]
df_merge$len <- nchar(as.character(df_merge$result))
df_merge

#load image
name <- '00450000203199_0'
label_file <- paste(base_path, 'exp4_digit/', name, '.txt', sep='')
label_file
img_file <- paste(base_path, 'dataset1/',name, '.jpg', sep='')
img_file

library(imager)
im <- load.image(img_file)
a <- rect(im, 0.57363, 0.469231, 0.181507, 0.846154, 
          color = "red", opacity = 1, filled = TRUE)
plot(a)
