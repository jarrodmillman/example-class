## Initialize

```bash
curl -u <token>:x-oauth-basic https://api.github.com/user/repos?type=member\&page=1\&per_page=100 > repos.json
curl -u <token>:x-oauth-basic https://api.github.com/user/repos?type=member\&page=2\&per_page=100 >> repos.json 
```

And then use `repos.py` to create `grades.json`.

## Leave individual repos

```bash
curl -u <token>:x-oauth-basic -X DELETE https://api.github.com/repos/:owner/:repo/collaborators/:username
```



## SIDS from bearfacts

Bearfacts data can be downloaded in weird Excel format (not useful for computing).

To extract SIDS from it one summer, I did something like:

library(gdata)
students = read.xls("tmp/studentsExcelFile.xls")
sids = as.character(students$Class[-c(1:3)])[-41]

library(rjson)
sink("sids.json")
cat(toJSON(unname(sapply(sids, substr, start=1, stop=8))))
sink()
