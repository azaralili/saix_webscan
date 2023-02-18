import re

clnurl = ""
with open(r"/home/kali/Desktop/result.txt") as file:
    for line in file:
        url = re.findall("(?P<url>https?://[^\s]+)", line)
        if len(url) == 0:
            continue
        url = url[0]
        url = url[:-1]
        print(url)
        clnurl = url
        with open("/home/kali/Desktop/cleanurl.txt", 'a') as result:
            result.write(str(clnurl)+'\n')
