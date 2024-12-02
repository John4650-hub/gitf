import requests
from base64 import b64encode


# push updates.
def pushFileModification(TOKEN, BRANCH, REPO_OWNER, REPO_NAME, FILE_PATH, MESSAGE):
    with open(FILE_PATH, "r") as new_content:
        NEW_CONTENT = new_content.read()

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"

    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    file_data = response.json()
    sha = file_data["sha"]

    # Prepare new file content in base64
    content_encoded = b64encode(NEW_CONTENT.encode()).decode()

    # Update file
    update_data = {
        "message": MESSAGE,
        "content": content_encoded,
        "sha": sha,
        "branch": BRANCH,
    }

    response = requests.put(url, headers=headers, json=update_data)
    response.raise_for_status()

    print(f"{FILE_PATH.split('/')[-1]} updated successfully.")
