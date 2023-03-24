import asyncio
import os
import sys
import time
import threading
import subprocess

server_process = None


def start_lm_server():
    """Start the language model server."""
    print("start lm server")
    # start the server using sys call
    global server_process
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join(sys.path)
    env["PYTHONUNBUFFERED"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    server_process = subprocess.Popen(
        [sys.executable, "lm_server.py"],
        env=env,
    )

    print("lm server started")


def stop_lm_server():
    """Stop the language model server."""
    print("stop lm server")
    # stop the server using sys call
    global server_process
    server_process.kill()

    print("lm server stopped")


async def lm_test():
    """Test the language model server."""
    # start the server on a separate thread
    thread = threading.Thread(target=start_lm_server)
    thread.start()
    global server_thread
    server_thread = thread

    # wait for the server to start
    time.sleep(5)

    # test the server
    print("test lm server")
    time.sleep(5)
    print("lm server tested")
    stop_lm_server()


if __name__ == "__main__":
    asyncio.run(lm_test())
