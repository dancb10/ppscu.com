package com.example.game;
import java.util.List;

import java.util.ArrayList;

public interface ISavable {

    List<String> write();
    void read(List<String> savedValues);
}
