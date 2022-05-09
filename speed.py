from re import sub
import subprocess
import re

def get_speed():
    output = subprocess.run(['speedtest'], capture_output=True).stdout.decode()
    re_exp = 'Download:\s(.*)'
    internet_speed = re.findall(re_exp, output)
    print(internet_speed)
    
    
if __name__ == '__main__':
    get_speed()