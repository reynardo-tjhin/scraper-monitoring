import asyncio
import time
import threading

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

def block_reading(i: int, filename: str, shared_event: threading.Event) -> None:
    with open(filename, "r") as f:
        for line in f.readlines():
            print(c[i] + f"{filename}: {line}", end="")
        while not shared_event.is_set():
            line = f.readline()
            if (line):
                print(c[i] + f"{filename}: {line}", end="")

async def main(shared_event: threading.Event):

    print(f"started main at {time.strftime('%X')}")
    await asyncio.gather(
        *[asyncio.to_thread(block_reading, 0, f".test_files/test{i+5}.txt", shared_event) for i in range(100)],
        asyncio.to_thread(block_reading, 1, ".test_files/test.txt", shared_event),
        asyncio.to_thread(block_reading, 2, ".test_files/test1.txt", shared_event),
    )
    
if (__name__ == "__main__"):

    shared_event = threading.Event()

    try:
        asyncio.run(main(shared_event))
    except KeyboardInterrupt:
        shared_event.set()
        print(c[0] + f"finished main at {time.strftime('%X')}")
        print(c[0] + "Keyboard Interrupted! Ending this program!")
