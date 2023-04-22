import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.web.app:create_app", factory=True, reload=True)
