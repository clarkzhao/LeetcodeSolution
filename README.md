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
|448|[Find All Numbers Disappeared in an Array](#find-all-numbers-disappeared-in-an-array)| Array|Easy|[Python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/Find_All_Numbers_Disappeared_in_an_Array.py)|
|283|[Move Zeroes](#move-zeroes)|Array, Two pointers|Easy|[python](https://github.com/clarkzhao/LeetcodeSolution/blob/master/src/move_zeros.py)
## Notes
### Two Sum
* Compared to brute force solution, the use of **hash_map** (**Dictionary** in python) is more efficient.
*  **hash_map[residual]** is returned at first, because the expected result is in ascending order.

### Two Summ II
* Take the advantage of the ascending order of the input array.
* The least complexity is O(N) using two pointer
* [Binary search](https://discuss.leetcode.com/topic/21800/python-different-solutions-two-pointer-dictionary-binary-search/2) has a complexity of O(N*log(N))

### Find All Numbers Disappeared in an Array
* Take the advantage of using the value of one array as the index for an array.
* [One solution](https://discuss.leetcode.com/topic/65738/java-accepted-simple-solution) marks the value by taking negative of them, and get the value by taking absolute of them, and it saves extra spaces than my solution.
* [Another solution](https://discuss.leetcode.com/topic/66063/5-line-java-easy-understanding/2) tries to solve similar problem but using concept of remainder.

### Move zeroes
* At first, I misunderstand the question. I thought the requirements is to put all the zeros in front of the arrays. That's Why I have the last line in first solution
* [The second solution](https://discuss.leetcode.com/topic/29902/1ms-java-solution) and [similar solution](https://discuss.leetcode.com/topic/32632/a-95-26-beat-rate-solution/4) puts my solution to shame. The reason is that I use **insert** method of python **List** and so less efficient.
