from fastapi import FastAPI



# Import FastAPI.
# Create an app instance.
# Write a path operation decorator using decorators like @app.get("/").
# Define a path operation function; for example, def root(): ....
# Run the development server using the command fastapi dev.


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello_world"}