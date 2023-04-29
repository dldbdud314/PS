package programmers.List;

import java.util.*;

class MyData{
    int value;

    public MyData(int value){
        this.value = value;
    }

    static MyData create(int v){
        return new MyData(v);
    }

    @Override
    public String toString() {
        return "" + value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        MyData myData = (MyData) o;
        return value == myData.value;
    }

    @Override
    public int hashCode(){
        return Objects.hash(value);
    }
}

class Main{
    public static void main(String[] args) {
        List<MyData> list = new Vector<>();
        
        list.add(MyData.create(1));
        list.add(MyData.create(2));
        list.add(MyData.create(3));

        System.out.println(list);
        System.out.println(list.contains(MyData.create(2)));
        System.out.println(list.isEmpty());
        System.out.println(list.size());
    }
}

