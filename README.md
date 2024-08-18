# MisConfigurationsManager

## Implemention

### Overview

This script demonstrates the risks associated with misconfiguring GitHub repository settings, specifically focusing on repository visibility and branch protection rules. By running this script, you would be able to see if these risks are already enforeced, if not the script enforced them automatically.

### Functionality
- Check if a repository is public and, if so, change it to private.
- Check if branch protection rules are set on a specified branch and, if not, apply default protection rules.

### Virtual env
It's better to use a virtual environment to run Python code. This way, you can avoid installing packages directly on your computer and manage multiple environments for different projects.
Most usefull tools are `conda` and `pyenv`

### Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **PyGithub**: Install the PyGithub SDK using pip:
   ```pip install PyGithub```
3. Navigate to `MisConfigurationsManager` directory where the source code is located.
4. Update in `constants.py` the desired repo, branch and Github token.
5. **Setting Up the GitHub Token**

- 5a. Go to GitHub Settings

   - Navigate to [GitHub Settings](https://github.com/settings/tokens).
   - Click on the `Generate new token` button.
   - For this script, you need to select the following scopes:
     - `repo` (for private repository access)
     - `admin:repo_hook` (for branch protection)

- 5b. Update `constants.py`
   - Open the `constants.py` file in your project.
   - Replace the placeholder `your_personal_access_token` with the token you copied.
   - Save the changes to `constants.py`.
2. **Run**: ```python main.py```

#### Execution examples
Repo visibility
![plot](./status/repo_visibility.png)

Branch protection rules
![plot](./status/branch_protection_rules.png)

## Repository Visibility misconfiguration

**Meaning of this Configuration:**

Repository visibility determines who can see and access the code in a repository. Repositories can be either **public** or **private**:
- **Public Repositories**: Anyone on the internet can view and clone the repository.
- **Private Repositories**: Only people you explicitly grant access to can view or work with the repository.

**Best Practice:**

- **Private Repositories**: For projects that contain sensitive or proprietary information, it's a best practice to set the repository to private. This helps protect the code from unauthorized access.

**Steps to Fix the Configuration Manually:**

1. **Navigate to the Repository on GitHub**:
   - Go to the GitHub website and open the repository you want to change.
   
2. **Access the Settings**:
   - Click on the `Settings` tab located at the top of the repository page.

3. **Change Visibility**:
   - In the `Settings` menu, scroll down to the `Danger Zone` section.
   - Click on `Change repository visibility`.
   - Choose `Make private`, and follow the prompts to confirm.

**Workaround for Risks:**

- If you need to keep a repository public but want to limit access, consider using GitHub's `Code Scanning Alerts` and `Audit logs` to monitor all operations. However, this is not a substitute for setting the repository to private if confidentiality is a concern.

**Impact on Working with GitHub:**

Changing a repository from public to private restricts who can view or contribute to the code. This enhances security but requires you to manage and grant access to collaborators explicitly.</br>
So, if access restrictions wasn't configured properly before going private, it can prevent some of the users that weren't given access from being able to use the repo. </br>
Moreover, it can break automated pipelines that are using this repo. </br>

<b>NOTE: It's highly important to verify the repo access configuration before making the repo private</b>


## Misconfigurations infrastructure