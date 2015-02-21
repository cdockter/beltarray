package io.belt.nav;

/**
 * Created by cdockter on 2/21/2015.
 */
public interface IBeltApi {
    void vibrate(double radiansFromNorth, double radiansOfArch, double durationInMS);
    void stop();
}
