package io.belt.nav;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothSocket;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.belt.nav.dto.Instruction;

import java.io.IOException;
import java.util.UUID;

/**
 * Created by cdockter on 2/21/2015.
 */
public class BluetoothBeltApi implements IBeltApi {

    private final BluetoothAdapter _adapter;
    private final UUID _appId;
    private final ObjectMapper _serializer;
    private final BluetoothSocket _socket;

    public BluetoothBeltApi(final UUID appId, final BluetoothSocket socket) {
        this(BluetoothAdapter.getDefaultAdapter(), appId, new ObjectMapper(), socket);
    }

    public BluetoothBeltApi(final BluetoothAdapter adapter, final UUID appId, final ObjectMapper serializer, final BluetoothSocket socket) {
        _adapter = adapter;
        _appId = appId;
        _serializer = serializer;
        _socket = socket;
    }

    public void sendInstructions(final String instruction) throws IOException {
        if(!_socket.isConnected()) {
            _socket.connect();
        }

        _socket.getOutputStream().write((instruction + "\0").getBytes("UTF-8"));
    }

    //TODO: Need to move this code out into the activity or maybe a factory class
//    public static int REQUEST_ENABLE_BT = 10000;
//    public boolean connect(Activity activity) throws IOException {
//        if (!_adapter.isEnabled()) {
//            Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
//            activity.startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
//        }
//        _socket = _adapter.getRemoteDevice("").createInsecureRfcommSocketToServiceRecord(_appId);
//        return true;
//    }

    @Override
    public void vibrate(final double radiansFromNorth, final double radiansOfArch, final double durationInMS) throws IOException {
        final Instruction instruction = new Instruction(radiansFromNorth, radiansOfArch, durationInMS);
        final String jsonString = _serializer.writeValueAsString(instruction);
        sendInstructions(jsonString);
    }

    @Override
    public void stop() throws IOException {
        vibrate(0,0,0);
    }

    @Override
    public void close() throws RuntimeException {
        try {
            if(_socket.isConnected()) {
                stop();
            }
            _socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
