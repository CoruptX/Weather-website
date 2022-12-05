1. go inside the folder of the project
2. open git bash there by right click
3. creating a new repository by executing following..
repository is a place to store code.
	$ git init 
4. step3 will create an empty repository
5. we should add files into empty repository by
 execting following
	$ git add .
6. This line will add all the files to staging area.
7. We put the code in repository by a process of commit
	$ git commit -m "message for commit"
8. Now files are stored in the local repository

LOCAL REPOSITORY means REPOSITory created on your own
 computer/machine

REMOTE REPOSITORY means REPOSITORY created on github

9. open github on your browser and login.
10. Create a new repository on github with same name.
11. go back to git bash and tell it that this github repository is going 
to be remote one. Where we will upload the code
 $git remote add origin https://github.com/rupeshkanth218/articles.git

12. UPLOAD THE CODE to remote server(github)
	a. FOR THE first time
		$git push -u origin master
	b. nex time onwards
		$git push origin