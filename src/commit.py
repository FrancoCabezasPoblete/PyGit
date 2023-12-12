from git import Repo
import argparse
import os
import sys

def find_repo_root(start_path):
    """
    Finds the root directory of a Git repository.

    Parameters:
        start_path (str): The starting path to search for the repository.

    Returns:
        str: The absolute path of the repository's root directory.

    Raises:
        Exception: If the repository root cannot be found.

    """
    try:
        repo = Repo(start_path, search_parent_directories=True)
        return repo.git.rev_parse("--show-toplevel")
    except Exception as e:
        print(f"Failed to find repository root: {e}")
        sys.exit(1)

def add_to_gitignore(repo_root, commit_message_file):
    """
    Adds a file to the .gitignore file in the specified repository root.

    Parameters:
        repo_root (str): The path to the root directory of the repository.
        filename (str): The name of the file to be added to .gitignore.

    Returns:
        None
    """
    gitignore_path = os.path.join(repo_root, '.gitignore')

    # Verifies if the file is already in .gitignore
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r+') as file:
            lines = file.readlines()
            if f"{commit_message_file}\n" not in lines:
                file.write(f'\n{commit_message_file}\n')  # Adds the file name to the end of .gitignore
    else:
        with open(gitignore_path, 'w') as file:
            file.write(f'{commit_message_file}\n')  # Creates .gitignore and adds the file name

def has_commits(repo):
    """
    Check if a Git repository has commits.

    Args:
        repo: The Git repository object.

    Returns:
        True if the repository has commits, False otherwise.
    """
    try:
        repo.head.commit
        return True
    except ValueError:
        return False

def main(args):
    
    # Find the repository root
    repo_root = find_repo_root(os.getcwd())
    commit_message_file = os.path.join(repo_root, 'commit_message.md')
    
    # Add the commit message file to .gitignore
    add_to_gitignore(repo_root, 'commit_message.md')
    
    # Set the path to the repository
    repo = Repo(repo_root)
    
    if not os.path.exists(commit_message_file):
        with open(commit_message_file, 'w') as file:
            file.write('<!--Title-->\n\n<!--Description-->\n\n')
        print(f"Commit message file created in {commit_message_file}, please write a commit message and try again.")
        sys.exit(0)

    with open(commit_message_file, 'r') as file:
        lines = file.readlines()

    # Filter out lines that are not part of the commit message
    lines = [line for line in lines if "<!--Title-->" not in line and "<!--Description-->" not in line]
        
    title = lines[0].strip()
    if not title:
        print("Commit title is empty. Please write a commit with title and try again.")
        sys.exit(1)
    description = "\n".join(line.strip() for line in lines[2:])  # A partir de la tercera línea

    commit_message = title + "\n\n" + description
        
    if not has_commits(repo) or repo.is_dirty(working_tree=False):
        repo.index.commit(commit_message)
        
        # Clean the commit message file
        with open(commit_message_file, 'w') as file:
            file.write('<!--Title-->\n\n<!--Description-->\n\n')
        print("Changes committed.")
        
        # Check if -p or --push was passed
        if args.push:
            try:
                origin = repo.remote(name='origin')
                origin.push()
                print("Changes pushed.")
            except Exception as e:
                print(f"Failed to push changes: {e}\nPush changes manually.")

    else:
        print("There are no changes to commit.")
    sys.exit(0)