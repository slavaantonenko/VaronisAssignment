from constants import GITHUB_TOKEN
from enforcer import enforce
from misconfig_detection import detect
from github import Github, GithubException

def main():
    try:
        security_risks = {"REPO": list(), "BRANCH": list()}
        github_obj = Github(GITHUB_TOKEN)

        detect(github_obj, security_risks)
        enforce(github_obj, security_risks)
    except GithubException as e:
        print(f"Failed to access github {e.data}")

if __name__ == "__main__":
    main()