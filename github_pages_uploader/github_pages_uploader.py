# -*- coding: utf-8 -*-

import os
from shutil import rmtree
from github import Github
from dulwich.porcelain import init, branch_create, add, commit, open_repo, push


def create_github_repo(repo_name, username, password):
    g = Github(username, password)
    me = g.get_user()
    me.create_repo(repo_name)


def prepare_local_dir(in_dir):
    init(in_dir)
    add(in_dir, in_dir)
    commit(in_dir, "adding files")
    branch_create(in_dir, 'gh-pages')

    r = open_repo(in_dir)
    r.reset_index(r[b"refs/heads/gh-pages"].tree)
    r.refs.set_symbolic_ref(b"HEAD", b"refs/heads/gh-pages")


def clean_up_local_dir(in_dir):
    rmtree(os.path.join(in_dir, '.git'))


def push_to_github(in_dir, username, password, repo_name):
    push(in_dir,
         "https://{username}:{password}@github.com/{username}/{repo_name}".format(username=username,
                                                                                  password=password,
                                                                                  repo_name=repo_name),
         b"gh-pages")


def upload_dir_to_github(in_dir, username, password, repo_name):
    create_github_repo(repo_name, username, password)
    try:
        prepare_local_dir(in_dir)
        push_to_github(in_dir, username, password, repo_name)
    finally:
        clean_up_local_dir(in_dir)
