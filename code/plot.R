df <- read.csv("D:/LYIT/repository/yolo/labelled_meter/unclear/scores2.csv",
               na = "", sep="\t", stringsAsFactors = FALSE)

df <- read.csv("D:/LYIT/dissertation/code/counter140.csv",
               na = "", sep=",", stringsAsFactors = FALSE)
# df <- read.csv("D:/LYIT/repository/yolo/labelled_meter/clear/score.csv", 
#                na = "", sep="\t", stringsAsFactors = FALSE)
file_path <- "D:/LYIT/dissertation/code/dataset-140ground_truth_and_quality.csv"
df <- read.csv(file_path,
               na = "", sep=",", stringsAsFactors = FALSE)

df$status <- as.factor(df$correct)
df1 <- subset(df,select = c(status,quality_score,blur_score))

quality_col <- cut(df1$quality_score,
               breaks = c(0, 10,20,30, 40, 50, 60, 70,80,90,Inf), 
               labels = c('under 10', '11-20', "21-30", "31-40","41-50",
                          "51-60","61-70","71-80","81-90","above 90"), 
               right = FALSE,
               order = TRUE)
df1$quality_level <- quality_col

str(df1)

library(ggplot2)
library(ggpubr)
library(histogram)
hist(df1$quality_score, main = 'sample quality distribution', xlab = 'samples')
hist(df1$blur_score, main = 'sample blur distribution', xlab = 'samples')
str(df1)
library(psych)

pairs.panels(df1,
             smooth = TRUE,# If TRUE, draws loess smooths    
             scale = FALSE, # If TRUE, scales the correlation text font    
             density = TRUE, # If TRUE, adds density plots and histograms    
             ellipses = TRUE, # If TRUE, draws ellipses    
             method = "spearman", # Correlation method (also "pearson" or "kendall")    
             pch = 21, # pch symbol    
             lm = FALSE, # If TRUE, plots linear fit rather than the LOESS (smoothed) fit    
             cor = TRUE, # If TRUE, reports correlations    
             jiggle = FALSE, # If TRUE, data points are jittered    
             factor = 2, # Jittering factor    
             hist.col = 4, # Histograms color  # stars = TRUE, # If TRUE, adds significance level with stars    
             stars = TRUE, 
             ci = TRUE) 

# distribution of quality
histogram(~quality_score | status, data = df1,
          main = "distribution of quality score",
          xlab = "recognition result",
          ylab = "quality score")

# distribution of blur
histogram(~blur_score | status, data = df1,
          main = "distribution of quality score",
          xlab = "recognition result",
          ylab = "quality score")



# summary with row column total values
tb <- table(df1$status, df1$quality_score)
addmargins(tb)

barplot(prop.table(tb,2)*100, 
        ylab='Percentages',
        main="percentage recognition by quality", 
        beside=F, 
        col=c("#0073C2FF", "#FC4E07"),
        legend=rownames(tb), 
        args.legend = list(x = "bottomleft"))

chisq.test(tb)




library(VIM) 
library("lattice")

missing_values <- aggr(df1, prop = FALSE, numbers = TRUE)

ggdensity(df1,
          x = "quality_score",
          add = "mean", rug = TRUE,
          title = "quality distribution by recognition status",
          color = "status", 
          fill = "status",
          palette = c("#0073C2FF", "#FC4E07"))



h <- hist(df$score,xlim=c(40,100),ylim=c(0,15), xlab = 'samples', main = 'quality distribution')
text(h$mids,h$counts,labels=h$counts, 
     adj=c(0.2, -0.5), xlab = 'samples')


d <- density(df$score) # returns the density data
plot(d, main='distribution') # plots the results

d <- density(df$score) # returns the density data
plot(d, main='distribution') # plots the results

d <- density(df[df$correct==TRUE,]$score) # returns the density data
plot(d, main='distribution') # plots the results
d <- density(df[df$correct==FALSE,]$score) # returns the density data
plot(d, main='distribution') # plots the results

library(ggplot2)
library(hrbrthemes)
library(dplyr)
library(tidyr)
library(viridis)

# The diamonds dataset is natively available with R.


ggplot(df, aes(x = score, y = correct)) +
  # ???????????????
  geom_point() +
  # ???????????????
  stat_density2d()

ggplot(df, aes(x = score, y = correct)) +
  # ???????????????
  geom_point() +
  # ???????????????:alpha????????????????????????????????????,geom?????????????????????
  stat_density2d(aes(alpha = ..density..), geom = "raster", contour = FALSE)

