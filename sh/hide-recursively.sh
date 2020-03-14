multiple_cmd() { 
    # put commands below
    echo "Hiding in  $1"; 
    echo "desktop.ini" > .hidden;
}; 
export -f multiple_cmd; 
find . -type d  -exec bash -c 'multiple_cmd "$0"' {} \;

echo "Hidden all desktop.ini recursively."
