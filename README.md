# data-structures

This repository holds sample code for a number of classic data structures implemented in Python.

### Includes

* Linked List  
* Stack
* Proper Parentheticals Challenge
    - Analyzes a unicode string to determine whether any parentheses in it are open, balanced, or broken
* Queue
* Doubly Linked List
    - The doubly linked list allows you to add and remove elements from both ends of the list. If you only need to implement a stack or queue, the singly linked list provides that functionality with less overhead. A doubly linked list might be used to cache visited sites in a browser allowing you to traverse your site history with back and forward buttons or to add and remove items from the top or bottom of a collection, like a deck of cards.
* Binary Heap
    - This binary max-heap sorts the data passed into it in descending order, such that the top value is the greatest and each parent value under it is greater than its children. Pushing a value into the heap will bubble it up until its parent is greater than it, while popping the top value off will resort the list to maintain descending order.
* Priority Queue
    - The priority queue sorts the data passed into it by priority in descending order. Items of equal priority are sorted by seniority. The priority queue supports insert, pop, and peek methods.
* Priority Queue with Heap
    - This implementation of the priority queue imports our binary heap module and passes tuples consisting of priority, seniority, and value into a heap. This implementation is adapted from the Python Cookbook example cited in the Resources section.

* Graph (unweighted, directed)
    -  As described from [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/) "Graphs are networks consisting of nodes connected by edges or arcs. In directed graphs, the connections between nodes have a direction, and are called arcs."
    - Graph Traversal
        - Graph traversal is explored in a [depth first](http://en.wikipedia.org/wiki/Depth-first_search) and [breadth first](http://en.wikipedia.org/wiki/Breadth-first_search) style.

## Resources
[Linked Lists Wiki](http://en.wikipedia.org/wiki/Linked_list)  
[Stack Wiki](http://en.wikipedia.org/wiki/Stack_(abstract_data_type))  
[Queue (data structure) from Princeton](http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html)
[Binary Heap Wiki](http://en.wikipedia.org/wiki/Binary_heap)  
[Binary Heap Visualization](http://www.comp.nus.edu.sg/~stevenha/visualization/heap.html)  
[Priority Queue Wiki](http://en.wikipedia.org/wiki/Priority_queue)  
[Implementing a Priority Queue from a Binary Heap](https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch01s05.html)  
[Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/)


Pytest - for testing structure functions

##Collaborators
Joel Stanner  
Henry Howes

Thanks to Mark Ableidinger for guidance on the Binary Heap implementation
