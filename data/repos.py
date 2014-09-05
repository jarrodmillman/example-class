import json

# load json returned from Github API
with open('github/repos.json') as infile:
    repos = json.load(infile)

# only keep ones with the correct repo name
repos = [x for x in repos if x["name"] == 'stat133']
grades = [dict(login=x['owner']['login'], url=x['ssh_url']) for x in repos]
grades = dict(students={x['login']:x for x in grades})

with open('grades.json', 'w') as outfile:
    json.dump(grades, outfile, sort_keys=True, indent=4)

