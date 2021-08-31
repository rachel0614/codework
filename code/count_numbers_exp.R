base_path = "D:/LYIT/repository/yolo/detect_digit/testimages/"
filename <- paste(base_path,'exp3_result.txt',sep='') 
separator <- ";"
separator <- ","

df0 <- read.csv(filename, na = "", sep=separator, stringsAsFactors = FALSE, header=T,
                colClasses=c('character'),)
str(df0)

library(stringr)
df0[paste0('num',"1")] <- str_count(df0$result, "1")
df0[paste0('num',"2")] <- str_count(df0$result, "2")
df0[paste0('num',"3")] <- str_count(df0$result, "3")
df0[paste0('num',"4")] <- str_count(df0$result, "4")
df0[paste0('num',"5")] <- str_count(df0$result, "5")
df0[paste0('num',"6")] <- str_count(df0$result, "6")
df0[paste0('num',"7")] <- str_count(df0$result, "7")
df0[paste0('num',"8")] <- str_count(df0$result, "8")
df0[paste0('num',"9")] <- str_count(df0$result, "9")
df0 <- subset(df0, select=-c(file))
str(df0)
target_file <- paste0(base_path, "exp3.txt")
write.csv(df0, fileEncoding="UTF-8", file = target_file)


filename <- paste(base_path,'ground_truth_100_full_1.txt',sep='') 
#separator <- ";"
separator <- ","
df1 <- read.csv(filename, na = "", sep=separator, stringsAsFactors = FALSE, header=T,
                colClasses=c('character'),)
str(df1)
str(df0)
df0 <- subset(df0, select=-c(no))
df1 <- subset(df1, select=-c(no, ImageName))

str(df0)
str(df1)
dfMerge <- merge(df0,df1,by.x = 'name', by.y = 'ImageId')

str(dfMerge)
dfMerge$chk1 <- as.integer(dfMerge$num1.x==dfMerge$num1.y)
dfMerge$chk2 <- as.integer(dfMerge$num2.x==dfMerge$num2.y)
dfMerge$chk3 <- as.integer(dfMerge$num3.x==dfMerge$num3.y)
dfMerge$chk4 <- as.integer(dfMerge$num4.x==dfMerge$num4.y)
dfMerge$chk5 <- as.integer(dfMerge$num5.x==dfMerge$num5.y)
dfMerge$chk6 <- as.integer(dfMerge$num6.x==dfMerge$num6.y)
dfMerge$chk7 <- as.integer(dfMerge$num7.x==dfMerge$num7.y)
dfMerge$chk8 <- as.integer(dfMerge$num8.x==dfMerge$num8.y)
dfMerge$chk9 <- as.integer(dfMerge$num9.x==dfMerge$num9.y)

dfMerge
target_file <- paste0(base_path, "exp3_compare1.txt")
write.csv(dfMerge, fileEncoding="UTF-8", file = target_file)
str(df0)

layout(matrix(1:4, ncol = 2))
as.matrix(df0)['num1','num2']
image(as.matrix(df0)[num1, num2], main = "Original distances")
image(as.matrix(df1)[num1, num2], main = "Cophenetic distances")
image((as.matrix(df0) - as.matrix(df1))[num1, num2], 
      main = "Cophenetic - Original")
plot(df0 ~ df1, ylab = "Cophenetic distances", xlab = "Original distances",
     main = "Shepard Plot")
abline(0,1, col = "red")
box()
layout(1)