import click

@click.group()
def stuff():
    pass

@stuff.command()
def main():
    print("my program")
