import asyncio


# Simulate a download task (async)
async def download_file(file_id):
    print(f"Starting download for file {file_id}...")
    await asyncio.sleep(30)  # Simulate download delay
    print(f"Download complete for file {file_id}")
    return f"File {file_id} content"


# Simulate logging activity (async)
async def log_activity():
    for i in range(2):
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
    download_task = asyncio.create_task(download_file(1))
    log_task = asyncio.create_task(log_activity())

    # Wait for the log task to finish
    await log_task
    print("Logging completed.")


    download_result = await download_task
    print(download_result)

    # Call the synchronous function after awaiting the log task
    sync_function()


if __name__ == '__main__':


    asyncio.run(main())
