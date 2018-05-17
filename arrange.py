import json
#Path you want, enter below
path = "/home/user"
with open('%s/dataset.json'%(path)) as f:
        data = json.load(f)
Url_File = open("%s/Urls.log"%(path),"w")
Id_File = open("%s/Ids.log"%(path),"w")
for video in data['database']:
        #url_dic[video] = data['database'][video]['url']
        Url_File.write("%s\n"%(data['database'][video]['url']))
        Id_File.write("%s\n"%(data['database'][video]))
Url_File.close()
Id_File.close()
