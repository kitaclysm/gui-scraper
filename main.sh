# for testing CLI implementation, check if needed for GUI
read -p 'Full url: ' BASH_URL
export BASH_URL
python3 src/main.py
# cd public && python3 -m http.server 8888