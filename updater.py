#easy tf2 mapper updater!!
import os
import requests
import zipfile
import shutil
import urllib.request

    
response = input("Are you sure you want to do this? (y/n):")
if response == "y" or response == "yes":
    #location = input("Paste directory of updater here: ")
    try:
        
        #
        #gets file info
        #
        url = 'http://github.com/baldengineers/easytf2_mapper/archive/master.zip'
        site = urllib.request.urlopen(url)
        meta = site.info()
        size = meta["Content-Length"]
        print("File size: ",size," bytes.")
        
        #
        #downloads zip
        #
        with open('easytf2mapper-master.zip', 'wb') as handle:
            response = requests.get('http://github.com/baldengineers/easytf2_mapper/archive/master.zip', stream=True)

            if not response.ok:
                print('something went wrong getting the file.')

            for i,block in enumerate(response.iter_content(1024)):
                print("\n"*50+"%d/%d bytes downloaded (%d percent)" % (i*1024, int(size), (float((i*1024)/int(size))*100)))
                handle.write(block)
        
        print('downloading complete.')
        #
        #unpacks master zip
        #

        zipupdate = zipfile.ZipFile('easytf2mapper-master.zip', 'r')
        for file in zipupdate.namelist():
            if file.startswith('easytf2_mapper-master/latestwinredist'):
                zipupdate.extract(file, 'updated/')
        zipupdate.close()
        print('done unpacking master zip')
        
        #
        #unpacks latest zip
        #
        ziplatest = zipfile.ZipFile('updated/easytf2_mapper-master/latestwinredist/easytf2mapper_latest.zip')
        for file in ziplatest.namelist():
            if file.startswith('updater.exe'):
                pass
            else:
                ziplatest.extract(file)
        ziplatest.close()
        print('done unpacking latest zip')
        
        #removes zip after it's done
        os.remove('easytf2mapper-master.zip')
        shutil.rmtree('updated/easytf2_mapper-master/')

        #status
        print("Update successful. You can find the updated version in the /updated directory.")
    except Exception as e:
        #status if errors
        print('ERROR!\n',str(e))
    #gives status
else:
    print("Aborted.")
    
    

