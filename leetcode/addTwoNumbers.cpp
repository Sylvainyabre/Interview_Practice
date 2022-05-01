/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int carry = 0;
        ListNode *curr1 = l1;
        ListNode *curr2 = l2;
        ListNode *result = nullptr;
        ListNode *end = result;
        while (curr1 || curr2)
        {
            if (curr1 && curr2)
            {
                int data1 = curr1->val;
                int data2 = curr2->val;
                int sum = data1 + data2 + carry;
                if (sum >= 10)
                {
                    int rem = sum % 10;
                    if (end)
                    {
                        ListNode *newNode = new ListNode(rem, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(rem, nullptr);
                        end = result;
                    }
                    carry = 1;
                }
                else
                { // sum is less than 10
                    if (result)
                    {
                        ListNode *newNode = new ListNode(sum, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(sum, nullptr);
                        end = result;
                    }
                    carry = 0;
                }
                curr1 = curr1->next;
                curr2 = curr2->next;
            }
            else if (!curr1 && curr2)
            {
                int data2 = curr2->val;
                int sum = data2 + carry;
                if (sum >= 10)
                {
                    int rem = sum % 10;
                    if (result)
                    {
                        ListNode *newNode = new ListNode(rem, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(rem, nullptr);
                        end = result;
                    }
                    carry = 1;
                }
                else
                {
                    if (result)
                    {
                        ListNode *newNode = new ListNode(sum, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(sum, nullptr);
                        end = result;
                    }
                    carry = 0;
                }
                curr2 = curr2->next;
            }
            else
            {
                int data1 = curr1->val;
                int sum = data1 + carry;
                if (sum >= 10)
                {
                    int rem = sum % 10;
                    if (result)
                    {
                        ListNode *newNode = new ListNode(rem, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(rem, nullptr);
                        end = result;
                    }
                    carry = 1;
                }
                else
                {
                    if (result)
                    {
                        ListNode *newNode = new ListNode(sum, nullptr);
                        end->next = newNode;
                        end = newNode;
                    }
                    else
                    {
                        result = new ListNode(sum, nullptr);
                        end = result;
                    }
                    carry = 0;
                }
                curr1 = curr1->next;
            }
        }
        if (!curr1 && !curr2)
        {
            if (carry)
            {
                end->next = new ListNode(carry, nullptr);
                carry = 0;
            }
        }
        return result;
    }
};