base_path = "D:/LYIT/repository/yolo/detect_digit/testimages/"
count_ground_truth_100 <- function(){
ground_truth_file <- paste(base_path,'ground_truth_100_full.txt',sep='') 
df0 <- read.csv(ground_truth_file, na = "", sep=';', stringsAsFactors = FALSE, header=T,
                colClasses=c('character'),)
str(df0)

library(stringr)
df0[paste0('num',"1")] <- str_count(df0$Read, "1")
df0[paste0('num',"2")] <- str_count(df0$Read, "2")
df0[paste0('num',"3")] <- str_count(df0$Read, "3")
df0[paste0('num',"4")] <- str_count(df0$Read, "4")
df0[paste0('num',"5")] <- str_count(df0$Read, "5")
df0[paste0('num',"6")] <- str_count(df0$Read, "6")
df0[paste0('num',"7")] <- str_count(df0$Read, "7")
df0[paste0('num',"8")] <- str_count(df0$Read, "8")
df0[paste0('num',"9")] <- str_count(df0$Read, "9")
target_file <- paste0(base_path, "ground_truth_100_full_1.txt")
write.csv(df0, fileEncoding="UTF-8", file = target_file)

