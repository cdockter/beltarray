package io.belt.nav.dto;

/**
* Created by cdockter on 2/21/2015.
*/
public class Instruction {
    public double radiansFromNorth;
    public double radiansOfArch;
    public double durationInMS;

    public Instruction(final double radiansFromNorth, final double radiansOfArch, final double durationInMS) {
        this.radiansFromNorth = radiansFromNorth;
        this.radiansOfArch = radiansOfArch;
        this.durationInMS = durationInMS;
    }
}
