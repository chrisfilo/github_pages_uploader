# -*- coding: utf-8 -*-

"""Console script for github_pages_uploader."""
import sys
import click

from github_pages_uploader import upload_dir_to_github


@click.command()
@click.option('--in_dir', prompt=True)
@click.option('--username', prompt=True)
@click.option('--password', prompt='Password or authentication token')
@click.option('--repo_name', prompt='Name of the target repository (cannot be an existing repository)')
def main(in_dir, username, password, repo_name):
    upload_dir_to_github(in_dir, username, password, repo_name)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
