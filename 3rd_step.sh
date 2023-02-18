mkdir /home/kali/Desktop/webfiles/
sed -n '4p' cleanurl.txt > /home/kali/Desktop/1_link_download.txt
cd /home/kali/Desktop/webfiles/
wget -r -np -nH --cut-dirs=3 -R index.html -i /home/kali/Desktop/1_link_download.txt
