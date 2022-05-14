from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
import sys


class Profile(object):

    def __init__(self, values_datas, values_repos):
        self.values_datas = values_datas
        self.values_repos = values_repos

    def get_datas(self, datas):
        print(datas['login'])
        print(datas['name'])
        print(datas['bio'])
        print(datas['company'])
        print(datas['blog'])
        print(datas['location'])

    def get_repos(self, repos):
        for repo in repos:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Name Repository")
            table.add_column("Language")
            table.add_column("Forks")
            table.add_column("Stars")

            table.add_row(
                repo['name'],
                repo['language'],
                str(repo['forks_count']),
                str(repo['stargazers_count'])
            )

            console = Console()
            console.print(table)

    def exist_application(self):
        option_exist = input("Do you really want to exit the system? y/n: ")

        if option_exist == "y":
            sys.exit()

    def process_data(self):
        for _ in track(range(100), description='[green]Processing data'):
            sleep(0.02)

    def run_app(self):
        while True:
            print("-----------------------------------------------")

            print("1 - My datas")
            print("2 - Repositories")
            print("3 - Exist")

            print("-----------------------------------------------")

            option = input("Choose an option: ")

            if option == "1":
                self.process_data()
                self.get_datas(self.values_datas)
            elif option == "2":
                self.process_data()
                self.get_repos(self.values_repos)
            elif option == "3":
                self.exist_application()
            else:
                print("This option does not exist")
