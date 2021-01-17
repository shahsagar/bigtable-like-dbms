package BigT;

/**
 * The fundamental storage unit in BigTable which replaces "tuples" in relational Java Minibase. A map follows the format:
 * <p>
 * {@literal (row : string, column : string, time : int) → string }.
 * <p>
 * This data type works like {@link heap.Tuple} in the relational Minibase.
 */
public class Map {
    /**
     * Create a new map with an appropriate size.
     */
    public Map() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Create a map from bytes.
     *
     * @param amap   a byte array containing the map
     * @param offset the offset of the map in the byte array
     */
    public Map(byte[] amap, int offset) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Create a map from another map.
     *
     * @param fromMap another map
     */
    public Map(Map fromMap) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Return the row label in the map.
     *
     * @return a row label
     */
    public String getRowLabel() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Return the column label in the map.
     *
     * @return a column label
     */
    public String getColumnLabel() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Return the value in the map.
     *
     * @return a value
     */
    public String getValue() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Set the row label.
     *
     * @param val a value to set
     * @return the map itself
     */
    public Map setRowLabel(String val) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Set the column label.
     *
     * @param val a value to set
     * @return the map itself
     */
    public Map setColumnLabel(String val) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Set the value.
     *
     * @param val a value to set
     * @return the map itself
     */
    public Map setValue(String val) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Print out the map.
     */
    public void print() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }


    /**
     * Get the size of the map.
     * @return the size of the map.
     */
    public int size() {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Copy the given map.
     * @param fromMap the map to copy
     */
    public void mapCopy(Map fromMap) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Initialize the map. (if you don't want to use the constructor).
     *
     * @param amap a byte array containing the map
     * @param offset the offset of the map in the byte array
     */
    public void mapInit(byte[] amap, int offset) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }

    /**
     * Set the map with the given byte array and offset.
     * @param frommap a byte array containing the map
     * @param offset the offset of the map in the byte array
     */
    public void mapSet(byte[] frommap, int offset) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }
}
