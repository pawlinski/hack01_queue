# main.py

class QueueItem:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __repr__(self):
        return f"{self.name} has priority {self.priority}"

def main():
    jacek = QueueItem("Jacek", 3)
    grzegorz = QueueItem("Grzegorz", 0)
    alina = QueueItem("Alina", 5)
    marta = QueueItem("Marta", 2)
    marek = QueueItem("Marek", 4)
    zbyszek = QueueItem("Zbyszek", 1)
    
    queue = [jacek, grzegorz, alina, marta, marek]
    print(f"Queue: {queue}")
    
    # Add element to the end of the queue
    queue.append(zbyszek)
    print(f"After adding Zbyszek: {queue}")
    
    # Pop and print the first element with the highest priority
    firstItem = queue[0]
    for item in queue:
        if item.priority > firstItem.priority:
            firstItem = item
    print(f"Popped item with the highest priority: {queue.pop(queue.index(firstItem)).name}")
    print(f"After popping: {queue}")
    
    # Peek at the first element with the highest priority without removing
    firstItem = queue[0]
    for item in queue:
        if item.priority > firstItem.priority:
            firstItem = item
    print(f"Peek at the first element with the highest priority: {queue[0].name}")
    
    # Check if the queue is empty
    if queue:
        print("Queue is not empty")
    else:
        print("Queue is empty")
    
    # Get the number of elements in the queue
    print(f"Queue has {len(queue)} elements")

if __name__ == "__main__":
    main()