from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_main():
    return """
    <html>
        <head>
            <title>Main Page</title>
        </head>
        <body>
            <h1>Welcome to the Main Page</h1>
            <p>This is the main page.</p>
            <a href="/subpage1">Go to Subpage 1</a><br>
            <a href="/subpage2">Go to Subpage 2</a>
        </body>
    </html>
    """

@app.get("/subpage1", response_class=HTMLResponse)
async def read_subpage1():
    return """
    <html>
        <head>
            <title>Subpage 1</title>
        </head>
        <body>
            <h1>Welcome to Subpage 1</h1>
            <p>This is subpage 1.</p>
            <a href="/">Go to Main Page</a><br>
            <a href="/subpage2">Go to Subpage 2</a>
        </body>
    </html>
    """

@app.get("/subpage2", response_class=HTMLResponse)
async def read_subpage2():
    return """
    <html>
        <head>
            <title>Subpage 2</title>
        </head>
        <body>
            <h1>Welcome to Subpage 2</h1>
            <p>This is subpage 2.</p>
            <a href="/">Go to Main Page</a><br>
            <a href="/subpage1">Go to Subpage 1</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8060)
