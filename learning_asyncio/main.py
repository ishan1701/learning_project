import asyncio


# Simulate a download task (async)
async def download_file(file_id):
    print(f"Starting download for file {file_id}...")
    await asyncio.sleep(50)  # Simulate download delay
    print(f"Download complete for file {file_id}")
    return f"File {file_id} content"


# Simulate logging activity (async)
async def log_activity():
    for i in range(5):
        print(f"Logging activity {i + 1}...")
        await asyncio.sleep(6)  # Simulate doing some other work


# A non-async function that runs synchronously after log_task
def sync_function():
    print("Sync function started.")
    # Simulate some work that completes after async tasks
    for i in range(2):
        print(f"Sync function is working... {i + 1}")
    print("Sync function completed.")


# Main function to run both async tasks and the sync function
async def main():
    # Start the download task concurrently (simulated)
    log_task = asyncio.create_task(log_activity())
    download_task = asyncio.create_task(download_file(1))

    # Wait for the log task to finish
    await log_task
    print("Logging completed.")

    print("between log and download")

    download_result = await download_task
    print(f"Download result: {download_result}")

    # Call the synchronous function after awaiting the log task
    sync_function()


#
#
# SO in the above example,
# 1. The `log_activity` function put on the event loop and runs concurrently.
# 2. The `download_file` function is also put on the event loop and runs concurrently.
# 3. The `sync_function` runs only after the `log_activity` function and `download_file` function are completed.
# 4. ""between log and download"" is printed after the log task completes. It can be possible that the download task is also completed by then.

# Below is the expected output:
# (learning-project-py3.10) ➜  learning_asyncio git:(main) ✗ poetry run  python main.py
# Logging activity 1...
# Starting download for file 1...
# Logging activity 2...
# Logging activity 3...
# Logging activity 4...
# Logging activity 5...
# Logging completed.
# between log and download
# Download complete for file 1
# Download result: File 1 content
# Sync function started.
# Sync function is working... 1
# Sync function is working... 2
# Sync function completed.


if __name__ == "__main__":
    asyncio.run(main())
