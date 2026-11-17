#include <iostream>
using namespace std;

#define SIZE 5

class CircularQueue {
    int arr[SIZE], front = -1, rear = -1;

public:
    void enqueue(int x) {
        if ((rear + 1) % SIZE == front)
            cout << "Queue Full\n";
        else {
            if (front == -1) front = 0;
            rear = (rear + 1) % SIZE;
            arr[rear] = x;
            cout << "Inserted: " << x << endl;
        }
    }

    void dequeue() {
        if (front == -1)
            cout << "Queue Empty\n";
        else {
            cout << "Deleted: " << arr[front] << endl;
            if (front == rear) front = rear = -1;
            else front = (front + 1) % SIZE;
        }
    }

    void display() {
        if (front == -1) cout << "Queue Empty\n";
        else {
            int i = front;
            do {
                cout << arr[i] << " ";
                i = (i + 1) % SIZE;
            } while (i != (rear + 1) % SIZE);
            cout << endl;
        }
    }
};

int main() {
    CircularQueue q;
    int ch, x;

    do {
        cout << "\n1.Enqueue 2.Dequeue 3.Display 4.Exit\n";
        cin >> ch;

        switch (ch) {
            case 1: cin >> x; q.enqueue(x); break;
            case 2: q.dequeue(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);

    return 0;
}
