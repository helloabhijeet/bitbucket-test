# bitbucket-test
python script to test the invalid permissions set across project or repo

1. First make changes in bibucket-api.ini file. This file holds information about the admin user credentials and bitbucket server base URL

2. To Run the script use below format (please make sure that you have Python3 installed on your machine):
    python user-permissions.py <bitbucket_user> <project_name> <repo_name> <expected_role>. 

** If Repository level access check is not required, pass "" , Permissons will be checked at Project level

<h3> Sample Commands </h3> <br> 

1. To check the Project level permissions use below command:<br>
    <b>python3 user-permissions.py TestUser3 proja "" PROJECT_WRITE</b><br> 
    <br>
    Input Arguments Explained : <br>
    <b> TestUser3 </b>: Bitbucket User name <br>
    <b> proja </b>: Project key <br>
    <b> "" </b>: Repository name is blank as we are checking permissions at Project Level <br>
    <b> PROJECT_WRITE </b>: Expected access <br>
    <br>
    
2. To check the Repository level permissions use below command:<br>
    <b>python3 user-permissions.py TestUser3 proja project-a-repo1 PROJECT_WRITE</b><br>
    <br>
    Input Arguments Explained: <br>
    <b> TestUser3 </b>: bitbucket user name<br>
    <b> proja </b>: Project key<br>
    <b> project-a-repo1 </b>: Repository name <br>
    <b> PROJECT_WRITE </b>: Expected access<br>
