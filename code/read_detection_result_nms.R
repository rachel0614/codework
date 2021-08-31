require(dplyr)    
library(stringr)
library(tidyverse)
library('stringr')
library("geosphere")
library(IRanges)
library(dplyr)
# Counter924使用NMS后记录急剧减少，不使用时82 out of 90正确
# load label files from specific folder
# sort numbers by x value, combine a new result
# save all recognition of each image files into result.csv
# digit recognition result
base_path = "D:/LYIT/repository/runs/detection/"
#base_path = "D:/LYIT/repository/runs/nms/"

# generate recognition result from labels
gen_detection_result <- function(digit_folder,expIndex) {
  label_files_folder = paste(base_path,digit_folder,'/labels/', sep='')
  output_file = paste(base_path,'exp',expIndex,'_result.txt',sep='')
  
  filenames <- list.files(label_files_folder,
                          pattern="*.txt", full.names=TRUE)
  dfResult <- data.frame("file"= character(0), "name"=character(0), "result"=character(0), stringsAsFactors=FALSE)
  #detection result
  for(f in filenames){
    dfCurrent <- read.csv(f, na = "", sep=" ", stringsAsFactors = FALSE, header=F)
    colnames(dfCurrent) <- c('value', 'x','y','w','h','conf')
    dfSorted <- dfCurrent[order(dfCurrent$x), ]
    # 不用NMS
    #ret = list(result = str_c(dfSorted$value, collapse = ""), overlap=FALSE)
    ret <- checkNMS(dfSorted)
    #dfSorted <- ret$result
    row <- data.frame(file = f, 
                      name = tools::file_path_sans_ext(basename(f)), 
                      result = ret$result, #str_c(dfSorted$value, collapse = "")
                      overlap = ret$overlap) # one recognition result
    dfResult <- rbind(dfResult, row)
    #overlaptag    
  }
  write.csv(dfResult, fileEncoding="UTF-8", file = output_file)
}
require(data.table)
library(dplyr)
# check the distance of each category with previous element which lower than the width of the ele

check <- function(df, index){
  # print(paste0('currentIndex=',index))
  df_cand <- df[c(index, index-1),]
  # print(df_cand)
  df1 <- df_cand[df_cand$conf==min(df_cand$conf), ]
  ret <- as.integer(rownames(df1))
  # find elements might overlap with the previous neighbour
  #df_result <- df[!rownames(df) %in% c(index),]
  # print(paste0("return ",ret))
  return(ret)
}

checkNMS <- function(df1){
  # print("original")
  # print(df1)
  DT <- data.table(df1)
  DT[, vx := c(10,diff(x))]
  # DT[, vy := c(10,diff(y))]
  DT[, previous_w := ifelse(is.na(shift(w)), 10, shift(w))]
  df <- data.frame(DT)
  print("calculate")
  print(df)
  df1 <- df[df$vx<df$previous_w*0.5,]  #overlap 20%
  print("candidates")
  print(df1)
  exclude_index <- numeric(0)
  for (value in rownames(df1)) {
    exclude <- check(df,as.integer(value))
    exclude_index <- append(exclude_index,exclude)
  }
  print(paste0('exclude',exclude_index))
  if(length(exclude_index)>0){
    df_result <- df[-exclude_index,]
  }else{
    df_result <- df
  }
  result <- str_c(df_result$value, collapse = "")
  print(result)
  overlap <- FALSE
  if(length(exclude_index)>0){
    overlap <- TRUE
  }
  ret <- list("result" = result, "overlap" = overlap)
  print(paste0(result,overlap))
  return(ret)
}
##########################recognition##########################
gen_detection_result("exp1073",1073) # python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/100_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.2 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1074",1074) # runs/digit/models/best95.pt  --source runs/100_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.1 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1075",1075) # python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/100_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.1 --conf-thres 0.5 --save-conf --line-thickness 1

#python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/153_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.1 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1076",1076)
#python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/153_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.1 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1077",1077)
# python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/640_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.1 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1079",1079)
#python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/640_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.3 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1080",1080)
#python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/640_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1081",1081)
#  python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/640_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1082",1082)

# python yolov5/detect.py --weights runs/digit/models/best88.pt  --source runs/100_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1083",1083)
# python yolov5/detect.py --weights runs/digit/models/best92.pt  --source runs/100_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1084",1084)
# python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/100_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1085",1085)
# python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/100_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1086",1086)
# python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/153_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1087",1087)
# python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/640_0.65conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1088",1088)
# python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/640_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1089",1089)
#python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/640_0.9conf/crops/ArteMeter --save-txt  --save-crop --project runs/detection --imgsz 256 --iou-thres 0.2 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1090",1090)
###############################################################
gen_detection_result("exp1003",1003) # conf 0.6 iou 0.5
gen_detection_result("exp924",924) # conf 0.6 iou 0.5
gen_detection_result("exp1013",1013) # python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/counter153_146/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.5 --conf-thres 0.7 --save-conf --line-thickness 1
gen_detection_result("exp1014",1014) #  python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/counter153_146/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.5 --conf-thres 0.7 --save-conf --line-thickness 1
gen_detection_result("exp1015",1015) #   python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/counter632/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.5 --conf-thres 0.7 --save-conf --line-thickness 1
gen_detection_result("exp1016",1016) # python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/counter632/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1017",1017) #  python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/counter632/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.5 --conf-thres 0.5 --save-conf --line-thickness 1
gen_detection_result("exp1018",1018) #   python yolov5/detect.py --weights runs/digit/models/best95.pt  --source runs/counter632/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.55 --conf-thres 0.6 --save-conf --line-thickness 1

