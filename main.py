import typer
from utils import read_file

app = typer.Typer()
       
@app.command()
def health():
    print("Hello, world!")

@app.command()
def quest():
    from InquirerPy import prompt

    questions = [
        # {"type": "input", "message": "What's your name:", "name": "name"},
        {
            "type": "list",
            "message": "What word book are you choosing?",
            "choices": ["N1", "N2", "N3", "N4", "N5"]
        }
        # {"type": "confirm", "message": "Confirm?"}
    ]
    result = prompt(questions)
    book_name = result[0]
    read_file('words/{}.csv'.format(book_name.lower()))

if __name__ == "__main__":
    app()