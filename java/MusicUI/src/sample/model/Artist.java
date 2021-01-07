package sample.model;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;

public class Artist {

    private SimpleIntegerProperty id;
    private SimpleStringProperty name;

    public int getId() {
        return id.get();
    }

    public void setId(int id) {
        this.id.set(id);
    }

    public String getName() {
        return name.get();
    }

    public Artist() {
        this.id = new SimpleIntegerProperty();
        this.name = new SimpleStringProperty();
    }

    public void setName(String name) {
        this.name.set(name);
    }
}
