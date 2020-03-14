multiple_cmd() { 
    echo $1;  #put command here
}; 
export -f multiple_cmd; 
find . -type d  -exec bash -c 'multiple_cmd "$0"' {} \;
