// Definition for singly-linked list.
  public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }

public class Question21 {
    public static void main(String[] args){
        Console.WriteLine(MergeTwoLists);
    }


    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode testNode = new ListNode();
        ListNode result = testNode;

        while (list1 != null && list2 != null){
            if (list1.val <= list2.val){
                result.next = list1; 
                list1 = list1.next;
            } 
            else {
                result.next = list2; 
                list2 = list2.next;
            }
            result = result.next;
        }

        while (list1 != null){ // could probably use if statements, too lazy atm
            result.next = list1;
            list1 = list1.next;
            result = result.next;
        } 
        while (list2 != null){
            result.next = list2;
            list2 = list2.next;
            result = result.next;
        } 

        return testNode.next;
    }
}

