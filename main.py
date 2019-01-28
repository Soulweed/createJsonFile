import json
import csv

jsonTemplate = json.load(open('./template.config.json'))

with open('./file.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for read in reader:
        temp = read[0].split(';')
        jsonfile = temp[0]+'.config.json'
        jsonTemplate.update({u'agent_id': str(temp[0]).decode('utf-8'),
                             u'device' : str(temp[1]).decode('utf-8'),
                             u''
                             }) # Add key that you want to update value 
        
        data = json.dumps(jsonTemplate,indent=4)
        f = open(jsonfile, 'w')
        f.write(data)
        f.close()

    csvfile.close()