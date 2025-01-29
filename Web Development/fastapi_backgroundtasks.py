"""
FastAPI does not natively support background tasks, but it provides integration with
libraries such as BackgroundTasks for simple tasks, and with Celery for more complex,
distributed task handling. BackgroundTasks allows tasks to run in the background without
blocking the response, which is useful for small, non-blocking operations that do not require
immediate results.
"""

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    message = f"notification sent to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Notification sent in the background"}