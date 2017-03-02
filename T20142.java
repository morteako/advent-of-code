class Addressable {
    int val;
    public String address;
    public Addressable next;
    public void printLabel(){System.out.println(address);}
}
class Person {
    public String name;
    public final Addressable addr = new Addressable (){
        public void printLabel(){
        System.out.println(name); // *1*
        super.printLabel();}
    };
    Person(String pname,String paddress) {
    name = pname; addr.address = paddress; }
}
class Company {
    public int orgNumber;
    public final Addressable addr = new Addressable(){
        public void printLabel(){
        System.out.println(orgNumber); // *2*
        super.printLabel(); }
    };
    Company (int porgNumber, String paddress) {
    orgNumber = porgNumber; addr.address = paddress; }
}
class T20142 {
    public static void main(String[] args) {
        Addressable a;
        // a simple list:
        Person birger = new Person("birger","Røahagan 33A");
        Company psykVirk = new Company(123,"Røahagan 33A");
        birger.addr.next = psykVirk.addr;
        a=birger.addr;
        while (a != null) {
        a.printLabel();
        System.out.println(a.val);
        a = a.next;
        }
    }
}