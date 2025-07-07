
#เข้า
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental

#pm2 run
cd mjpg-streamer/mjpg-streamer-experimental
mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480 -f 5" -o "output_http.so -p 8080 -w ./www"
# pm2 start --name cam -- mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480 -f 5" -o "output_http.so -p 8080 -w ./www"

ngrok http 8080

https://d1f2-49-237-198-189.ngrok-free.app/?action=stream

/?action=stream
 
#test cam
http://10.99.98.62:8080



http://10.113.254.23:8080



json


ip : hostname -I
mac : e4:5f:01:3b:6f:75
site_id : /etc/mydevice/site_id.txt
uuid : 100000002d8b01a7
name : raspberrypi
sn : : 100000002d8b01a7