git clone https://github.com/vina0vina/ubotdidin

Nama:vina0vina

sudo apt update && sudo apt upgrade -y

sudo apt install python3.10-venv ffmpeg -y

cd ubotdidin

screen -S ubotdidin

python3 -m venv didin

source didin/bin/activate

pip install --no-cache-dir -r requirements.txt

cp sample.env .env

nano .env

bash start
