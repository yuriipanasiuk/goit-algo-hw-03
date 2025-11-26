from queue import Queue
import uuid
import time

queue = Queue()


def generate_request():
    """Creates a new request and adds it to the queue"""
    request = uuid.uuid4()
    queue.put(request)
    print(f"Generated request: {request}")


def process_request():
    """Processes a request from the queue, if one exists"""
    if not queue.empty():
        request = queue.get()
        print(f"Processed request: {request}")
    else:
        print("Queue is empty")


if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
        time.sleep(1)
