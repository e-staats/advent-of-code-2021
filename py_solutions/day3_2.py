class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def populate_linked_list(prevNode, line):
    prevNode.next = Node(str(line))
    return prevNode.next


with open("../inputs/day3.txt", "r") as file:
    lines = file.readlines()


def this_whole_process(most_common):
    head = Node(0)
    prev_node = head
    for i in range(len(lines)):
        prev_node = populate_linked_list(prev_node, lines[i])

    filt = list(range(12))
    for i in range(12):
        count = 0
        count2 = 0
        # count up the bit values of the remaining numbers
        node = head
        node = node.next
        while node != None:
            bit = node.value[i]
            count2 += 1
            if bit == "0":
                count -= 1
            else:
                count += 1
            node = node.next

        # set the filter bit accordingly
        if most_common == 1:
            if count < 0:
                filt[i] = "0"
            else:
                filt[i] = "1"
        else:
            if count >= 0:
                filt[i] = "0"
            else:
                filt[i] = "1"
        # filter the list whose values aren't the most common
        node = head
        while node != None:
            if node.next == None:
                break
            bit = node.next.value[i]
            if bit != filt[i]:
                try:
                    node.next = node.next.next
                except:
                    node.next = None
                    break
            else:
                node = node.next

        # counting for troubleshooting
        node = head
        node = node.next
        ts_count = 0
        while node != None:
            ts_count += 1
            node = node.next
        if ts_count == 1:
            decimal_val = int(head.next.value, 2)
            return decimal_val


val1 = this_whole_process(1)
val2 = this_whole_process(0)
print(val1 * val2)
