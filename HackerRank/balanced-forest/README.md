# Balanced Forest

Greg has a tree of nodes containing integer data. He wants to insert a node with some zero or positive integer value somewhere into the tree. His goal is to be able to cut two edges and have the values of each of the three new trees sum to the same amount. This is called a balanced forest. Being frugal, the data value he inserts should be minimal. Determine the minimal amount that a new node can have to allow creation of a balanced forest. If it's not possible to create a balanced forest, return -1.

## Input

The first line contains a single integer, `q`, the number of queries.

Each of the following `q` sets of lines is as follows:
* The first line contains an integer, `n`, the number of nodes in the tree.
* The second line contains `n` space-separated integers describing the respective values of `c[1], c[2], ..., c[n]`, where each `c[i]` denotes the value at node `i`.
* Each of the following `n - 1` lines contains two space-separated integers, `x[j]` and `y[j]`, describing edge `j` connecting nodes `x[j]` and `y[j]`. `x[j]` and `y[j]` can be parent or child.

### Constraints

* `1 <= q <= 5`
* `1 <= n <= 5 * 10^4`
* `1 <= c[i] <= 10^9`

## Output

For each query, return the minimum value of the integer `c[w]`. If no such value exists, return `-1` instead.

## Example

### Input

```
2
5
1 2 2 1 1
1 2
1 3
3 5
1 4
3
1 3 5
1 3
1 2
```

### Output

```
2
-1
```

## Analysis

There are some cases identified.

### Cases

**Description:** Two independent subtrees with the same cumulative value
**Solution:** Keep track of visited cumulative values

```
   (1)
  /   \
(2)   (2)*
```

**Description:** Visiting the subtree that should be discarded first
**Solution:** Based on the complement of the discarded subtree define the valid subtree (complement/2) and review this list when visiting a valid subtree

```
   (2)
  /   \
(1)   (2)*
```

**Description:** Visiting the subtree that should be discarded after the valid subtree
**Solution:** Based on the complement of the discarded subtree define the valid subtree (complement/2) and review if you already visited valid subtree

```
   (2)
  /   \
(2)   (1)*
```

**Description:** Chained subtrees having the discarded subtree at the beginning
**Solution:** Keep track of the parents cummulative values, and verify if there is a parent with cummulative value equals to 2X current cummulative value

```
   (1)
    |
   (2)
    |
   (2)*
```

**Description:** Chained subtrees having the discarded subtree at the middle
**Solution:** Keep track of the parents complement values, and verify if there is a parent with complement value equals to current cummulative value

```
   (2)
    |
   (1)
    |
   (2)*
```

**Description:** Chained subtrees having the discarded subtree at the end
**Solution:** Based on the complement of the discarded subtree define the valid subtree (complement/2) and review parents cummulative values equals to complement/2 + current cumulative value

```
   (2)
    |
   (2)
    |
   (1)*
```

### Big O

**`O(n)`**
