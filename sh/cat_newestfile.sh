#ls -lht list file by time
#head -n 2 get result from list secound 
# tail -n 1 get result form list end
# awk '{print $9}' get filename
#tail -f read file 
tail -f $(ls -lht | head -n 2 | tail -n 1 | awk '{print $9}')