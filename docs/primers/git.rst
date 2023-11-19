Git Primer
==========

Why Use Git?
------------

Git is a widely-used distributed version control system that offers
numerous advantages for managing and collaborating on software projects.
Here are some reasons to use Git:

1. **Version control**: Git allows you to track changes in your code
   over time. You can easily revert to a previous version of your code
   if needed, making it safer to experiment and develop new features
   without losing work.

2. **Branching and merging**: Git supports branching and merging,
   allowing developers to work on different features or bug fixes
   simultaneously without affecting the main codebase. Once a feature or
   fix is complete and tested, it can be merged back into the main
   branch.

3. **Distributed system**: Git is a distributed version control system,
   which means every developer has a complete copy of the repository on
   their local machine. This allows for faster operations, as most
   actions can be performed locally without needing to communicate with
   a central server.

4. **Collaboration**: Git makes it easy for multiple developers to work
   on the same project. Changes can be pushed to a shared remote
   repository, allowing team members to review, comment on, and
   integrate each other's work.

5. **Conflict resolution**: Git provides tools to handle merge
   conflicts, helping developers resolve issues when multiple people
   have made changes to the same file. This allows for smoother
   collaboration and less time spent on resolving conflicts.

6. **Integration**: Many tools and platforms, such as GitHub, GitLab,
   and Bitbucket, are built around Git, offering additional features for
   project management, issue tracking, and continuous integration. Git
   also integrates with popular IDEs and text editors, making it easy to
   incorporate into your development workflow.

7. **Popularity**: Git is the most popular version control system, which
   means you're likely to encounter it in various projects and
   organizations. Being familiar with Git can be a valuable skill when
   collaborating with others or looking for job opportunities.

Overall, Git provides a powerful and flexible system for managing your
code, collaborating with others, and integrating with various tools and
platforms. Its widespread adoption and active development make it a
valuable tool for any software developer.

Terminology
-----------

1.  **Repository (repo)**: A collection of files and folders, including
    the entire version history, that is managed by Git.

2.  **Commit**: A snapshot of changes in the repository. Each commit has
    a unique identifier (hash) and includes metadata such as the author,
    timestamp, and a commit message describing the changes.

3.  **Branch**: A parallel version of the repository that diverges from
    the main working project. Branches are used to isolate changes for a
    feature or bug fix without affecting the main branch.

4.  **Main (master) branch**: The default branch in a repository, which
    contains the latest stable version of the project. It is often named
    master or main.

5.  **Clone**: Creating a local copy of a remote repository on your
    machine, including the entire commit history.

6.  **Fork**: Creating a personal copy of another user's repository on
    your GitHub account. This allows you to make changes and create pull
    requests without affecting the original repository.

7.  **Remote**: A reference to a remote repository, such as one hosted
    on GitHub. The default remote is usually called origin.

8.  **Fetch**: Retrieving updates from a remote repository, such as new
    commits or branches, without merging them into your local
    repository.

9.  **Pull**: Fetching updates from a remote repository and merging them
    into your local repository.

10. **Push**: Sending your local commits to a remote repository.

11. **Merge**: Combining changes from one branch into another. This can
    be done locally or via a pull request on platforms like GitHub.

12. **Pull request (PR)**: A request to merge changes from one branch
    into another on a remote repository, such as on GitHub. PRs allow
    for code review and collaboration before merging.

13. **Conflict**: A situation that occurs when changes in different
    branches conflict with each other. Conflicts need to be resolved
    manually before a merge can be completed.

14. **Staging area**: An intermediate area where changes are added
    before they are committed to the repository. The staging area allows
    you to selectively stage and commit changes.

15. **.gitignore**: A file that lists file patterns and directories to
    be ignored by Git when committing changes. This is useful for
    ignoring files that should not be tracked, such as temporary files,
    build artifacts, or sensitive data.

How to push your first commit
-----------------------------

1. Add the files that you changed. You can see all files that have
   changed by running:

.. code:: bash

   git status

