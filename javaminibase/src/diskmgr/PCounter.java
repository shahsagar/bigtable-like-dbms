package diskmgr;

/**
 * For counting the number of reads and writes in the bigtable DB.
 *
 * TODO: Include methods in this class into read_page() and write_page() of the {@link diskmgr}.
 */
public class PCounter {
    public static int rcounter;
    public static int wcounter;

    /**
     * Initialize the counter.
     */
    public static void initialize() {
        rcounter = wcounter = 0;
    }

    /**
     * Increase the "read" counter by one.
     */
    public static void readIncrement() {
        ++rcounter;
    }

    /**
     * Increase the "write" counter by one.
     */
    public static void writeIncrement() {
        ++wcounter;
    }
}
