apt update && apt upgrade
apt install wget

rm -rif check.py
wget https://raw.githubusercontent.com/iq7j/checkifthenumberisvaild/main/check.py
echo "done"
