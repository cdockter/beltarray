package io.belt.nav;

import com.fasterxml.jackson.core.JsonGenerationException;

import java.io.IOException;

/**
 * API for interacting with the belt communication device.
 */
public interface IBeltApi extends ICloseable {
    /**
     * Start the belt vibrating in the indicated direction for the specified duration.
     * @param radiansFromNorth radians left of north in which the belt should indicate.
     * @param radiansOfArch an arch with with its mid point centered on the radiansFromNorth which should be include in the indication.
     *                      This provides the ability to have a fine or bord direction indication.
     * @param durationInMS duration in milliseconds the indication should last.
     * @throws IOException
     */
    void vibrate(double radiansFromNorth, double radiansOfArch, double durationInMS) throws IOException;

    /**
     * Stops any current indication the device is communicating.
     * @throws IOException
     */
    void stop() throws IOException;
}
