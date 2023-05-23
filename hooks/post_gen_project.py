import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'remote', 'add', 'origin', '{{cookiecutter.module_git_repo}}'])
