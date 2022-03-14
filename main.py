import typer

app = typer.Typer()


@app.command()
def hello(name: str, dumb: bool = True):
    print(f"Hello {name}")
    if dumb:
        print('Dumb!')


@app.command()
def goodbye():
    print("Bye!")


if __name__ == "__main__":
    app()