gen_detection_result("exp1020",1020) # python yolov5/detect.py --weights runs/digit/models/best92.pt  --source runs/counter632/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.45 --conf-thres 0.6 --save-conf --line-thickness 1
gen_detection_result("exp1030",1030) # python yolov5/detect.py --weights runs/digit/models/best98.pt  --source runs/counter140/ --save-txt  --save-crop --project runs/detection --imgsz 512 --iou-thres 0.45 --conf-thres 0.6 --save-conf --line-thickness 1


gen_detection_result("exp1008",1008) #counter153_146 iou0.5 conf0.5 model95
gen_detection_result("exp1008",1009) #counter153_146 iou0.3 conf0.5 model95
gen_detection_result("exp950",1009) #counter153_146 iou0.3 conf0.5 model95

gen_detection_result("exp1010",1011) #counter72 iou0.5 conf0.5 model95

gen_detection_result("exp987",987) #counter153_146 iou0.5 conf0.5 model95


#gen_detection_result("exp976",976) #counter153_146 iou0.4 conf0.5 model95 half
# generate detection result
# gen_detection_result("exp4_digit",1)
# gen_detection_result("exp2_digit",2)
# gen_detection_result("exp5_digit",3)
# gen_detection_result("exp6_digit",4)
# gen_detection_result("exp7_digit",5)
# gen_detection_result("exp8_digit",6) #0.4 conf thres
# gen_detection_result("exp9_digit",7) #0.5 conf thres
# gen_detection_result("exp10_digit",8) #no conf
# gen_detection_result("exp11_digit",9) #more single numbers 2 combination
# gen_detection_result("exp13_digit",10) # conf 0.6
# 
# gen_detection_result("model57_exp14",11) # conf 0.6
# gen_detection_result("model95_exp15_digit",95) # conf 0.6
# 
# gen_detection_result("exp4",9521) # conf 0.9
# 
# gen_detection_result("exp5",92) # conf 0.9
# gen_detection_result("exp6",90) # conf 0.9
# gen_detection_result("exp7",94) # conf 0.9

gen_detection_result("exp95",92) # conf 0.9 iou 0.5
gen_detection_result("exp922",922) # conf 0.9 iou 0.5
gen_detection_result("exp923",923) # conf 0.9 iou 0.5


gen_detection_result("exp925",925) # conf 0.6 iou 0.5
gen_detection_result("exp926",926) # conf 0.6 iou 0.5 on 159counters

gen_detection_result("exp927",927) # conf 0.6 iou 0.5 on 159counters

gen_detection_result("exp928",928) # conf 0.6 iou 0.5 on 159counters

gen_detection_result("exp929",929) # conf 0.6 iou 0.5 on 159counters
gen_detection_result("exp931",931) 
gen_detection_result("exp932",932) 

gen_detection_result("exp933",933) 

gen_detection_result("exp934",934)
gen_detection_result("exp935",935) #counter159(150 images) iou.55 confthres 0.6

gen_detection_result("exp936",936) #counter140(from 159 images) iou.55 confthres 0.6

gen_detection_result("exp937",937) #counter140(from 159 images) iou.5 confthres 0.6
gen_detection_result("exp938",938) #counter38(home) iou.5 confthres 0.6
gen_detection_result("exp940",940) #counter38_1080(home) iou.5 confthres 0.6
gen_detection_result("exp942",942) #counter38_640(home) iou.5 confthres 0.6

gen_detection_result("exp943",943) #counter38_256(home) iou.5 confthres 0.5
gen_detection_result("exp944",944) #counter38_256(home) iou.5 confthres 0.55

gen_detection_result("exp946",946) #counter38_unskewed(home) iou.5 confthres 0.55

gen_detection_result("exp947",947) #counter38 iou.5 confthres 0.55
gen_detection_result("exp948",948) #counter38_1080 iou.5 confthres 0.55
gen_detection_result("exp959",959) #counter86

gen_detection_result("exp976",976) #counter72
gen_detection_result("exp984",984) #counter25 iou0.45 conf0.5

gen_detection_result("exp985",985) #counter25 iou0.45 conf0.5 model95
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
gen_detection_result("exp993",993) #counter153_146 iou0.5 conf0.5 model95

gen_detection_result("exp994",994) #counter153_146 iou0.5 conf0.7 model95
gen_detection_result("exp995",995) #counter153_146 iou0.3 conf0.7 model95

gen_detection_result("exp1063",1063) #counter153_146 iou0.3 conf0.7 model95

gen_detection_result("exp1028",1028) # final counter 140

gen_detection_result("exp1066",1066) # final counter20

