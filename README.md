# LeetcodeSolution

This solution is written in Python at first.

- [x] python

- [ ] C++

- [ ] Java


## Menu

| Squence | Name of Problem| Tags | Level	| Language  |
|:-------:|:--------------|:------:|:------:|:---------:|
|1|[Two Sum](#two-sum)| Array, Hash Table|Easy|[Python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/two_sum.py)|
|167|[Two Sum II - input array is sorted](#two-sum-ii)|Array, Two pointer, Binary Search|Medium|[Python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/two_sum_II.py)|
|238|[Product of Array Except Self](product-of-array-except-self)|Array|Medium|[python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/product_of_array_except_self.py)|
|283|[Move Zeroes](#move-zeroes)|Array, Two pointers|Easy|[python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/move_zeros.py)|
|442|[Find All Duplicates in an Array](#find-all-duplicates-in-an-array)|Array|Medium|[python]((https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/find_all_duplicates_in_an_array.py)|
|448|[Find All Numbers Disappeared in an Array](#find-all-numbers-disappeared-in-an-array)| Array|Easy|[Python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/find_All_numbers_disappeared_in_an_array.py)|

## Notes
### Two Sum
* Compared to brute force solution, the use of **hash_map** (**Dictionary** in python) is more efficient.
*  **hash_map[residual]** is returned at first, because the expected result is in ascending order.

### Two Summ II
* Take the advantage of the ascending order of the input array.
* The least complexity is O(N) using two pointer
* [Binary search](https://discuss.leetcode.com/topic/21800/python-different-solutions-two-pointer-dictionary-binary-search/2) has a complexity of O(N*log(N))

### Product of Array Except Self
* It is easy to know by intuition, we cannot finish this task within one for loop.
* For example, assuming the input is [1,2,3,4]:

|iteration  | output[0]|output[1]|output[2]|output[3]|
|:-------|:--------|:-------|:-------|:------|
|0| x1|x1|x1|x1|
|1|x2|x1|x2|x2|
|2|x3|x3|x1|x3|
|3|x4|x4|x4|x1|
|output|24|12|8|6|

* Notice that, output[i] is multiplied by 1 for iteration 1
* For the first loop, we get the information in the upper right of above table that is [1, 1x1, 1x2, 1x2x3] which is [1, 1, 2, 6]
* For the second loop, we get the information in the lower left of above table that is [4x3x2, 4x3, 4, 1] which is [24, 12, 4, 1]
* The results is just the product of the items in the two list.

### Move zeroes
* At first, I misunderstand the question. I thought the requirements is to put all the zeros in front of the arrays. That's Why I have the last line in first solution
* [The second solution](https://discuss.leetcode.com/topic/29902/1ms-java-solution) and [similar solution](https://discuss.leetcode.com/topic/32632/a-95-26-beat-rate-solution/4) puts my solution to shame. The reason is that I use **insert** method of python **List** and so less efficient.

### Find All Duplicates in an Array
* This is question similar to Question 448. My solution use extra O(n) spaces, while [this solution](https://discuss.leetcode.com/topic/64735/java-simple-solution) use the tricks that the absolute value of the one value and its negativity are the same to avoid using extra spaces.

### Find All Numbers Disappeared in an Array
* Take the advantage of using the value of one array as the index for an array.
* [One solution](https://discuss.leetcode.com/topic/65738/java-accepted-simple-solution) marks the value by taking negative of them, and get the value by taking absolute of them, and it saves extra spaces than my solution.
* [Another solution](https://discuss.leetcode.com/topic/66063/5-line-java-easy-understanding/2) tries to solve similar problem but using concept of remainder.
