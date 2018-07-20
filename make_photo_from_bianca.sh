ssh -t root@134.28.136.118 -i /home/bianca/.ssh/key_pi_softrobots 'python /home/pi/Git/VideoCapture/takeImage.py'
scp -i /home/bianca/.ssh/key_pi_softrobots root@134.28.136.118:/home/pi/Git/VideoCapture/image.jpg ~/Git/VideoCapture/Images/
