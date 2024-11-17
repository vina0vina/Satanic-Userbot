git clone https://github.com/vina0vina/Satanic-Userbot.git

Nama:vina0vina

sudo apt update && sudo apt upgrade -y

sudo apt install python3.10-venv ffmpeg -y

cd Satanic

screen -S Satanic

python3 -m venv vina

source vina/bin/activate

pip install --no-cache-dir -r requirements.txt

cp sample.env .env

nano .env

bash start
