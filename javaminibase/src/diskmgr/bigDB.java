package diskmgr;

/**
 * Creating and maintaining all the relevant files and btree based index files to organize the data.
 * <p>
 * TODO: This class acts like {@link diskmgr.DB} and should replicate the existing methods in that class.
 */
public class bigDB {
    /**
     * Construct a new bigtable DB. This method accepts the following types:
     * <p>
     * Type 1: No index
     * <p>
     * Type 2: one btree to index row labels
     * <p>
     * Type 3: one btree to index column labels
     * <p>
     * Type 4:
     * one btree to index column label and row label (combined key) and one btree to index timestamps
     * <p>
     * Type 5: one btree to index row label and value (combined key) and one btree to index timestamps
     *
     * @param type an integer denoting the different clustering and indexing strategies you will use for the graph database.
     */
    public bigDB(int type) {
        throw new UnsupportedOperationException("Not implemented yet.");
    }
}
