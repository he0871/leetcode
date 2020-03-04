#My tips: every sort problem can be transformed into hash_map and 
#using sort function provided by python itself which turns out to be 
#the fastest sort method.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #located the head of each list
        hash_map = {}
        
        for item in lists:
            temp = item;
            while(temp != None):
                hash_map[temp] = temp.val;
                temp = temp.next;
        if not bool(hash_map):
            return None;
        
        root = None;
        head = None;
        for elem in sorted(hash_map.items(), key=lambda item: item[1]):
            #print(elem[0].next);
            #print(head)
            if root == None:
                root =  elem[0];
                head = root;
            else:
                head.next = elem[0];
                head = elem[0];
        return root;
