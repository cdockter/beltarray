package io.belt.nav;

/**
 * Created by cdockter on 2/21/2015.
 */
public interface ICloseable extends AutoCloseable {
    @Override
    void close() throws RuntimeException;
}
