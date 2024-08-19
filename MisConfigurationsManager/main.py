import sys

from constants import GITHUB_TOKEN
from enforcer import enforce
from misconfig_detection import detect
from github import Github, GithubException

def main():
    try:
        run_type = "" if len(sys.argv) == 1 else sys.argv[1]
        security_risks = {"REPO": list(), "BRANCH": list()}
        github_obj = Github(GITHUB_TOKEN)

        detect(github_obj, security_risks, run_type)
        enforce(github_obj, security_risks)
    except GithubException as e:
        print(f"Failed to access github {e.data}")

if __name__ == "__main__":
    main()