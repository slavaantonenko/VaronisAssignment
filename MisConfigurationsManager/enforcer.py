from constants import Configurations, BRANCH_NAME, GITHUB_TOKEN, REPO_NAME
from github import Github, GithubException

def enfore(github_obj, security_risks):
    try:
        repo = github_obj.get_repo(REPO_NAME)

        for type, risks in security_risks.items():
            match type:
                case "REPO":
                    __repo_enforcer(repo, risks)
                case "BRANCH":
                    __branch_enforcer(repo, risks)
    except GithubException as e:
        if e.status == 404:
            print(f"Repo '{REPO_NAME}' not found in.")
        else:
            print(f"Failed to access repo '{REPO_NAME}': {e.data}")

def __repo_enforcer(repo, risks):
    for config in risks:
        match config:
            case Configurations.REPOSITORY_VISIBILITY:
                __enforce_repo_privacy(repo)

                
def __branch_enforcer(repo, risks):
    for config in risks:
        match config:
            case Configurations.BRANCH_PROTECTION_RULES:
                __enforce_branch_protection(repo, BRANCH_NAME)

# Change repo from public to private
def __enforce_repo_privacy(repo):
    try:
        print(f"Repository '{repo.name}' is public. Changing it to private...")
        repo.edit(private=True)
        print(f"Repository '{repo.name}' is now private.")
    except GithubException as e:
        print(f"Failed to change repository visibility: {e.data}")

def __enforce_branch_protection(repo, branch_name):
    try:
        print(f"Enforcing branch '{branch_name}' protection rules...")
        
        branch = repo.get_branch(branch_name)

        # Enforce branch protection rules
        branch.edit_protection(
            required_approving_review_count=1,  # Require at least 1 approving review
            dismiss_stale_reviews=True,  # Dismiss stale pull request approvals when new commits are pushed
            require_code_owner_reviews=True,  # Require review from code owners
            enforce_admins=True  # Include administrators
        )

        print(f"Branch protection rules enforced for '{branch_name}' branch in '{repo.name}'.")
    
    except GithubException as e:
        if e.status == 404:
            print(f"Branch '{branch_name}' not found in '{repo.name}'.")
        else:
            print(f"Failed to enforce branch protection rules: {e.data}")
