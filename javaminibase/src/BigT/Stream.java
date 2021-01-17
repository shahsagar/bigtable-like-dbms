package BigT;

import global.MID;

/**
 * Working as an interface for retrieving maps from big tables.
 * <p>
 * This class acts like {@link heap.Scan} in the original Minibase.
 * <p>
 * TODO: Please refer {@link heap.Scan} to see how to implement this class.
 */
public class Stream {
    /**
     * Initialize a stream of maps on the given bigtable.
     *
     * @param bigtable     a bigtable where to build a stream on
     * @param orderType    how to order the results. See {@link BigT.bigt#openStream(int, String, String, String)}
     * @param rowFilter    a filter to match row labels
     * @param columnFilter a filter to match column labels
     * @param valueFilter  a filter to match values
     */
    public Stream(bigt bigtable, int orderType, int rowFilter, String columnFilter, String valueFilter) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Close the stream object.
     */
    public void closestream() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Retrieve the next map in the open stream.
     *
     * @param mid the map ID of the map to retrieve
     * @return the retrieved map
     */
    public Map getNext(MID mid) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }
}
