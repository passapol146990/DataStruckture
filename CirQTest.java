class CirQTest{
    public static void main(String[] args){
        CircilarQ q = new CircilarQ(5);
        int v = 0;
        q.clearQ();
        q.enQ(10);
        q.enQ(5);
        q.enQ(20);
        q.printQ();
        q.enQ(30);
        v = q.deQ();
        q.printQ();
        q.enQ(50);
        q.printQ();
        v = q.deQ();
        q.printQ();
        v = q.deQ();
        q.printQ();
    }
}
class CircilarQ{
    private int size;
    private int CirQ[];
    private int f,r;
    public CircilarQ(int max){
        this.size = max;
        CirQ = new int[max];
    }
    public void clearQ(){
        f = r = 0;
    }
    public boolean isFull(){
        if(f==(r+1)%size){
            return true;
        }else{
            return false;
        }
    }
    public boolean isEmpty(){
        if(f==-1){
            return true;
        }else{
            return false;
        }
    }
    public void enQ(int value){
        if(isFull()){
            System.out.println("Queue is Full");
        }else{
            if(isEmpty()){
                f = r=0;
            }else{
                r = (r+1)%size;
            }
            CirQ[r] = value;
        }
    }
    public int deQ(){
        int value = 0;
        if(isEmpty()){
            System.out.println("Queue is Empty");
        }else{
            value = CirQ[f];
            if(f==r){
                f=r=-1;
            }else{
                f = (f+1)%size;
            }
        }
        return value;
    }
    public void printQ(){
        int i=0;
        if(isEmpty()){
            System.out.println("Queue is Empty");
        }else if(f<=r){
            for(i=f;i<=r;i++){
                System.out.print(CirQ[i]+" ");
            }
        }else{
            for(i=f;i<size;i++){
                System.out.print(CirQ[i]+" ");
            }
            for(i=0;i<=r;i++){
                System.out.print(CirQ[i]+" ");
            }
        }
        System.out.println();
    }
}