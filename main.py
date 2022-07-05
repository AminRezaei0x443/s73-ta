import uvicorn
from fastapi import FastAPI
from app import app

def main():
    uvicorn.run(app, host="0.0.0.0", port=8118, log_level="info")


if __name__ == "__main__":
    main()
