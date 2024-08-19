from constants import Configurations, BRANCH_NAME, GITHUB_TOKEN, REPO_NAME
from github import Github, GithubException

def detect(github_obj, security_risks, run_params):
    try:
        repo = github_obj.get_repo(REPO_NAME)

        if (run_params == "" or run_params == "repo"):
            security_risks['REPO'] = __repo(repo)

        if (run_params == "" or run_params == "branch"):
            security_risks['BRANCH'] = __branch(repo, BRANCH_NAME)
    except GithubException as e:
        print(f"Failed to access repository '{REPO_NAME}': {e.data}")

# Get all repo related misconfigurations
def __repo(repo):
    try:
        security_risks = list()

        result = __is_repo_private(repo)

        if (result is False):
            security_risks.append(Configurations.REPOSITORY_VISIBILITY)
    except GithubException as e:
        print(f"Failed to access repo '{repo.name}': {e.data}")

    return security_risks

def __is_repo_private(repo):
    if repo.private:
        print(f"Repository '{repo.name}' is already private.")
        return True

    print(f"Repository '{repo.name}' is public, this is a security risk.")
    return False

# Get all branch related misconfigurations
def __branch(repo, branch_name):
    try:
        security_risks = list()

        # Get the branch object
        branch = repo.get_branch(branch_name)
        result = __branch_protection_rules_enabled(repo.name, branch, branch_name)

        if (result is False):
            security_risks.append(Configurations.BRANCH_PROTECTION_RULES)
    except GithubException as e:
        print(f"Failed to access repo '{repo.name}' branch '{branch_name}': {e.data}")

    return security_risks

def __branch_protection_rules_enabled(repo_name, branch, branch_name):
    try:
        protection = branch.get_protection()
            
        if protection:
            print(f"Branch protection rules are already set for '{branch_name}' branch in '{repo_name}'.")
            return True
    except GithubException as e:
        if e.status == 404:
            print(f"No branch protection found for '{branch_name}' in '{repo_name}'.")
        else:
            print(f"Branch protection not set properly for '{branch_name}' in '{repo_name}'.")

    return False