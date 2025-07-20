public class ThreadDemo {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Thread started.");
                try {
                    Thread.sleep(5000); // Simulate a long-running task
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread finished.");
            }
        });
 Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Thread1 started.");
                try {
                    Thread.sleep(3000); // Simulate a long-running task
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread1 finished.");
            }
        });
        thread.start();
        thread1.start();
        System.out.println("Is thread alive? " + thread.isAlive());
        System.out.println("Is thread1 alive? " + thread1.isAlive());
        try {
            thread.join(); // Wait for the thread to finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Is thread alive? " + thread.isAlive());
        System.out.println("Is thread1 alive? " + thread1.isAlive());
    }
}
