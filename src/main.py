import argparse
from . import commit

def main():
    parser = argparse.ArgumentParser(description="PyGit tool")
    subparsers = parser.add_subparsers(dest="subcommand", help="Subcommands")

    commit_parser = subparsers.add_parser('commit', help='Commit a from commit_message.md')
    commit_parser.add_argument('-p', '--push', action='store_true', help='Push after committing')
    commit_parser.set_defaults(func=commit.main)

    # Parse the arguments
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()