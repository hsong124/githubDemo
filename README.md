<<<<<<< Updated upstream
# githubDemo
=======
# githubDemo

### Cloning a repository:
Open your command prompt
Find the directory/folder you want to put the repo in
Clone the repo
'git clone <repo link>'

### Branches
You will automatically be on develop as that was set as the default branch
To check which branch you are on:
'git branch'
To checkout a different branch:
'git checkout <branchname>'
To make a new branch and check it out
'git checkout -b <new branchname>'

### Pushing your changes 
After you have made changes to the repository like creating a new file or editing a file,
you need to push it up to the remote repository so others can use/see/pull it.
To see what has been changed:
'git status'
To add to staging:
'git add *'
The '*' will add everything that changed, you can also just do 'git add <changedfilename>'
To make a commit:
'git commit -m <your comment here>'
To push
'git push'
If it is the first time pushing from a branch on your local machine, you will need to set the upstream:
'git push --set-upstream origin <branchname>'

### Pull and Fetch
In general, simply pulling will be enough, but if you want to see all the branches, use fetch
To pull a branch from the repo:
'git pull'
To fetch all branches from the repo:
'git fetch'
[Here](https://stackoverflow.com/questions/24151990/pull-all-branches-from-origin) are more details if you are interested.

### General Flow
There are two protected branches: master and develop.
When pushing to master, all code should have gone through qa, security, etc. as it usually deploys to production.
You can think of develop as the main branch to work off of. When you have a new feature, or are fixing a new bug, you branch off of develop and then merge back into develop using a pull request.
A pull request is essentially you asking to have your code integrated with the base branch.
Create a new pull request using the github website. It will typically need at least one approval before it can be merged back into develop. This is a type of branch rule, which can be changed in settings of the repository on the github website.

>>>>>>> Stashed changes
