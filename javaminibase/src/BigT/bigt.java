package BigT;

import global.MID;

/**
 * Creating and maintaining all the relevant heap files and index files of your choice.
 */
public class bigt {
    /**
     * Initialize a bigtable.
     *
     * @param name a name of the bigtable
     * @param type an integer from 1 to 5 representing different clustering and indexing strategies.
     */
    public bigt(String name, int type) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Delete the bigtable from the database.
     */
    public void deleteBigt() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Return the number of maps in the bigtable.
     *
     * @return the number of maps
     */
    public int getMapCnt() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }


    /**
     * Return the number of distinct row labels in the bigtable.
     *
     * @return the number of distinct row labels
     */
    public int getRowCnt() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Return number of distinct column labels in the bigtable.
     *
     * @return the number of distinct column labels
     */
    public int getColumnCnt() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Insert map into the bigtable, return its MID. The method ensures that there are at most <strong>three</strong> maps
     * with the same row and column labels, but different timestamps, in the bigtable. When a fourth is inserted, the one
     * with the oldest label is dropped from the bigtable.
     *
     * @param mapPtr a map in bytes
     * @return the map ID
     */
    public MID insertMap(byte[] mapPtr) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Initialize a stream of maps where row label matching rowFilter, column label matching columnFilter, and value
     * label matching valueFilter. If any of the filter are null strings, then that filter is not considered
     * (e.g., if rowFilter is null, then all row labels are OK).
     * <p>
     * The orderType can be one of the following:
     * <ul>
     * <li>1, then results are first ordered in row label, then column label, then time stamp</li>
     * <li>2, then results are first ordered in column label, then row label, then time stamp</li>
     * <li>3, then results are first ordered in row label, then time stamp</li>
     * <li>4, then results are first ordered in column label, then time stamp</li>
     * <li>6, then results are ordered in time stamp</li>
     * </ul>
     *
     * @param orderType    an integer indicating how to order the results
     * @param rowFilter    a string matching row labels
     * @param columnFilter a string matching column labels
     * @param valueFilter  a string matching values
     * @return a Stream of maps
     */
    public Stream openStream(int orderType, String rowFilter, String columnFilter, String valueFilter) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }
}
