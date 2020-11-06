def knowme():
    greeting = "Getting to know me!!"
    name = "Biography"
    doa = "N/A"
    job = "knowme Link"
    embed = "https://docs.google.com/document/d/1eraYQJxeKZMs2jIfLqTlP15P6V-SPBlfNjDUKnpwh3k/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def runtime():
    greeting = "No feelings!"
    name = "Coder Joes Repl"
    doa = "November 6"
    job = "Runtime Link"
    embed = "https://repl.it/@BraydenBasinger/Flask-Web-Series-Coder-Joes#main.py"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def planning():
    greeting = "Only Artifacts!"
    name = "Padlet"
    doa = "October 23"
    job = "Project Planning"
    embed = "https://padlet.com/jmortensen7/csptime1_2"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def journal():
    greeting = "No feelings!"
    name = "Google Doc"
    doa = "Never! Keep Working!"
    job = "Journal Record"
    embed = "https://docs.google.com/document/d/1gujp2Y736AuA5281oYEUouxItbU_b3Ntq_5H199rxXk/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def playground():
    greeting = "Only Artifacts!"
    name = "Snake Game Playground"
    doa = "Never! Keep Working!"
    job = "Playground"
    embed = "https://repl.it/@ryanmgds/playground#main.py"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "embed": embed}
    return info

def code():
    greeting = "No feelings!"
    name = "Gist"
    doa = "November 6"
    job = "Code Sample"
    gist = "https://gist.github.com/jm1021/cfb277c7357e02fcb4123a6c7429a5c1.js"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "gist": gist}
    return info

def alldata():
    return [runtime(), planning(), journal(), playground(), code(), knowme()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Ryan's Personal Work"
    github = "https://github.com/ryanmgds/personalweek9"
    youtube = "https://www.youtube.com/channel/UCZnCh2FDjYaWZCFFA9mWaGg?view_as=subscriber"
    source = {"name": name, "github": github, "youtube": youtube}
    #Project Data
    project1 =  "Guess the Number Game"
    projlinks1 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@BraydenBasinger/First-Project-Guess-The-Number#README.md"),
        Link("Resources", "https://padlet.com/jmortensen7/csp2021")
    ]
    project2 =  "Coder Joes"
    projlinks2 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@BraydenBasinger/Flask-Web-Series-Coder-Joes#README.MD"),
        Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

#Project data class contain project name and links (Link class objects)
class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects
