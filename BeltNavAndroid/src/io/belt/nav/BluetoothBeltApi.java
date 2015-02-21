package io.belt.nav;

import android.bluetooth.BluetoothAdapter;

/**
 * Created by cdockter on 2/21/2015.
 */
public class BluetoothBeltApi implements IBeltApi {

    private final BluetoothAdapter _adapter;

    public BluetoothBeltApi() {
        this(BluetoothAdapter.getDefaultAdapter());
    }

    public BluetoothBeltApi(final BluetoothAdapter adapter) {
        _adapter = adapter;
    }

    @Override
    public void vibrate(final double radiansFromNorth, final double radiansOfArch, final double durationInMS) {

    }

    @Override
    public void stop() {

    }
}
