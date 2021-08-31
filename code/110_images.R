# generate 153 ground truth - execute once
base_path = 'D:/LYIT/repository/yolo/detect_digit/testimages/dataset1/'
filenames <- list.files(base_path,
                        pattern="*.jpg", full.names=TRUE)

dfResult <- data.frame("file"= character(0), "name"=character(0), "result"=character(0), stringsAsFactors=FALSE)
for(f in filenames){
  row <- data.frame(file = f, 
                    name = tools::file_path_sans_ext(basename(f)), 
                    result = "", 
                    collapse = "")
  dfResult <- rbind(dfResult, row)
}
write.csv(dfResult, fileEncoding="UTF-8", 
          file = 'D:/LYIT/repository/yolo/detect_digit/testimages/exp1_ground_truth.txt')

