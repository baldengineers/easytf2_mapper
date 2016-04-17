#easy tf2 mapper updater!!
import urllib.request
import urllib.parse
import zipfile

try:
    #
    #downloads zip
    #
    url = 'http://github.com/baldengineers/easytf2_mapper/archive/master.zip'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req) 
    respData = resp.read()             

    saveFile = open('tmp/latest.zip', 'w') 
    saveFile.write(str(respData))
    saveFile.close()

    #
    #unpacks master zip
    #
    zipupdate = zipfile.ZipFile('tmp/latest.zip', 'r+')
    zipupdate.extract('latestwinredist/easytf2mapper_latest.zip','updated/')
    zipupdate.close()

    #
    #unpacks latest zip
    #
    ziplatest = zipfile.ZipFile('updated/easytf2mapper_latest.zip')
    ziplatest.extractall('updated/')
    ziplatest.close()

    #removes zip after it's done
    os.remove('updated/easytf2mapper_latest.zip')

    #status
    print("Update successful. You can find the updated version in the /updated directory.")
except Exception as e:
    #status if errors
    print(str(e))
#gives status

