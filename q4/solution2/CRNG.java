import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;

// Concurrent Random Number Generator
public class CRNG {
    public static AtomicBoolean init = new AtomicBoolean(true);
    // Using a synchronized List to ensure thread safety and consistent behaviour
    public static List<Integer> list = Collections.synchronizedList(new ArrayList<Integer>());

    public static class Numthread extends Thread {
        @Override
        public void run() {

            Random random = new Random();
            while (init.get()) {
                // list is a synchronised list and operations add and remove are thread-safe

                // Elements enter appended and leave from index 0
                list.add(random.nextInt(10) + 1);

                // Elements leave from the front as list.remove(index 0)
                if (list.size() >= 31) list.remove(0);
            }
        }
    }

    public static void main(String[] args) {
        // Number of threads
        int n_threads;
        Scanner scanner = new Scanner(System.in);
        // Handling input
        if (args.length == 0) {
            System.out.println("Give the program a number");
            n_threads = scanner.nextInt();


        } else {
            try {
                n_threads = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Args is not a number, Enter one now");
                n_threads = scanner.nextInt();
            }
        }

        // Base case of no threads to randomly generate numbers
        if (n_threads <= 0) {
            System.out.println("No numbers are generated from " + n_threads + " threads");
            return;
        } else {
            // Thread creation begins
            for (int i = 0; i < n_threads; i++) {
                Thread numthread = new Numthread();
                numthread.start();
            }

            System.out.println("Enter # to stop RNG threads and print results of last 30 RNG numbers");
            while (init.get()) {
                if (scanner.nextLine().equals("#")) {
                    init.set(false);
                }
            }

            int[] f_arr = new int[11];

            int freq = 0, count = 0, min = 11, max = 0, avg = 0;

            // iteration of list requires synchronisation
            synchronized (list) {
                for (int num : list) {
                    if (num > max) max = num;
                    if (num < min) min = num;
                    avg += num;
                    f_arr[num]++;
                }
                avg = avg / list.size();
            }

            System.out.println("min: " + min);
            System.out.println("max: " + max);
            System.out.println("avg: " + avg);

            for (int i = 1; i < f_arr.length; i++) {
                if (f_arr[i] > count) {
                    count = f_arr[i];
                    freq = i;
                }
            }
            System.out.println("freq: " + freq);
        }
    }
}

