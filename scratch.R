library(jpeg)


A1_2012 <- readJPEG('2012/BlackMarble_2012_A1_gray.jpg')
A1_2012.1 <- A1_2012[1:10800,1:10800]
A1_2012.2 <- A1_2012[10801:21600,1:10800]
A1_2012.3 <- A1_2012[1:10800,10801:21600]
A1_2012.4 <- A1_2012[10801:21600,10801:21600]

rm(A1_2012)

A1_2016 <- readJPEG('2016/BlackMarble_2016_A1_gray.jpg')
A1_2016.1 <- A1_2016[1:10800,1:10800]
A1_2016.2 <- A1_2016[10801:21600,1:10800]
A1_2016.3 <- A1_2016[1:10800,10801:21600]
A1_2016.4 <- A1_2016[10801:21600,10801:21600]

rm(A1_2016)

A1_new.1 <- A1_2016.1 - A1_2012.1
#writeJPEG(A1_diff, target = 'diff/BlackMarble_diff_A1_gray.jpg')
A1_gone.1 <- A1_2012.1 - A1_2016.1
#writeJPEG(A1_diff2, target = 'diff/BlackMarble_diff2_A1_gray.jpg')
rm(A1_2012.1); rm(A1_2016.1)

A1_new_abs.1 <- replace(A1_new.1, A1_new.1 <0, 0)
A1_gone_abs.1 <- replace(A1_gone.1, A1_gone.1 <0, 0)
rm(A1_new.1); rm(A1_gone.1)

diffs.1 <- array(c(A1_new_abs.1, A1_gone_abs.1, matrix(rep(0,116640000),nrow=10800,ncol=10800)), c(10800, 10800, 3))
rm(A1_new_abs.1); rm(A1_gone_abs.1)

writeJPEG(diffs.1, target = 'diff/BlackMarble_diff.1_A1_2d.jpg')




run_quarters <- function(file2012, file2016){
  map_2012 <- readJPEG(file2012)
  map_2016 <- readJPEG(file2016)
  
  maps_2012 <- list()
  maps_2012[[1]] <- map_2012[1:10800,1:10800]
  maps_2012[[2]] <- map_2012[10801:21600,1:10800]
  maps_2012[[3]] <- map_2012[1:10800,10801:21600]
  maps_2012[[4]] <- map_2012[10801:21600,10801:21600]
  rm(map_2012)
  
  maps_2016 <- list()
  maps_2016[[1]] <- map_2016[1:10800,1:10800]
  maps_2016[[2]] <- map_2016[10801:21600,1:10800]
  maps_2016[[3]] <- map_2016[1:10800,10801:21600]
  maps_2016[[4]] <- map_2016[10801:21600,10801:21600]
  rm(map_2016)
  
  for (i in 1:4){
    new <- maps_2016[[i]] - maps_2012[[i]]
    gone <- maps_2012[[i]] - maps_2016[[i]]
    
    new <- replace(new, new <0, 0)
    gone <- replace(gone, gone <0, 0)
    
    diffs <- array(c(new, gone, matrix(rep(0,116640000),nrow=10800,ncol=10800)), c(10800, 10800, 3))
    
    writeJPEG(diffs, target = paste('diff/BlackMarble_diff', strsplit(file2012, "_")[[1]][3], i, 'color.jpg', sep="_"))
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

