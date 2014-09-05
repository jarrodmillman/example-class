example-class
=============

Example class repo for use with
[gradebook](https://github.com/jarrodmillman/gradebook).


1. Read `data/README.md` and create `data/grades.json`
1. Clone instructor repos with `gb-clone instructor`
1. Clone student repos with `gb-clone student`
1. Clone project repos with `gb-clone project`

Here is what the repo might look like once you have one
student and have assigned one homework.

```
    .
    ├── data
    │   ├── github
    │   │   └── repos.json
    │   ├── grades.json
    │   ├── README.md
    │   └── repos.py
    ├── log
    │   └── 2014-09-04-assigned-hw1.log
    ├── README.md
    └── repos
        ├── instructor
        │   └── assignments
        │       ├── hw1
        │       │   ├── ex1-data.csv
        │       │   ├── ex1.r
        │       │   └── ex1-sol.r
        │       └── hw2.py
        └── students
            └── student1
                └── hw1
                   ├── ex1.r
                   └── ex1-data.csv
```
