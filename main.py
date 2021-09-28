import uvicorn
from dotenv import load_dotenv
from src import create_app

app = create_app()

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        app="main:app",
        workers=1,
    )
