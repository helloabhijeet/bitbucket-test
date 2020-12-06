# bitbucket-test
python script to test the invalid permissions set across project or repo

1. First make changes in bibucket-api.ini file. This file holds information about the admin user credentials and bitbucket server base URL

2. To Run the script use below format (please make sure that you have Python3 installed on your machine):
    python user-permissions.py <bitbucket_user> <project_name> <repo_name> <expected_role>. 

** If Repository access check is not required, pass "", Permissons will be checked at Project level

<h3> Examples </h3> <br> 

1. To check the project level access use below command:<br>
    <b>python3 user-permissions.py TestUser3 proja "" PROJECT_WRITE</b><br> 
    <br>
    Input Argument details: <br>
    <b> TestUser3 </b>: bitbucket user name <br>
    <b> proja </b>: project key of the project <br>
    <b> "" </b>: repo name is empty because we just need to check project <br>
    <b> PROJECT_WRITE </b>: expected access level <br>
    <br>
    
2. To check the repo level access use below command:<br>
    <b>python3 user-permissions.py TestUser3 proja project-a-repo1 PROJECT_WRITE</b><br>
    <br>
    Input Argument details: <br>
    <b> TestUser3 </b>: bitbucket user name<br>
    <b> proja </b>: project key of the project<br>
    <b> project-a-repo1 </b>: repo name <br>
    <b> PROJECT_WRITE </b>: expected access level<br>
