library(jpeg)

setwd("~/R/NASA Lights")

run_quarters <- function(file2012, file2016) {
  map_2012 <- jpeg::readJPEG(file2012)
  map_2016 <- jpeg::readJPEG(file2016)
  
  maps_2012 <- list()
  maps_2012[[1]] <- map_2012[1:10800, 1:10800]
  maps_2012[[2]] <- map_2012[10801:21600, 1:10800]
  maps_2012[[3]] <- map_2012[1:10800, 10801:21600]
  maps_2012[[4]] <- map_2012[10801:21600, 10801:21600]
  rm(map_2012)
  
  maps_2016 <- list()
  maps_2016[[1]] <- map_2016[1:10800, 1:10800]
  maps_2016[[2]] <- map_2016[10801:21600, 1:10800]
  maps_2016[[3]] <- map_2016[1:10800, 10801:21600]
  maps_2016[[4]] <- map_2016[10801:21600, 10801:21600]
  rm(map_2016)
  
  for (i in 1:4) {
    new <- maps_2016[[i]] - maps_2012[[i]]
    gone <- maps_2012[[i]] - maps_2016[[i]]
    
    new <- replace(new, new < 0, 0)
    gone <- replace(gone, gone < 0, 0)
    
    diffs <-
      array(c(matrix(
              rep(0, 116640000), nrow = 10800, ncol = 10800),
              new, 
              gone),  c(10800, 10800, 3))
    
    jpeg::writeJPEG(diffs,
              target = paste(
                'diff/BlackMarble_diff',
                strsplit(file2012, "_")[[1]][3],
                i,
                'color.jpg',
                sep = "_"
              ))
    rm(new, gone, diffs)
  }
}

run_quarters('2012/BlackMarble_2012_A1_gray.jpg','2016/BlackMarble_2016_A1_gray.jpg')
run_quarters('2012/BlackMarble_2012_A2_gray.jpg','2016/BlackMarble_2016_A2_gray.jpg')
run_quarters('2012/BlackMarble_2012_B1_gray.jpg','2016/BlackMarble_2016_B1_gray.jpg')
run_quarters('2012/BlackMarble_2012_B2_gray.jpg','2016/BlackMarble_2016_B2_gray.jpg')
run_quarters('2012/BlackMarble_2012_c1_gray.jpg','2016/BlackMarble_2016_C1_gray.jpg')
run_quarters('2012/BlackMarble_2012_c2_gray.jpg','2016/BlackMarble_2016_C2_gray.jpg')
run_quarters('2012/BlackMarble_2012_D1_gray.jpg','2016/BlackMarble_2016_D1_gray.jpg')
run_quarters('2012/BlackMarble_2012_D2_gray.jpg','2016/BlackMarble_2016_D2_gray.jpg')







eigth <- "A1"

Q1 <- jpeg::readJPEG(paste("diff/BlackMarble_diff", eigth, 1, "color.jpg", sep="_"))
Q2 <- jpeg::readJPEG(paste("diff/BlackMarble_diff", eigth, 2, "color.jpg", sep="_"))
Q3 <- jpeg::readJPEG(paste("diff/BlackMarble_diff", eigth, 3, "color.jpg", sep="_"))
Q4 <- jpeg::readJPEG(paste("diff/BlackMarble_diff", eigth, 4, "color.jpg", sep="_"))


diff[1:10800, 1:10800]         <- Q1
diff[10801:21600, 1:10800]     <- Q2
diff[1:10800, 10801:21600]     <- Q3
diff[10801:21600, 10801:21600] <- Q4

rm(Q1, Q2, Q3, Q4)


jpeg::writeJPEG(diff, paste("diff/BlackMarble_diff", eigth, "color.jpg", sep="_"))