Use ``git add`` to stage files

.. code:: bash

   git add <file_name>               # Stage a single file
   git add <file_name1> <file_name2> # Stage multiple files
   git add .                         # Stage all changes

2. Commit your changes.

.. code:: bash

   git commit -m "Your commit message"

3. Check the difference between your local and main to ensure you are
   pushing the correct changes.

.. code:: bash

   git diff

4. Push!

.. code:: bash

   git push 

Common Commands
---------------

1. **git init**: Initialize a new Git repository in the current
   directory.

.. code:: bash

   git init

2. **git clone**: Create a local copy of a remote repository.

.. code:: bash

   git clone <repository_url>

3. **git status**: Check the status of your working directory, including
   any changes made, files staged for commit, and files untracked by
   Git.

.. code:: bash

   git status

4. **git add**: Stage changes for the next commit. You can stage a
   single file, multiple files, or all changes in the working directory.

.. code:: bash

   git add <file_name>               # Stage a single file
   git add <file_name1> <file_name2> # Stage multiple files
   git add .                         # Stage all changes

5. **git commit**: Create a new commit with the staged changes and a
   descriptive commit message.

.. code:: bash

   git commit -m "Your commit message"

6. **git log**: View the commit history for the current branch.

.. code:: bash

   git log

7. **git diff**: Show the differences between the working directory and
   the latest commit.

.. code:: bash

   git diff

8. **git remote**: List remote repositories connected to your local
   repository.

.. code:: bash

   git remote -v

9. **git remote add**: Add a remote repository to your local repository.

.. code:: bash

   git remote add <remote_name> <repository_url>

10. **git fetch**: Download changes from a remote repository, but don't
    merge or update your local branch.

.. code:: bash

   git fetch <remote_name>

11. **git pull**: Download changes from a remote repository and merge
    them into your local branch.

.. code:: bash

   git pull <remote_name> <branch_name>

12. **git push**: Push your local changes to a remote repository.

.. code:: bash

   git push <remote_name> <branch_name>

13. **git branch**: List all branches in your local repository.

.. code:: bash

   git branch

14. **git checkout**: Switch to a different branch or commit.

.. code:: bash

   git checkout <branch_name> # Switch to a branch
   git checkout <commit_hash> # Switch to a specific commit

15. **git checkout -b**: Create a new branch and switch to it.

.. code:: bash

   git checkout -b <new_branch_name>

16. **git merge**: Merge changes from one branch into another.

.. code:: bash

   git merge <source_branch_name>

These basic Git commands will help you get started with version control
and enable you to collaborate effectively with other developers. As you
gain experience, you can explore more advanced Git features to further
enhance your workflow.

Best Practices
--------------

1. **Commit often and with meaningful messages**: Make frequent, small
   commits that represent a single logical change. Write clear and
   descriptive commit messages that explain the changes and their
   purpose. This makes it easier to track progress, identify issues, and
   understand the history of your project.

2. **Use branches**: Use branches to separate work on different
   features, bug fixes, or experiments. This keeps your main branch
   clean and stable, while allowing you to work on multiple tasks
   simultaneously without affecting each other.

3. **Keep a clean history**: Rebase or squash commits before merging
   branches to maintain a clean and linear commit history. This makes it
   easier to follow the project's history and identify changes that
   introduced bugs or issues.

4. **Review, test, and lint code before merging**: Use code reviews and
   pull requests to ensure that all changes are reviewed by at least one
   other team member before merging. This helps catch bugs, maintain
   code quality, and share knowledge within the team.

5. **Resolve conflicts promptly**: Address and resolve merge conflicts
   as soon as they arise. Keep communication open with your team members
   to prevent conflicts and ensure a smooth merging process. **DO NOT
   FORCE PUSH TO SOLVE A CONFLICT**

6. **Use .gitignore**: Create and maintain a .gitignore file to exclude
   unnecessary or sensitive files from your repository. This helps keep
   your repository clean and prevents accidental exposure of sensitive
   information.
