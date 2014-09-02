import urllib2,os

###################
#  Constants and Declares
###################
github = "https://github.com"
githubPeeps = "https://github.com/orgs/USFWS/people"
gitRepoSuffix = "?tab=repositories"

tagIn = ' <a class="member-link" href=' 
tagOut = '" itemprop="url">'

tagIn2  =  '<h3 class="repo-list-name">'
tagOut2 =  '">'

listGitters = []
listRepos = []

#################
#  local subs
#################
def AmIForked():
    closeTag = html.find("</h3>")
    closeCloseTag = html[closeTag:].find("<h3 class")
    #print html[closeTag:closeCloseTag]
    if "forked from" in html[closeTag:closeCloseTag]: return True
    else:  return False

def SimpleTwoColumnTable( inputList , outputFile = "GIT_users.htm"):
    '''  A supersimple 2-column HTML Page Generator
	         inputList is a list-of-lists n-length of ['user', 'url_path_to_repo']
	'''
    def writeRow(inputRow,f):
        f.write( "<tr> \n" )
        for items in inputRow:
            outString = '''<a href="'''+items[1]+'''" target="_blank">'''+ os.path.split(items[0])[1]+'''</a> '''
            f.write( "  <td>" +outString + "</td> \n" )
        f.write( "</tr> \n" )
    
    line1 = "	<!DOCTYPE html> \n \n <html> \n \n <head> \n <style> \n"
    line2 =  "table, th, td { border: 1px solid black; \n \n </style> \n \n </head> \n \n } "
    line3 = ''' <body> \n \n <table style="width:100%"> \n '''
    line4 = " </table> \n </body> \n </html> "
	
    f = open(outputFile, "w")
    f.write(line1)
    f.write(line2)
    f.write(line3)
    
    for pairs in inputList:
        writeRow(pairs,f)
    
    f.write(line4)
    f.close()
	

#######
#  Programs Starts Here
#######
response = urllib2.urlopen(githubPeeps)
html = response.read()

start = html.find(tagIn)
#print start

if tagIn in html:
    start = html.find(tagIn)
    end = html.find(tagOut)

    readStart = start+len(tagIn) + 2

    print html[readStart:end]
    listGitters.append( html[readStart:end] )

    html = html[readStart:]  #  the ol' fast forward trick, once through

	#  Now iterate through all the members of the FWS Organization
for items in listGitters:
    gitterHub = github +"/"+ items + gitRepoSuffix
    response = urllib2.urlopen(gitterHub)
    html = response.read()

    logical = True
    while logical:
        start = html.find(tagIn2)
        readStart = start+len(tagIn2) + 14
        html = html[readStart:]
        end = html.find(tagOut2)

        strRepo = github+html[:end]
        print strRepo
        testRepo = AmIForked()
        print "forked:",testRepo
        
        if not testRepo: listRepos.append([(items,gitterHub),(strRepo,strRepo)])

        # Test for the last element on the page
        if tagIn2 in html:
            print "TRUE"
        else:
            logical = False
        #print html
######  BOGUS OUTPUT #####  create --> output to Sharepoint
for rows in listRepos:
    print rows[0][0],"--->", rows[1][1]
######    REAL OUTPUT #####   Defaults to "GitHub.htm" in same directory	
SimpleTwoColumnTable(listRepos)
