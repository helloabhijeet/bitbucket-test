import configparser


import requests
from requests.auth import HTTPBasicAuth
import sys


def read_from_config(prop_key):
    config = configparser.ConfigParser()
    config.read("bitbucket-api.ini")
    propval = config.get('Bitbucket API', prop_key)
    return propval


def execute_rest_call(rest_url):
    admin_user_name = read_from_config("adminUser")
    admin_user_pwd = read_from_config("adminPassword")
    r = requests.get(rest_url, auth=HTTPBasicAuth(admin_user_name, admin_user_pwd))
    return r.json()


def prepare_api_url(project_name, repo_name, user_name):
    server_base_url = read_from_config("serverBaseURL")
    if len(project_name) != 0 and len(repo_name) != 0:
        return server_base_url + "/rest/api/1.0/projects/" + project_name + "/repos/" + repo_name + "/permissions/users?filter=" + user_name
    else:
        return server_base_url + "/rest/api/1.0/projects/" + project_name + "/permissions/users?filter=" + user_name


def get_permissions_from_response(response_json):
    try:
        return response_json["values"][0]["permission"]
    except:
        print('User "{0}" has no permissions on Repository or Project => {1}  {2} '.format(bitbucket_user_name, bitbucket_project_name, bitbucket_project_repo_name))
        sys.exit()

def check_repo_level_access(bitbucket_user, project_name, repo_name, expected_role):
    project_repo_url = prepare_api_url(project_name, repo_name, bitbucket_user)
    project_repo_permissions_response = execute_rest_call(project_repo_url)
    project_repo_level_access = get_permissions_from_response(project_repo_permissions_response)
    if expected_role != project_repo_level_access:
        print(
            'User "{0}" permission is not set correctly in Project "{1}" Repository "{2}". Expected permission is "{3}", but configured "{4}"'.format(
                bitbucket_user_name, bitbucket_project_name, bitbucket_project_repo_name,
                expected_role, project_repo_level_access))


def check_project_level_access(bitbucket_user, project_name, expected_role):
    project_url = prepare_api_url(project_name, "", bitbucket_user)
    project_permissions_response = execute_rest_call(project_url)
    project_level_access = get_permissions_from_response(project_permissions_response)
    if expected_role != project_level_access:
        print(
            'User "{0}" permission is not set correctly in Project "{1}". Expected permission is "{2}", but configured "{3}"'.format(
                bitbucket_user_name, bitbucket_project_name, expected_user_access, project_level_access))


def verify_user_permissions(bitbucket_user, project_name, repo_name, expected_role):
    if len(project_name) == 0 or len(bitbucket_user) == 0 or len(expected_role) == 0:
        print(
            'Script ERROR. To run the script, use format "python user-permissions.py <bitbucket_user> <project_name> <repo_name> <expected_role>". bitbucket_user, project_name, expected_role are mandatory, if repository access check not required then just pass "". Please check the inout and try again.')
        sys.exit()

    if len(project_name) != 0 and len(repo_name) != 0:
        check_repo_level_access(bitbucket_user, project_name, repo_name, expected_role)
    else:
        check_project_level_access(bitbucket_user, project_name, expected_role)


if __name__ == '__main__':

    if sys.argv[1] == "--help":
        print(
            'Script Usage: user-permissions.py <bitbucket_user> <project_name> <repo_name> <expected_role>. If Repository access check is not required then just pass "" ')
        sys.exit()

    # set the input variables
    bitbucket_project_name = sys.argv[2]
    bitbucket_project_repo_name = sys.argv[3]
    bitbucket_user_name = sys.argv[1]
    expected_user_access = sys.argv[4]

    verify_user_permissions(bitbucket_user_name, bitbucket_project_name, bitbucket_project_repo_name,
                            expected_user_access)