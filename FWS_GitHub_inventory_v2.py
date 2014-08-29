import urllib2

github = "https://github.com"
githubPeeps = "https://github.com/orgs/USFWS/people"
gitRepoSuffix = "?tab=repositories"

tagIn = ' <a class="member-link" href=' 
tagOut = '" itemprop="url">'

tagIn2  =  '<h3 class="repo-list-name">'
tagOut2 =  '">'

listGitters = []
listRepos = []

def AmIForked():
    closeTag = html.find("</h3>")
    closeCloseTag = html[closeTag:].find("<h3 class")
    #print html[closeTag:closeCloseTag]
    if "forked from" in html[closeTag:closeCloseTag]: return True
    else:  return False

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
        
		if not testRepo: listRepos.append([items,strRepo])

        # Test for the last element on the page
        if tagIn2 in html:
            print "TRUE"
        else:
            logical = False
        #print html
######  BOGUS OUTPUT #####  create --> output to Sharepoint
for rows in listRepos:
    print listRepos
    
