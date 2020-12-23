import os
from github import Github

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Create a Github instance using an access token
g = Github(os.getenv("GITHUB_TOKEN"))

# List of repos and their information
myRepos = []

# Github objects:
for repo in g.get_user().get_repos():
    # Only fetch public repositories
    if repo.private == False:
        # Create repo key/value pair and add to myRepos:
        # Name, URL, Description, Language, Created at, Forks, 
        # Open issues, Size (kb), Star count
        currRepo = {"name": repo.name, "url": repo.html_url, "description": repo.description,
            "language": repo.language, "creation": repo.created_at, "forks": repo.forks_count, 
            "issues": repo.open_issues_count, "size": repo.size, "stars": repo.stargazers_count}
        myRepos.append(currRepo)
print(myRepos)