# ?????????
ggplot(df, aes(x = factor(correct), y = score, 
               fill = factor(correct))) +
  # ???????????????
  geom_boxplot(notch = TRUE) +
  # ????????????
  scale_fill_brewer(palette = "Pastel2")

# ?????????
ggplot(df, aes(x = score)) +
  # ???????????????
  geom_histogram(fill = "lightblue", colour = "black") +
  # ????????????:????????????
  facet_grid(correct ~ .)


ggplot(df, aes(x = factor(correct), y = score, fill = factor(correct))) +
  # ???????????????
  geom_boxplot(notch = TRUE) +
  # ????????????
  scale_fill_brewer(palette = "Pastel2")

ggplot(df, aes(x = factor(correct), y = score, fill = factor(correct))) +
  # ???????????????
  geom_boxplot() +
  # ????????????
  scale_fill_brewer(palette = "Pastel2")


ggplot(df, aes(x = score, fill = correct)) +
  # ??????????????????:alpha????????????????????????
  geom_density(alpha = 0.3)

# Without transparency (left)
p1 <- ggplot(data=df, aes(x=score, group=correct, fill=correct)) +
  geom_density(adjust=1.5) +
  theme_ipsum()
#p1

# With transparency (right)
p2 <- ggplot(data=df, aes(x=score, group=correct, fill=correct)) +
  geom_density(adjust=1.5, alpha=.4) +
  theme_ipsum()


# Interleaved histograms
ggplot(df, aes(x=score, fill=correct)) +
  geom_histogram(binwidth=.5, position="dodge")

ggplot(df, aes(x=score, colour=correct)) + geom_density()


h <- hist(df$score,xlim=c(40,100),ylim=c(0,30), xlab = 'samples', main = 'quality distribution')
text(h$mids,h$counts,labels=h$counts, 
     adj=c(0.2, -0.5), xlab = 'samples')

# blur 
df1 <- read.csv("D:/LYIT/repository/yolo/labelled_meter/unclear/blur_score.csv", 
               na = "", sep="\t", stringsAsFactors = FALSE)
str(df1)

d <- density(df1$score) # returns the density data
plot(d, main='unclear images distribution') # plots the results

# Libraries
library(ggplot2)
library(hrbrthemes)
library(dplyr)
library(tidyr)
library(viridis)

# The diamonds dataset is natively available with R.

# Without transparency (left)
ggplot(data=df, aes(x=score, group=correct, fill=correct)) +
  geom_density(adjust=1.5) +
  theme_ipsum() +
  facet_wrap(~correct) +
  theme(
    legend.position="none",
    panel.spacing = unit(0.1, "lines"),
    axis.ticks.x=element_blank()
  )


ggplot(data = df) +
  geom_bar(mapping = aes(x = correct))

library(ggplot2)
library(dplyr)
library(hrbrthemes)
library(sm)

sm.density.compare(df, correct, xlab="Miles Per Gallon")
title(main="MPG Distribution by Car Cylinders")


# clear number
dfc <- read.csv("D:/LYIT/repository/yolo/labelled_meter/clear/score.csv",
                na = "", sep="\t", stringsAsFactors = FALSE)

h <- hist(dfc$score, xlab = 'samples'
          ,ylim=c(0,50),main = 'good quality distribution')
text(h$mids,h$counts,labels=h$counts, 
     adj=c(0.2, -0.5), xlab = 'samples')


# blur 
df2 <- read.csv("D:/LYIT/repository/yolo/labelled_meter/clear/blur_score.csv", 
               na = "", sep="\t", stringsAsFactors = FALSE)
str(df2)

d <- density(df2[df2$score<15,]$score) # returns the density data
plot(d, main='clear images distribution') # plots the results

h <- hist(df2[df2$score<15,]$score, xlab = 'samples',xlim=c(0,50)
          ,ylim=c(0,40),main = 'good quality distribution')
text(h$mids,h$counts,labels=h$counts, 
     adj=c(0.2, -0.5), xlab = 'samples')


library(ggplot2)
ggplot(df1, aes(x=score)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#FF6666") 
# Color by groups
ggplot(df1, aes(x=score)) + 
  geom_histogram(aes(y=..density..), colour="blue", fill="white")+
  geom_density(alpha=.2, fill="#FF0066") 

ggplot(df2, aes(x=score, color=sex, fill=sex)) + 
  geom_histogram(aes(y=..density..), alpha=0.5, 
                 position="identity")+
  geom_density(alpha=.2) 

