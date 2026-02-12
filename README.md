
# Leet-Code-Solutions

This repository contains my solutions to LeetCode problems, implemented in Python.

## Problem Tree

```mermaid
graph TD
    Root[LeetCode Solutions]
    Root --> Cat0(Arrays & Hashing)
    Root --> Cat1(Strings)
    Root --> Cat2(Math)
    Root --> Cat3(Linked List)
    Root --> Cat4(Trees)
    Root --> Cat5(Graphs)
    Root --> Cat6(Dynamic Programming)
    Root --> Cat7(Backtracking)
    Root --> Cat8(Binary Search & Sorting)
    Root --> Cat9(Database)
    Root --> Cat10(Shell)
    Root --> Cat11(Others)
    Cat4 -.-> Cat5
    Cat7 -.-> Cat4
    Cat7 -.-> Cat6
    Cat8 --> Cat0
    Cat1 -.-> Cat0
    Cat0 --> P1["﻿1. Two Sum"]
    Cat0 --> P15["15. 3Sum"]
    Cat0 --> P152["152. Maximum Product Subarray"]
    Cat0 --> P16["16. 3Sum Closest"]
    Cat0 --> P170["170. Two Sum III - Data structure design"]
    Cat0 --> P18["18. 4Sum"]
    Cat0 --> P189["189. Rotate Array"]
    Cat0 --> P1975["1975. Maximum Matrix Sum"]
    Cat0 --> P209["209. Minimum Size Subarray Sum"]
    Cat0 --> P215["215. Kth Largest Element in an Array"]
    Cat0 --> P217["217. Contains Duplicate"]
    Cat0 --> P219["219. Contains Duplicate II"]
    Cat0 --> P220["220. Contains Duplicate III"]
    Cat0 --> P228["228. Summary Ranges"]
    Cat0 --> P238["238. Product of Array Except Self"]
    Cat0 --> P311["311. Sparse Matrix Multiplication"]
    Cat0 --> P316["316. Remove Duplicate Letters"]
    Cat0 --> P327["327. Count of Range Sum"]
    Cat0 --> P330["330. Patching Array"]
    Cat0 --> P3379["3379. Transformed Array"]
    Cat0 --> P349["349. Intersection of Two Arrays"]
    Cat0 --> P350["350. Intersection of Two Arrays II"]
    Cat0 --> P352["352. Data Stream as Disjoint Intervals"]
    Cat0 --> P3640["3640. Trionic Array II"]
    Cat0 --> P3719["3719. Longest Balanced Subarray I"]
    Cat0 --> P3721["3721. Longest Balanced Subarray II"]
    Cat0 --> P384["384. Shuffle an Array"]
    Cat0 --> P404["404. Sum of Left Leaves"]
    Cat0 --> P410["410. Split Array Largest Sum"]
    Cat0 --> P435["435. Non-overlapping Intervals"]
    Cat0 --> P453["453. Minimum Moves to Equal Array Elements"]
    Cat0 --> P454["454. 4Sum II"]
    Cat0 --> P457["457. Circular Array Loop"]
    Cat0 --> P462["462. Minimum Moves to Equal Array Elements II"]
    Cat0 --> P54["54. Spiral Matrix"]
    Cat0 --> P56["56. Merge Intervals"]
    Cat0 --> P59["59. Spiral Matrix II"]
    Cat0 --> P73["73. Set Matrix Zeroes"]
    Cat0 --> P961["961. N-Repeated Element in Size 2N Array"]
    Cat1 --> P125["125. Valid Palindrome"]
    Cat1 --> P126["126. Word Ladder II"]
    Cat1 --> P127["127. Word Ladder"]
    Cat1 --> P131["131. Palindrome Partitioning"]
    Cat1 --> P132["132. Palindrome Partitioning II"]
    Cat1 --> P139["139. Word Break"]
    Cat1 --> P14["14. Longest Common Prefix"]
    Cat1 --> P140["140. Word Break II"]
    Cat1 --> P151["151. Reverse Words in a String"]
    Cat1 --> P20["20. Valid Parentheses"]
    Cat1 --> P205["205. Isomorphic Strings"]
    Cat1 --> P211["211. Design Add and Search Words Data Structure"]
    Cat1 --> P212["212. Word Search II"]
    Cat1 --> P214["214. Shortest Palindrome"]
    Cat1 --> P242["242. Valid Anagram"]
    Cat1 --> P273["273. Integer to English Words"]
    Cat1 --> P28["28. Find the Index of the First Occurrence in a String"]
    Cat1 --> P290["290. Word Pattern"]
    Cat1 --> P2977["2977. Minimum Cost to Convert String II"]
    Cat1 --> P301["301. Remove Invalid Parentheses"]
    Cat1 --> P318["318. Maximum Product of Word Lengths"]
    Cat1 --> P32["32. Longest Valid Parentheses"]
    Cat1 --> P336["336. Palindrome Pairs"]
    Cat1 --> P344["344. Reverse String"]
    Cat1 --> P345["345. Reverse Vowels of a String"]
    Cat1 --> P387["387. First Unique Character in a String"]
    Cat1 --> P394["394. Decode String"]
    Cat1 --> P409["409. Longest Palindrome"]
    Cat1 --> P415["415. Add Strings"]
    Cat1 --> P420["420. Strong Password Checker"]
    Cat1 --> P43["43. Multiply Strings"]
    Cat1 --> P434["434. Number of Segments in a String"]
    Cat1 --> P438["438. Find All Anagrams in a String"]
    Cat1 --> P443["443. String Compression"]
    Cat1 --> P472["472. Concatenated Words"]
    Cat1 --> P479["479. Largest Palindrome Product"]
    Cat1 --> P481["481. Magical String"]
    Cat1 --> P49["49. Group Anagrams"]
    Cat1 --> P58["58. Length of Last Word"]
    Cat1 --> P68["68. Text Justification"]
    Cat1 --> P79["79. Word Search"]
    Cat1 --> P8["8. String to Integer atoi"]
    Cat1 --> P87["87. Scramble String"]
    Cat1 --> P9["9. Palindrome Number"]
    Cat1 --> P97["97. Interleaving String"]
    Cat1 --> P3713["3713. Longest Balanced Substring I"]
    Cat2 --> P12["12. Integer to Roman"]
    Cat2 --> P129["129. Sum Root to Leaf Numbers"]
    Cat2 --> P13["13. Roman to Integer"]
    Cat2 --> P136["136. Single Number"]
    Cat2 --> P137["137. Single Number II"]
    Cat2 --> P165["165. Compare Version Numbers"]
    Cat2 --> P166["166. Fraction to Recurring Decimal"]
    Cat2 --> P171["171. Excel Sheet Column Number"]
    Cat2 --> P179["179. Largest Number"]
    Cat2 --> P180["180. Consecutive Numbers"]
    Cat2 --> P191["191. Number of 1 Bits"]
    Cat2 --> P2["2. Add Two Numbers"]
    Cat2 --> P200["200. Number of Islands"]
    Cat2 --> P201["201. Bitwise AND of Numbers Range"]
    Cat2 --> P202["202. Happy Number"]
    Cat2 --> P223["223. Rectangle Area"]
    Cat2 --> P224["224. Basic Calculator"]
    Cat2 --> P227["227. Basic Calculator II"]
    Cat2 --> P231["231. Power of Two"]
    Cat2 --> P233["233. Number of Digit One"]
    Cat2 --> P258["258. Add Digits"]
    Cat2 --> P260["260. Single Number III"]
    Cat2 --> P263["263. Ugly Number"]
    Cat2 --> P264["264. Ugly Number II"]
    Cat2 --> P268["268. Missing Number"]
    Cat2 --> P279["279. Perfect Squares"]
    Cat2 --> P287["287. Find the Duplicate Number"]
    Cat2 --> P29["29. Divide Two Integers"]
    Cat2 --> P3013["3013. Divide an Array Into Subarrays With Minimum Cost II"]
    Cat2 --> P302["302. Smallest Rectangle Enclosing Black Pixels"]
    Cat2 --> P305["305. Number of Islands II"]
    Cat2 --> P306["306. Additive Number"]
    Cat2 --> P313["313. Super Ugly Number"]
    Cat2 --> P315["315. Count of Smaller Numbers After Self"]
    Cat2 --> P321["321. Create Maximum Number"]
    Cat2 --> P326["326. Power of Three"]
    Cat2 --> P342["342. Power of Four"]
    Cat2 --> P343["343. Integer Break"]
    Cat2 --> P357["357. Count Numbers with Unique Digits"]
    Cat2 --> P363["363. Max Sum of Rectangle No Larger Than K"]
    Cat2 --> P367["367. Valid Perfect Square"]
    Cat2 --> P371["371. Sum of Two Integers"]
    Cat2 --> P372["372. Super Pow"]
    Cat2 --> P374["374. Guess Number Higher or Lower"]
    Cat2 --> P375["375. Guess Number Higher or Lower II"]
    Cat2 --> P386["386. Lexicographical Numbers"]
    Cat2 --> P391["391. Perfect Rectangle"]
    Cat2 --> P397["397. Integer Replacement"]
    Cat2 --> P400["400. Nth Digit"]
    Cat2 --> P402["402. Remove K Digits"]
    Cat2 --> P405["405. Convert a Number to Hexadecimal"]
    Cat2 --> P414["414. Third Maximum Number"]
    Cat2 --> P421["421. Maximum XOR of Two Numbers in an Array"]
    Cat2 --> P423["423. Reconstruct Original Digits from English"]
    Cat2 --> P445["445. Add Two Numbers II"]
    Cat2 --> P447["447. Number of Boomerangs"]
    Cat2 --> P448["448. Find All Numbers Disappeared in an Array"]
    Cat2 --> P452["452. Minimum Number of Arrows to Burst Balloons"]
    Cat2 --> P476["476. Number Complement"]
    Cat2 --> P50["50. Powx, n"]
    Cat2 --> P65["65. Valid Number"]
    Cat2 --> P69["69. Sqrtx"]
    Cat2 --> P7["7. Reverse Integer"]
    Cat2 --> P84["84. Largest Rectangle in Histogram"]
    Cat2 --> P85["85. Maximal Rectangle"]
    Cat3 --> P138["138. Copy List with Random Pointer"]
    Cat3 --> P141["141. Linked List Cycle"]
    Cat3 --> P142["142. Linked List Cycle II"]
    Cat3 --> P147["147. Insertion Sort List"]
    Cat3 --> P148["148. Sort List"]
    Cat3 --> P160["160. Intersection of Two Linked Lists"]
    Cat3 --> P203["203. Remove Linked List Elements"]
    Cat3 --> P206["206. Reverse Linked List"]
    Cat3 --> P21["21. Merge Two Sorted Lists"]
    Cat3 --> P23["23. Merge k Sorted Lists"]
    Cat3 --> P234["234. Palindrome Linked List"]
    Cat3 --> P237["237. Delete Node in a Linked List"]
    Cat3 --> P328["328. Odd Even Linked List"]
    Cat3 --> P341["341. Flatten Nested List Iterator"]
    Cat3 --> P382["382. Linked List Random Node"]
    Cat3 --> P430["430. Flatten a Multilevel Doubly Linked List"]
    Cat3 --> P61["61. Rotate List"]
    Cat3 --> P82["82. Remove Duplicates from Sorted List II"]
    Cat3 --> P83["83. Remove Duplicates from Sorted List"]
    Cat3 --> P86["86. Partition List"]
    Cat3 --> P92["92. Reverse Linked List II"]
    Cat4 --> P100["100. Same Tree"]
    Cat4 --> P101["101. Symmetric Tree"]
    Cat4 --> P104["104. Maximum Depth of Binary Tree"]
    Cat4 --> P108["108. Convert Sorted Array to Binary Search Tree"]
    Cat4 --> P109["109. Convert Sorted List to Binary Search Tree"]
    Cat4 --> P110["110. Balanced Binary Tree"]
    Cat4 --> P111["111-Minimum-Depth-of-Binary-Tree"]
    Cat4 --> P114["114-Flatten-Binary-Tree-to-Linked-List"]
    Cat4 --> P116["116-Populating-Next-Right-Pointers-in-Each-Node"]
    Cat4 --> P1161["1161. Maximum Level Sum of a Binary Tree"]
    Cat4 --> P117["117-Populating-Next-Right-Pointers-in-Each-Node-II"]
    Cat4 --> P124["124. Binary Tree Maximum Path Sum"]
    Cat4 --> P1339["1339. Maximum Product of Splitted Binary Tree"]
    Cat4 --> P1382["1382. Balance a Binary Search Tree"]
    Cat4 --> P173["173. Binary Search Tree Iterator"]
    Cat4 --> P19["19. Remove Nth Node From End of List"]
    Cat4 --> P199["199. Binary Tree Right Side View"]
    Cat4 --> P208["208. Implement Trie Prefix Tree"]
    Cat4 --> P222["222. Count Complete Tree Nodes"]
    Cat4 --> P226["226. Invert Binary Tree"]
    Cat4 --> P230["230. Kth Smallest Element in a BST"]
    Cat4 --> P235["235. Lowest Common Ancestor of a Binary Search Tree"]
    Cat4 --> P236["236. Lowest Common Ancestor of a Binary Tree"]
    Cat4 --> P24["24. Swap Nodes in Pairs"]
    Cat4 --> P25["25. Reverse Nodes in k-Group"]
    Cat4 --> P257["257. Binary Tree Paths"]
    Cat4 --> P297["297. Serialize and Deserialize Binary Tree"]
    Cat4 --> P3["3. Longest Substring Without Repeating Characters"]
    Cat4 --> P30["30. Substring with Concatenation of All Words"]
    Cat4 --> P310["310. Minimum Height Trees"]
    Cat4 --> P395["395. Longest Substring with At Least K Repeating Characters"]
    Cat4 --> P427["427. Construct Quad Tree"]
    Cat4 --> P449["449. Serialize and Deserialize BST"]
    Cat4 --> P450["450. Delete Node in a BST"]
    Cat4 --> P459["459. Repeated Substring Pattern"]
    Cat4 --> P467["467. Unique Substrings in Wraparound String"]
    Cat4 --> P5["5. Longest Palindromic Substring"]
    Cat4 --> P76["76. Minimum Window Substring"]
    Cat4 --> P95["95. Unique Binary Search Trees II"]
    Cat4 --> P96["96. Unique Binary Search Trees"]
    Cat4 --> P98["98. Validate Binary Search Tree"]
    Cat4 --> P99["99. Recover Binary Search Tree"]
    Cat5 --> P130["130. Surrounded Regions"]
    Cat5 --> P133["133. Clone Graph"]
    Cat5 --> P207["207. Course Schedule"]
    Cat5 --> P210["210. Course Schedule II"]
    Cat6 --> P112["112-Path-Sum"]
    Cat6 --> P113["113-Path-Sum-II"]
    Cat6 --> P115["115-Distinct-Subsequences"]
    Cat6 --> P118["118-Pascals-Triangle"]
    Cat6 --> P119["119-Pascals-Triangle-II"]
    Cat6 --> P120["120-Triangle"]
    Cat6 --> P121["121. Best Time to Buy and Sell Stock"]
    Cat6 --> P122["122. Best Time to Buy and Sell Stock II"]
    Cat6 --> P123["123. Best Time to Buy and Sell Stock III"]
    Cat6 --> P188["188. Best Time to Buy and Sell Stock IV"]
    Cat6 --> P198["198. House Robber"]
    Cat6 --> P213["213. House Robber II"]
    Cat6 --> P241["241. Different Ways to Add Parentheses"]
    Cat6 --> P300["300. Longest Increasing Subsequence"]
    Cat6 --> P309["309. Best Time to Buy and Sell Stock with Cooldown"]
    Cat6 --> P322["322. Coin Change"]
    Cat6 --> P329["329. Longest Increasing Path in a Matrix"]
    Cat6 --> P334["334. Increasing Triplet Subsequence"]
    Cat6 --> P337["337. House Robber III"]
    Cat6 --> P3650["3650. Minimum Cost Path with Edge Reversals"]
    Cat6 --> P376["376. Wiggle Subsequence"]
    Cat6 --> P388["388. Longest Absolute File Path"]
    Cat6 --> P392["392. Is Subsequence"]
    Cat6 --> P437["437. Path Sum III"]
    Cat6 --> P446["446. Arithmetic Slices II - Subsequence"]
    Cat6 --> P45["45. Jump Game II"]
    Cat6 --> P53["53. Maximum Subarray"]
    Cat6 --> P55["55. Jump Game"]
    Cat6 --> P62["62. Unique Paths"]
    Cat6 --> P63["63. Unique Paths II"]
    Cat6 --> P64["64. Minimum Path Sum"]
    Cat6 --> P71["71. Simplify Path"]
    Cat6 --> P72["72. Edit Distance"]
    Cat6 --> P91["91. Decode Ways"]
    Cat7 --> P216["216. Combination Sum III"]
    Cat7 --> P282["282. Expression Add Operators"]
    Cat7 --> P31["31. Next Permutation"]
    Cat7 --> P36["36. Valid Sudoku"]
    Cat7 --> P368["368. Largest Divisible Subset"]
    Cat7 --> P37["37. Sudoku Solver"]
    Cat7 --> P377["377. Combination Sum IV"]
    Cat7 --> P39["39. Combination Sum"]
    Cat7 --> P40["40. Combination Sum II"]
    Cat7 --> P416["416. Partition Equal Subset Sum"]
    Cat7 --> P46["46. Permutations"]
    Cat7 --> P47["47. Permutations II"]
    Cat7 --> P51["51. N-Queens"]
    Cat7 --> P52["52. N-Queens II"]
    Cat7 --> P60["60. Permutation Sequence"]
    Cat7 --> P77["77. Combinations"]
    Cat7 --> P78["78. Subsets"]
    Cat7 --> P90["90. Subsets II"]
    Cat8 --> P153["153. Find Minimum in Rotated Sorted Array"]
    Cat8 --> P154["154. Find Minimum in Rotated Sorted Array II"]
    Cat8 --> P162["162. Find Peak Element"]
    Cat8 --> P167["167. Two Sum II - Input Array Is Sorted"]
    Cat8 --> P240["240. Search a 2D Matrix II"]
    Cat8 --> P26["26. Remove Duplicates from Sorted Array"]
    Cat8 --> P278["278. First Bad Version"]
    Cat8 --> P295["295. Find Median from Data Stream"]
    Cat8 --> P324["324. Wiggle Sort II"]
    Cat8 --> P33["33. Search in Rotated Sorted Array"]
    Cat8 --> P34["34. Find First and Last Position of Element in Sorted Array"]
    Cat8 --> P35["35. Search Insert Position"]
    Cat8 --> P373["373. Find K Pairs with Smallest Sums"]
    Cat8 --> P378["378. Kth Smallest Element in a Sorted Matrix"]
    Cat8 --> P389["389. Find the Difference"]
    Cat8 --> P4["4. Median of Two Sorted Arrays"]
    Cat8 --> P401["401. Binary Watch"]
    Cat8 --> P436["436. Find Right Interval"]
    Cat8 --> P442["442. Find All Duplicates in an Array"]
    Cat8 --> P451["451. Sort Characters By Frequency"]
    Cat8 --> P480["480. Sliding Window Median"]
    Cat8 --> P67["67. Add Binary"]
    Cat8 --> P74["74. Search a 2D Matrix"]
    Cat8 --> P75["75. Sort Colors"]
    Cat8 --> P80["80. Remove Duplicates from Sorted Array II"]
    Cat8 --> P81["81. Search in Rotated Sorted Array II"]
    Cat8 --> P88["88. Merge Sorted Array"]
    Cat9 --> P102["102. Binary Tree Level Order Traversal"]
    Cat9 --> P103["103. Binary Tree Zigzag Level Order Traversal"]
    Cat9 --> P105["105. Construct Binary Tree from Preorder and Inorder Traversal"]
    Cat9 --> P106["106. Construct Binary Tree from Inorder and Postorder Traversal"]
    Cat9 --> P107["107. Binary Tree Level Order Traversal II"]
    Cat9 --> P143["143. Reorder List"]
    Cat9 --> P144["144. Binary Tree Preorder Traversal"]
    Cat9 --> P145["145. Binary Tree Postorder Traversal"]
    Cat9 --> P175["175. Combine Two Tables"]
    Cat9 --> P176["176. Second Highest Salary"]
    Cat9 --> P177["177. Nth Highest Salary"]
    Cat9 --> P181["181. Employees Earning More Than Their Managers"]
    Cat9 --> P182["182. Duplicate Emails"]
    Cat9 --> P183["183. Customers Who Never Order"]
    Cat9 --> P184["184. Department Highest Salary"]
    Cat9 --> P185["185. Department Top Three Salaries"]
    Cat9 --> P196["196. Delete Duplicate Emails"]
    Cat9 --> P262["262. Trips and Users"]
    Cat9 --> P303["303. Range Sum Query - Immutable"]
    Cat9 --> P304["304. Range Sum Query 2D - Immutable"]
    Cat9 --> P307["307. Range Sum Query - Mutable"]
    Cat9 --> P308["308. Range Sum Query 2D - Mutable"]
    Cat9 --> P314["314. Binary Tree Vertical Order Traversal"]
    Cat9 --> P331["331. Verify Preorder Serialization of a Binary Tree"]
    Cat9 --> P429["429. N-ary Tree Level Order Traversal"]
    Cat9 --> P440["440. K-th Smallest in Lexicographical Order"]
    Cat9 --> P94["94. Binary Tree Inorder Traversal"]
    Cat10 --> P17["17. Letter Combinations of a Phone Number"]
    Cat10 --> P192["192. Word Frequency"]
    Cat10 --> P193["193. Valid Phone Numbers"]
    Cat10 --> P194["194. Transpose File"]
    Cat10 --> P195["195. Tenth Line"]
    Cat11 --> P10["10. Regular Expression Matching"]
    Cat11 --> P11["11. Container With Most Water"]
    Cat11 --> P128["128. Longest Consecutive Sequence"]
    Cat11 --> P134["134. Gas Station"]
    Cat11 --> P135["135. Candy"]
    Cat11 --> P1390["1390. Four Divisors"]
    Cat11 --> P146["146. LRU Cache"]
    Cat11 --> P149["149. Max Points on a Line"]
    Cat11 --> P150["150. Evaluate Reverse Polish Notation"]
    Cat11 --> P155["155. Min Stack"]
    Cat11 --> P164["164. Maximum Gap"]
    Cat11 --> P168["168. Excel Sheet Column Title"]
    Cat11 --> P169["169. Majority Element"]
    Cat11 --> P172["172. Factorial Trailing Zeroes"]
    Cat11 --> P174["174. Dungeon Game"]
    Cat11 --> P178["178. Rank Scores"]
    Cat11 --> P187["187. Repeated DNA Sequences"]
    Cat11 --> P190["190. Reverse Bits"]
    Cat11 --> P197["197. Rising Temperature"]
    Cat11 --> P204["204. Count Primes"]
    Cat11 --> P218["218. The Skyline Problem"]
    Cat11 --> P22["22. Generate Parentheses"]
    Cat11 --> P221["221. Maximal Square"]
    Cat11 --> P225["225. Implement Stack using Queues"]
    Cat11 --> P229["229. Majority Element II"]
    Cat11 --> P232["232. Implement Queue using Stacks"]
    Cat11 --> P239["239. Sliding Window Maximum"]
    Cat11 --> P27["27. Remove Element"]
    Cat11 --> P274["274. H-Index"]
    Cat11 --> P275["275. H-Index II"]
    Cat11 --> P283["283. Move Zeroes"]
    Cat11 --> P284["284. Peeking Iterator"]
    Cat11 --> P289["289. Game of Life"]
    Cat11 --> P292["292. Nim Game"]
    Cat11 --> P299["299. Bulls and Cows"]
    Cat11 --> P312["312. Burst Balloons"]
    Cat11 --> P317["317. Shortest Distance from All Buildings"]
    Cat11 --> P319["319. Bulb Switcher"]
    Cat11 --> P320["320. Generalized Abbreviation"]
    Cat11 --> P332["332. Reconstruct Itinerary"]
    Cat11 --> P335["335. Self Crossing"]
    Cat11 --> P338["338. Counting Bits"]
    Cat11 --> P347["347. Top K Frequent Elements"]
    Cat11 --> P354["354. Russian Doll Envelopes"]
    Cat11 --> P355["355. Design Twitter"]
    Cat11 --> P365["365. Water and Jug Problem"]
    Cat11 --> P38["38. Count and Say"]
    Cat11 --> P383["383. Ransom Note"]
    Cat11 --> P385["385. Mini Parser"]
    Cat11 --> P390["390. Elimination Game"]
    Cat11 --> P393["393. UTF-8 Validation"]
    Cat11 --> P396["396. Rotate Function"]
    Cat11 --> P398["398. Random Pick Index"]
    Cat11 --> P399["399. Evaluate Division"]
    Cat11 --> P403["403. Frog Jump"]
    Cat11 --> P406["406. Queue Reconstruction by Height"]
    Cat11 --> P407["407. Trapping Rain Water II"]
    Cat11 --> P41["41. First Missing Positive"]
    Cat11 --> P412["412. Fizz Buzz"]
    Cat11 --> P413["413. Arithmetic Slices"]
    Cat11 --> P417["417. Pacific Atlantic Water Flow"]
    Cat11 --> P419["419. Battleships in a Board"]
    Cat11 --> P42["42. Trapping Rain Water"]
    Cat11 --> P424["424. Longest Repeating Character Replacement"]
    Cat11 --> P433["433. Minimum Genetic Mutation"]
    Cat11 --> P44["44. Wildcard Matching"]
    Cat11 --> P441["441. Arranging Coins"]
    Cat11 --> P455["455. Assign Cookies"]
    Cat11 --> P456["456. 132 Pattern"]
    Cat11 --> P458["458. Poor Pigs"]
    Cat11 --> P461["461. Hamming Distance"]
    Cat11 --> P463["463. Island Perimeter"]
    Cat11 --> P464["464. Can I Win"]
    Cat11 --> P466["466. Count The Repetitions"]
    Cat11 --> P468["468. Validate IP Address"]
    Cat11 --> P470["470. Implement Rand10 Using Rand7"]
    Cat11 --> P473["473. Matchsticks to Square"]
    Cat11 --> P474["474. Ones and Zeroes"]
    Cat11 --> P475["475. Heaters"]
    Cat11 --> P477["477. Total Hamming Distance"]
    Cat11 --> P478["478. Generate Random Point in a Circle"]
    Cat11 --> P48["48. Rotate Image"]
    Cat11 --> P482["482. License Key Formatting"]
    Cat11 --> P483["483. Smallest Good Base"]
    Cat11 --> P57["57. Insert Interval"]
    Cat11 --> P6["6. Zigzag Conversion"]
    Cat11 --> P66["66. Plus One"]
    Cat11 --> P70["70. Climbing Stairs"]
    Cat11 --> P89["89. Gray Code"]
    Cat11 --> P93["93. Restore IP Addresses"]```

## Solved Problems

- [1. Two Sum](./1.%20Two%20Sum)
- [2. Add Two Numbers](./2.%20Add%20Two%20Numbers)
- [3. Longest Substring Without Repeating Characters](./3.%20Longest%20Substring%20Without%20Repeating%20Characters)
- [4. Median of Two Sorted Arrays](./4.%20Median%20of%20Two%20Sorted%20Arrays)
- [5. Longest Palindromic Substring](./5.%20Longest%20Palindromic%20Substring)
- [6. Zigzag Conversion](./6.%20Zigzag%20Conversion)
- [7. Reverse Integer](./7.%20Reverse%20Integer)
- [8. String to Integer (atoi)](./8.%20String%20to%20Integer%20%28atoi%29)
- [9. Palindrome Number](./9.%20Palindrome%20Number)
- [10. Regular Expression Matching](./10.%20Regular%20Expression%20Matching)
- [11. Container With Most Water](./11.%20Container%20With%20Most%20Water)
- [12. Integer to Roman](./12.%20Integer%20to%20Roman)
- [13. Roman to Integer](./13.%20Roman%20to%20Integer)
- [14. Longest Common Prefix](./14.%20Longest%20Common%20Prefix)
- [15. 3Sum](./15.%203Sum)
- [16. 3Sum Closest](./16.%203Sum%20Closest)
- [17. Letter Combinations of a Phone Number](./17.%20Letter%20Combinations%20of%20a%20Phone%20Number)
- [18. 4Sum](./18.%204Sum)
- [19. Remove Nth Node From End of List](./19.%20Remove%20Nth%20Node%20From%20End%20of%20List)
- [20. Valid Parentheses](./20.%20Valid%20Parentheses)
- [21. Merge Two Sorted Lists](./21.%20Merge%20Two%20Sorted%20Lists)
- [22. Generate Parentheses](./22.%20Generate%20Parentheses)
- [23. Merge k Sorted Lists](./23.%20Merge%20k%20Sorted%20Lists)
- [24. Swap Nodes in Pairs](./24.%20Swap%20Nodes%20in%20Pairs)
- [25. Reverse Nodes in k-Group](./25.%20Reverse%20Nodes%20in%20k-Group)
- [26. Remove Duplicates from Sorted Array](./26.%20Remove%20Duplicates%20from%20Sorted%20Array)
- [27. Remove Element](./27.%20Remove%20Element)
- [28. Find the Index of the First Occurrence in a String](./28.%20Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String)
- [29. Divide Two Integers](./29.%20Divide%20Two%20Integers)
- [30. Substring with Concatenation of All Words](./30.%20Substring%20with%20Concatenation%20of%20All%20Words)
- [31. Next Permutation](./31.%20Next%20Permutation)
- [32. Longest Valid Parentheses](./32.%20Longest%20Valid%20Parentheses)
- [33. Search in Rotated Sorted Array](./33.%20Search%20in%20Rotated%20Sorted%20Array)
- [34. Find First and Last Position of Element in Sorted Array](./34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array)
- [35. Search Insert Position](./35.%20Search%20Insert%20Position)
- [36. Valid Sudoku](./36.%20Valid%20Sudoku)
- [37. Sudoku Solver](./37.%20Sudoku%20Solver)
- [38. Count and Say](./38.%20Count%20and%20Say)
- [39. Combination Sum](./39.%20Combination%20Sum)
- [40. Combination Sum II](./40.%20Combination%20Sum%20II)
- [41. First Missing Positive](./41.%20First%20Missing%20Positive)
- [42. Trapping Rain Water](./42.%20Trapping%20Rain%20Water)
- [43. Multiply Strings](./43.%20Multiply%20Strings)
- [44. Wildcard Matching](./44.%20Wildcard%20Matching)
- [45. Jump Game II](./45.%20Jump%20Game%20II)
- [46. Permutations](./46.%20Permutations)
- [47. Permutations II](./47.%20Permutations%20II)
- [48. Rotate Image](./48.%20Rotate%20Image)
- [49. Group Anagrams](./49.%20Group%20Anagrams)
- [50. Pow(x, n)](./50.%20Pow%28x%2C%20n%29)
- [51. N-Queens](./51.%20N-Queens)
- [52. N-Queens II](./52.%20N-Queens%20II)
- [53. Maximum Subarray](./53.%20Maximum%20Subarray)
- [54. Spiral Matrix](./54.%20Spiral%20Matrix)
- [55. Jump Game](./55.%20Jump%20Game)
- [56. Merge Intervals](./56.%20Merge%20Intervals)
- [57. Insert Interval](./57.%20Insert%20Interval)
- [58. Length of Last Word](./58.%20Length%20of%20Last%20Word)
- [59. Spiral Matrix II](./59.%20Spiral%20Matrix%20II)
- [60. Permutation Sequence](./60.%20Permutation%20Sequence)
- [61. Rotate List](./61.%20Rotate%20List)
- [62. Unique Paths](./62.%20Unique%20Paths)
- [63. Unique Paths II](./63.%20Unique%20Paths%20II)
- [64. Minimum Path Sum](./64.%20Minimum%20Path%20Sum)
- [65. Valid Number](./65.%20Valid%20Number)
- [66. Plus One](./66.%20Plus%20One)
- [67. Add Binary](./67.%20Add%20Binary)
- [68. Text Justification](./68.%20Text%20Justification)
- [69. Sqrt(x)](./69.%20Sqrt%28x%29)
- [70. Climbing Stairs](./70.%20Climbing%20Stairs)
- [71. Simplify Path](./71.%20Simplify%20Path)
- [72. Edit Distance](./72.%20Edit%20Distance)
- [73. Set Matrix Zeroes](./73.%20Set%20Matrix%20Zeroes)
- [74. Search a 2D Matrix](./74.%20Search%20a%202D%20Matrix)
- [75. Sort Colors](./75.%20Sort%20Colors)
- [76. Minimum Window Substring](./76.%20Minimum%20Window%20Substring)
- [77. Combinations](./77.%20Combinations)
- [78. Subsets](./78.%20Subsets)
- [79. Word Search](./79.%20Word%20Search)
- [80. Remove Duplicates from Sorted Array II](./80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II)
- [81. Search in Rotated Sorted Array II](./81.%20Search%20in%20Rotated%20Sorted%20Array%20II)
- [82. Remove Duplicates from Sorted List II](./82.%20Remove%20Duplicates%20from%20Sorted%20List%20II)
- [83. Remove Duplicates from Sorted List](./83.%20Remove%20Duplicates%20from%20Sorted%20List)
- [84. Largest Rectangle in Histogram](./84.%20Largest%20Rectangle%20in%20Histogram)
- [85. Maximal Rectangle](./85.%20Maximal%20Rectangle)
- [86. Partition List](./86.%20Partition%20List)
- [87. Scramble String](./87.%20Scramble%20String)
- [88. Merge Sorted Array](./88.%20Merge%20Sorted%20Array)
- [89. Gray Code](./89.%20Gray%20Code)
- [90. Subsets II](./90.%20Subsets%20II)
- [91. Decode Ways](./91.%20Decode%20Ways)
- [92. Reverse Linked List II](./92.%20Reverse%20Linked%20List%20II)
- [93. Restore IP Addresses](./93.%20Restore%20IP%20Addresses)
- [94. Binary Tree Inorder Traversal](./94.%20Binary%20Tree%20Inorder%20Traversal)
- [95. Unique Binary Search Trees II](./95.%20Unique%20Binary%20Search%20Trees%20II)
- [96. Unique Binary Search Trees](./96.%20Unique%20Binary%20Search%20Trees)
- [97. Interleaving String](./97.%20Interleaving%20String)
- [98. Validate Binary Search Tree](./98.%20Validate%20Binary%20Search%20Tree)
- [99. Recover Binary Search Tree](./99.%20Recover%20Binary%20Search%20Tree)
- [100. Same Tree](./100.%20Same%20Tree)
- [101. Symmetric Tree](./101.%20Symmetric%20Tree)
- [102. Binary Tree Level Order Traversal](./102.%20Binary%20Tree%20Level%20Order%20Traversal)
- [103. Binary Tree Zigzag Level Order Traversal](./103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal)
- [104. Maximum Depth of Binary Tree](./104.%20Maximum%20Depth%20of%20Binary%20Tree)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](./105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](./106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal)
- [107. Binary Tree Level Order Traversal II](./107.%20Binary%20Tree%20Level%20Order%20Traversal%20II)
- [108. Convert Sorted Array to Binary Search Tree](./108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree)
- [109. Convert Sorted List to Binary Search Tree](./109.%20Convert%20Sorted%20List%20to%20Binary%20Search%20Tree)
- [110. Balanced Binary Tree](./110.%20Balanced%20Binary%20Tree)
- [111. Minimum Depth of Binary Tree](./111-Minimum-Depth-of-Binary-Tree)
- [112. Path Sum](./112-Path-Sum)
- [113. Path Sum II](./113-Path-Sum-II)
- [114. Flatten Binary Tree to Linked List](./114-Flatten-Binary-Tree-to-Linked-List)
- [115. Distinct Subsequences](./115-Distinct-Subsequences)
- [116. Populating Next Right Pointers in Each Node](./116-Populating-Next-Right-Pointers-in-Each-Node)
- [117. Populating Next Right Pointers in Each Node II](./117-Populating-Next-Right-Pointers-in-Each-Node-II)
- [118. Pascal's Triangle](./118-Pascals-Triangle)
- [119. Pascal's Triangle II](./119-Pascals-Triangle-II)
- [120. Triangle](./120-Triangle)
- [121. Best Time to Buy and Sell Stock](./121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock)
- [122. Best Time to Buy and Sell Stock II](./122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II)
- [123. Best Time to Buy and Sell Stock III](./123.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20III)
- [124. Binary Tree Maximum Path Sum](./124.%20Binary%20Tree%20Maximum%20Path%20Sum)
- [125. Valid Palindrome](./125.%20Valid%20Palindrome)
- [126. Word Ladder II](./126.%20Word%20Ladder%20II)
- [127. Word Ladder](./127.%20Word%20Ladder)
- [128. Longest Consecutive Sequence](./128.%20Longest%20Consecutive%20Sequence)
- [129. Sum Root to Leaf Numbers](./129.%20Sum%20Root%20to%20Leaf%20Numbers)
- [130. Surrounded Regions](./130.%20Surrounded%20Regions)
- [131. Palindrome Partitioning](./131.%20Palindrome%20Partitioning)
- [132. Palindrome Partitioning II](./132.%20Palindrome%20Partitioning%20II)
- [133. Clone Graph](./133.%20Clone%20Graph)
- [134. Gas Station](./134.%20Gas%20Station)
- [135. Candy](./135.%20Candy)
- [136. Single Number](./136.%20Single%20Number)
- [137. Single Number II](./137.%20Single%20Number%20II)
- [138. Copy List with Random Pointer](./138.%20Copy%20List%20with%20Random%20Pointer)
- [139. Word Break](./139.%20Word%20Break)
- [140. Word Break II](./140.%20Word%20Break%20II)
- [141. Linked List Cycle](./141.%20Linked%20List%20Cycle)
- [142. Linked List Cycle II](./142.%20Linked%20List%20Cycle%20II)
- [143. Reorder List](./143.%20Reorder%20List)
- [144. Binary Tree Preorder Traversal](./144.%20Binary%20Tree%20Preorder%20Traversal)
- [145. Binary Tree Postorder Traversal](./145.%20Binary%20Tree%20Postorder%20Traversal)
- [146. LRU Cache](./146.%20LRU%20Cache)
- [147. Insertion Sort List](./147.%20Insertion%20Sort%20List)
- [148. Sort List](./148.%20Sort%20List)
- [149. Max Points on a Line](./149.%20Max%20Points%20on%20a%20Line)
- [150. Evaluate Reverse Polish Notation](./150.%20Evaluate%20Reverse%20Polish%20Notation)
- [151. Reverse Words in a String](./151.%20Reverse%20Words%20in%20a%20String)
- [152. Maximum Product Subarray](./152.%20Maximum%20Product%20Subarray)
- [153. Find Minimum in Rotated Sorted Array](./153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array)
- [154. Find Minimum in Rotated Sorted Array II](./154.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II)
- [155. Min Stack](./155.%20Min%20Stack)
- [160. Intersection of Two Linked Lists](./160.%20Intersection%20of%20Two%20Linked%20Lists)
- [162. Find Peak Element](./162.%20Find%20Peak%20Element)
- [164. Maximum Gap](./164.%20Maximum%20Gap)
- [165. Compare Version Numbers](./165.%20Compare%20Version%20Numbers)
- [166. Fraction to Recurring Decimal](./166.%20Fraction%20to%20Recurring%20Decimal)
- [167. Two Sum II - Input Array Is Sorted](./167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted)
- [168. Excel Sheet Column Title](./168.%20Excel%20Sheet%20Column%20Title)
- [169. Majority Element](./169.%20Majority%20Element)
- [170. Two Sum III - Data structure design](./170.%20Two%20Sum%20III%20-%20Data%20structure%20design)
- [171. Excel Sheet Column Number](./171.%20Excel%20Sheet%20Column%20Number)
- [172. Factorial Trailing Zeroes](./172.%20Factorial%20Trailing%20Zeroes)
- [173. Binary Search Tree Iterator](./173.%20Binary%20Search%20Tree%20Iterator)
- [174. Dungeon Game](./174.%20Dungeon%20Game)
- [175. Combine Two Tables](./175.%20Combine%20Two%20Tables)
- [176. Second Highest Salary](./176.%20Second%20Highest%20Salary)
- [177. Nth Highest Salary](./177.%20Nth%20Highest%20Salary)
- [178. Rank Scores](./178.%20Rank%20Scores)
- [179. Largest Number](./179.%20Largest%20Number)
- [180. Consecutive Numbers](./180.%20Consecutive%20Numbers)
- [181. Employees Earning More Than Their Managers](./181.%20Employees%20Earning%20More%20Than%20Their%20Managers)
- [182. Duplicate Emails](./182.%20Duplicate%20Emails)
- [183. Customers Who Never Order](./183.%20Customers%20Who%20Never%20Order)
- [184. Department Highest Salary](./184.%20Department%20Highest%20Salary)
- [185. Department Top Three Salaries](./185.%20Department%20Top%20Three%20Salaries)
- [187. Repeated DNA Sequences](./187.%20Repeated%20DNA%20Sequences)
- [188. Best Time to Buy and Sell Stock IV](./188.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV)
- [189. Rotate Array](./189.%20Rotate%20Array)
- [190. Reverse Bits](./190.%20Reverse%20Bits)
- [191. Number of 1 Bits](./191.%20Number%20of%201%20Bits)
- [192. Word Frequency](./192.%20Word%20Frequency)
- [193. Valid Phone Numbers](./193.%20Valid%20Phone%20Numbers)
- [194. Transpose File](./194.%20Transpose%20File)
- [195. Tenth Line](./195.%20Tenth%20Line)
- [196. Delete Duplicate Emails](./196.%20Delete%20Duplicate%20Emails)
- [197. Rising Temperature](./197.%20Rising%20Temperature)
- [198. House Robber](./198.%20House%20Robber)
- [199. Binary Tree Right Side View](./199.%20Binary%20Tree%20Right%20Side%20View)
- [200. Number of Islands](./200.%20Number%20of%20Islands)
- [201. Bitwise AND of Numbers Range](./201.%20Bitwise%20AND%20of%20Numbers%20Range)
- [202. Happy Number](./202.%20Happy%20Number)
- [203. Remove Linked List Elements](./203.%20Remove%20Linked%20List%20Elements)
- [204. Count Primes](./204.%20Count%20Primes)
- [205. Isomorphic Strings](./205.%20Isomorphic%20Strings)
- [206. Reverse Linked List](./206.%20Reverse%20Linked%20List)
- [207. Course Schedule](./207.%20Course%20Schedule)
- [208. Implement Trie (Prefix Tree)](./208.%20Implement%20Trie%20%28Prefix%20Tree%29)
- [209. Minimum Size Subarray Sum](./209.%20Minimum%20Size%20Subarray%20Sum)
- [210. Course Schedule II](./210.%20Course%20Schedule%20II)
- [211. Design Add and Search Words Data Structure](./211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure)
- [212. Word Search II](./212.%20Word%20Search%20II)
- [213. House Robber II](./213.%20House%20Robber%20II)
- [214. Shortest Palindrome](./214.%20Shortest%20Palindrome)
- [215. Kth Largest Element in an Array](./215.%20Kth%20Largest%20Element%20in%20an%20Array)
- [216. Combination Sum III](./216.%20Combination%20Sum%20III)
- [217. Contains Duplicate](./217.%20Contains%20Duplicate)
- [218. The Skyline Problem](./218.%20The%20Skyline%20Problem)
- [219. Contains Duplicate II](./219.%20Contains%20Duplicate%20II)
- [220. Contains Duplicate III](./220.%20Contains%20Duplicate%20III)
- [221. Maximal Square](./221.%20Maximal%20Square)
- [222. Count Complete Tree Nodes](./222.%20Count%20Complete%20Tree%20Nodes)
- [223. Rectangle Area](./223.%20Rectangle%20Area)
- [224. Basic Calculator](./224.%20Basic%20Calculator)
- [961. N-Repeated Element in Size 2N Array](./961.%20N-Repeated%20Element%20in%20Size%202N%20Array)
- [1161. Maximum Level Sum of a Binary Tree](./1161.%20Maximum%20Level%20Sum%20of%20a%20Binary%20Tree)
- [1339. Maximum Product of Splitted Binary Tree](./1339.%20Maximum%20Product%20of%20Splitted%20Binary%20Tree)
- [1382. Balance a Binary Search Tree](./1382.%20Balance%20a%20Binary%20Search%20Tree)
- [1390. Four Divisors](./1390.%20Four%20Divisors)
- [1975. Maximum Matrix Sum](./1975.%20Maximum%20Matrix%20Sum)
- [225. Implement Stack using Queues](./225.%20Implement%20Stack%20using%20Queues)
- [226. Invert Binary Tree](./226.%20Invert%20Binary%20Tree)
- [227. Basic Calculator II](./227.%20Basic%20Calculator%20II)
- [228. Summary Ranges](./228.%20Summary%20Ranges)
- [229. Majority Element II](./229.%20Majority%20Element%20II)
- [230. Kth Smallest Element in a BST](./230.%20Kth%20Smallest%20Element%20in%20a%20BST)
- [231. Power of Two](./231.%20Power%20of%20Two)
- [232. Implement Queue using Stacks](./232.%20Implement%20Queue%20using%20Stacks)
- [233. Number of Digit One](./233.%20Number%20of%20Digit%20One)
- [234. Palindrome Linked List](./234.%20Palindrome%20Linked%20List)
- [235. Lowest Common Ancestor of a Binary Search Tree](./235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree)
- [236. Lowest Common Ancestor of a Binary Tree](./236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree)
- [237. Delete Node in a Linked List](./237.%20Delete%20Node%20in%20a%20Linked%20List)
- [238. Product of Array Except Self](./238.%20Product%20of%20Array%20Except%20Self)
- [239. Sliding Window Maximum](./239.%20Sliding%20Window%20Maximum)
- [240. Search a 2D Matrix II](./240.%20Search%20a%202D%20Matrix%20II)
- [241. Different Ways to Add Parentheses](./241.%20Different%20Ways%20to%20Add%20Parentheses)
- [242. Valid Anagram](./242.%20Valid%20Anagram)
- [257. Binary Tree Paths](./257.%20Binary%20Tree%20Paths)
- [258. Add Digits](./258.%20Add%20Digits)
- [260. Single Number III](./260.%20Single%20Number%20III)
- [262. Trips and Users](./262.%20Trips%20and%20Users)
- [263. Ugly Number](./263.%20Ugly%20Number)
- [264. Ugly Number II](./264.%20Ugly%20Number%20II)
- [268. Missing Number](./268.%20Missing%20Number)
- [273. Integer to English Words](./273.%20Integer%20to%20English%20Words)
- [274. H-Index](./274.%20H-Index)
- [275. H-Index II](./275.%20H-Index%20II)
- [278. First Bad Version](./278.%20First%20Bad%20Version)
- [279. Perfect Squares](./279.%20Perfect%20Squares)
- [282. Expression Add Operators](./282.%20Expression%20Add%20Operators)
- [283. Move Zeroes](./283.%20Move%20Zeroes)
- [284. Peeking Iterator](./284.%20Peeking%20Iterator)
- [287. Find the Duplicate Number](./287.%20Find%20the%20Duplicate%20Number)
- [289. Game of Life](./289.%20Game%20of%20Life)
- [290. Word Pattern](./290.%20Word%20Pattern)
- [292. Nim Game](./292.%20Nim%20Game)
- [295. Find Median from Data Stream](./295.%20Find%20Median%20from%20Data%20Stream)
- [297. Serialize and Deserialize Binary Tree](./297.%20Serialize%20and%20Deserialize%20Binary%20Tree)
- [299. Bulls and Cows](./299.%20Bulls%20and%20Cows)
- [300. Longest Increasing Subsequence](./300.%20Longest%20Increasing%20Subsequence)
- [301. Remove Invalid Parentheses](./301.%20Remove%20Invalid%20Parentheses)
- [302. Smallest Rectangle Enclosing Black Pixels](./302.%20Smallest%20Rectangle%20Enclosing%20Black%20Pixels)
- [303. Range Sum Query - Immutable](./303.%20Range%20Sum%20Query%20-%20Immutable)
- [304. Range Sum Query 2D - Immutable](./304.%20Range%20Sum%20Query%202D%20-%20Immutable)
- [305. Number of Islands II](./305.%20Number%20of%20Islands%20II)
- [306. Additive Number](./306.%20Additive%20Number)
- [307. Range Sum Query - Mutable](./307.%20Range%20Sum%20Query%20-%20Mutable)
- [308. Range Sum Query 2D - Mutable](./308.%20Range%20Sum%20Query%202D%20-%20Mutable)
- [309. Best Time to Buy and Sell Stock with Cooldown](./309.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20with%20Cooldown)
- [310. Minimum Height Trees](./310.%20Minimum%20Height%20Trees)
- [311. Sparse Matrix Multiplication](./311.%20Sparse%20Matrix%20Multiplication)
- [312. Burst Balloons](./312.%20Burst%20Balloons)
- [313. Super Ugly Number](./313.%20Super%20Ugly%20Number)
- [314. Binary Tree Vertical Order Traversal](./314.%20Binary%20Tree%20Vertical%20Order%20Traversal)
- [315. Count of Smaller Numbers After Self](./315.%20Count%20of%20Smaller%20Numbers%20After%20Self)
- [316. Remove Duplicate Letters](./316.%20Remove%20Duplicate%20Letters)
- [317. Shortest Distance from All Buildings](./317.%20Shortest%20Distance%20from%20All%20Buildings)
- [318. Maximum Product of Word Lengths](./318.%20Maximum%20Product%20of%20Word%20Lengths)
- [319. Bulb Switcher](./319.%20Bulb%20Switcher)
- [320. Generalized Abbreviation](./320.%20Generalized%20Abbreviation)
- [321. Create Maximum Number](./321.%20Create%20Maximum%20Number)
- [322. Coin Change](./322.%20Coin%20Change)
- [324. Wiggle Sort II](./324.%20Wiggle%20Sort%20II)
- [326. Power of Three](./326.%20Power%20of%20Three)
- [327. Count of Range Sum](./327.%20Count%20of%20Range%20Sum)
- [328. Odd Even Linked List](./328.%20Odd%20Even%20Linked%20List)
- [329. Longest Increasing Path in a Matrix](./329.%20Longest%20Increasing%20Path%20in%20a%20Matrix)
- [330. Patching Array](./330.%20Patching%20Array)
- [331. Verify Preorder Serialization of a Binary Tree](./331.%20Verify%20Preorder%20Serialization%20of%20a%20Binary%20Tree)
- [332. Reconstruct Itinerary](./332.%20Reconstruct%20Itinerary)
- [334. Increasing Triplet Subsequence](./334.%20Increasing%20Triplet%20Subsequence)
- [335. Self Crossing](./335.%20Self%20Crossing)
- [336. Palindrome Pairs](./336.%20Palindrome%20Pairs)
- [337. House Robber III](./337.%20House%20Robber%20III)
- [338. Counting Bits](./338.%20Counting%20Bits)
- [341. Flatten Nested List Iterator](./341.%20Flatten%20Nested%20List%20Iterator)
- [342. Power of Four](./342.%20Power%20of%20Four)
- [343. Integer Break](./343.%20Integer%20Break)
- [344. Reverse String](./344.%20Reverse%20String)
- [345. Reverse Vowels of a String](./345.%20Reverse%20Vowels%20of%20a%20String)
- [347. Top K Frequent Elements](./347.%20Top%20K%20Frequent%20Elements)
- [349. Intersection of Two Arrays](./349.%20Intersection%20of%20Two%20Arrays)
- [350. Intersection of Two Arrays II](./350.%20Intersection%20of%20Two%20Arrays%20II)
- [352. Data Stream as Disjoint Intervals](./352.%20Data%20Stream%20as%20Disjoint%20Intervals)
- [354. Russian Doll Envelopes](./354.%20Russian%20Doll%20Envelopes)
- [355. Design Twitter](./355.%20Design%20Twitter)
- [357. Count Numbers with Unique Digits](./357.%20Count%20Numbers%20with%20Unique%20Digits)
- [363. Max Sum of Rectangle No Larger Than K](./363.%20Max%20Sum%20of%20Rectangle%20No%20Larger%20Than%20K)
- [365. Water and Jug Problem](./365.%20Water%20and%20Jug%20Problem)
- [367. Valid Perfect Square](./367.%20Valid%20Perfect%20Square)
- [368. Largest Divisible Subset](./368.%20Largest%20Divisible%20Subset)
- [371. Sum of Two Integers](./371.%20Sum%20of%20Two%20Integers)
- [372. Super Pow](./372.%20Super%20Pow)
- [373. Find K Pairs with Smallest Sums](./373.%20Find%20K%20Pairs%20with%20Smallest%20Sums)
- [374. Guess Number Higher or Lower](./374.%20Guess%20Number%20Higher%20or%20Lower)
- [375. Guess Number Higher or Lower II](./375.%20Guess%20Number%20Higher%20or%20Lower%20II)
- [376. Wiggle Subsequence](./376.%20Wiggle%20Subsequence)
- [377. Combination Sum IV](./377.%20Combination%20Sum%20IV)
- [378. Kth Smallest Element in a Sorted Matrix](./378.%20Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix)
- [382. Linked List Random Node](./382.%20Linked%20List%20Random%20Node)
- [383. Ransom Note](./383.%20Ransom%20Note)
- [384. Shuffle an Array](./384.%20Shuffle%20an%20Array)
- [385. Mini Parser](./385.%20Mini%20Parser)
- [386. Lexicographical Numbers](./386.%20Lexicographical%20Numbers)
- [387. First Unique Character in a String](./387.%20First%20Unique%20Character%20in%20a%20String)
- [388. Longest Absolute File Path](./388.%20Longest%20Absolute%20File%20Path)
- [389. Find the Difference](./389.%20Find%20the%20Difference)
- [390. Elimination Game](./390.%20Elimination%20Game)
- [391. Perfect Rectangle](./391.%20Perfect%20Rectangle)
- [392. Is Subsequence](./392.%20Is%20Subsequence)
- [393. UTF-8 Validation](./393.%20UTF-8%20Validation)
- [394. Decode String](./394.%20Decode%20String)
- [395. Longest Substring with At Least K Repeating Characters](./395.%20Longest%20Substring%20with%20At%20Least%20K%20Repeating%20Characters)
- [396. Rotate Function](./396.%20Rotate%20Function)
- [397. Integer Replacement](./397.%20Integer%20Replacement)
- [398. Random Pick Index](./398.%20Random%20Pick%20Index)
- [399. Evaluate Division](./399.%20Evaluate%20Division)
- [400. Nth Digit](./400.%20Nth%20Digit)
- [401. Binary Watch](./401.%20Binary%20Watch)
- [402. Remove K Digits](./402.%20Remove%20K%20Digits)
- [403. Frog Jump](./403.%20Frog%20Jump)
- [404. Sum of Left Leaves](./404.%20Sum%20of%20Left%20Leaves)
- [405. Convert a Number to Hexadecimal](./405.%20Convert%20a%20Number%20to%20Hexadecimal)
- [406. Queue Reconstruction by Height](./406.%20Queue%20Reconstruction%20by%20Height)
- [407. Trapping Rain Water II](./407.%20Trapping%20Rain%20Water%20II)
- [409. Longest Palindrome](./409.%20Longest%20Palindrome)
- [410. Split Array Largest Sum](./410.%20Split%20Array%20Largest%20Sum)
- [412. Fizz Buzz](./412.%20Fizz%20Buzz)
- [413. Arithmetic Slices](./413.%20Arithmetic%20Slices)
- [414. Third Maximum Number](./414.%20Third%20Maximum%20Number)
- [415. Add Strings](./415.%20Add%20Strings)
- [416. Partition Equal Subset Sum](./416.%20Partition%20Equal%20Subset%20Sum)
- [417. Pacific Atlantic Water Flow](./417.%20Pacific%20Atlantic%20Water%20Flow)
- [419. Battleships in a Board](./419.%20Battleships%20in%20a%20Board)
- [420. Strong Password Checker](./420.%20Strong%20Password%20Checker)
- [421. Maximum XOR of Two Numbers in an Array](./421.%20Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array)
- [423. Reconstruct Original Digits from English](./423.%20Reconstruct%20Original%20Digits%20from%20English)
- [424. Longest Repeating Character Replacement](./424.%20Longest%20Repeating%20Character%20Replacement)
- [427. Construct Quad Tree](./427.%20Construct%20Quad%20Tree)
- [429. N-ary Tree Level Order Traversal](./429.%20N-ary%20Tree%20Level%20Order%20Traversal)
- [430. Flatten a Multilevel Doubly Linked List](./430.%20Flatten%20a%20Multilevel%20Doubly%20Linked%20List)
- [433. Minimum Genetic Mutation](./433.%20Minimum%20Genetic%20Mutation)
- [434. Number of Segments in a String](./434.%20Number%20of%20Segments%20in%20a%20String)
- [435. Non-overlapping Intervals](./435.%20Non-overlapping%20Intervals)
- [436. Find Right Interval](./436.%20Find%20Right%20Interval)
- [437. Path Sum III](./437.%20Path%20Sum%20III)
- [438. Find All Anagrams in a String](./438.%20Find%20All%20Anagrams%20in%20a%20String)
- [440. K-th Smallest in Lexicographical Order](./440.%20K-th%20Smallest%20in%20Lexicographical%20Order)
- [441. Arranging Coins](./441.%20Arranging%20Coins)
- [442. Find All Duplicates in an Array](./442.%20Find%20All%20Duplicates%20in%20an%20Array)
- [443. String Compression](./443.%20String%20Compression)
- [445. Add Two Numbers II](./445.%20Add%20Two%20Numbers%20II)
- [446. Arithmetic Slices II - Subsequence](./446.%20Arithmetic%20Slices%20II%20-%20Subsequence)
- [447. Number of Boomerangs](./447.%20Number%20of%20Boomerangs)
- [448. Find All Numbers Disappeared in an Array](./448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array)
- [449. Serialize and Deserialize BST](./449.%20Serialize%20and%20Deserialize%20BST)
- [450. Delete Node in a BST](./450.%20Delete%20Node%20in%20a%20BST)
- [451. Sort Characters By Frequency](./451.%20Sort%20Characters%20By%20Frequency)
- [452. Minimum Number of Arrows to Burst Balloons](./452.%20Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons)
- [453. Minimum Moves to Equal Array Elements](./453.%20Minimum%20Moves%20to%20Equal%20Array%20Elements)
- [454. 4Sum II](./454.%204Sum%20II)
- [455. Assign Cookies](./455.%20Assign%20Cookies)
- [456. 132 Pattern](./456.%20132%20Pattern)
- [457. Circular Array Loop](./457.%20Circular%20Array%20Loop)
- [458. Poor Pigs](./458.%20Poor%20Pigs)
- [459. Repeated Substring Pattern](./459.%20Repeated%20Substring%20Pattern)
- [461. Hamming Distance](./461.%20Hamming%20Distance)
- [462. Minimum Moves to Equal Array Elements II](./462.%20Minimum%20Moves%20to%20Equal%20Array%20Elements%20II)
- [463. Island Perimeter](./463.%20Island%20Perimeter)
- [464. Can I Win](./464.%20Can%20I%20Win)
- [466. Count The Repetitions](./466.%20Count%20The%20Repetitions)
- [467. Unique Substrings in Wraparound String](./467.%20Unique%20Substrings%20in%20Wraparound%20String)
- [468. Validate IP Address](./468.%20Validate%20IP%20Address)
- [470. Implement Rand10() Using Rand7()](./470.%20Implement%20Rand10%28%29%20Using%20Rand7%28%29)
- [472. Concatenated Words](./472.%20Concatenated%20Words)
- [473. Matchsticks to Square](./473.%20Matchsticks%20to%20Square)
- [474. Ones and Zeroes](./474.%20Ones%20and%20Zeroes)
- [475. Heaters](./475.%20Heaters)
- [476. Number Complement](./476.%20Number%20Complement)
- [477. Total Hamming Distance](./477.%20Total%20Hamming%20Distance)
- [478. Generate Random Point in a Circle](./478.%20Generate%20Random%20Point%20in%20a%20Circle)
- [479. Largest Palindrome Product](./479.%20Largest%20Palindrome%20Product)
- [480. Sliding Window Median](./480.%20Sliding%20Window%20Median)
- [481. Magical String](./481.%20Magical%20String)
- [482. License Key Formatting](./482.%20License%20Key%20Formatting)
- [483. Smallest Good Base](./483.%20Smallest%20Good%20Base)
- [3379. Transformed Array](./3379.%20Transformed%20Array)
- [3013. Divide an Array Into Subarrays With Minimum Cost II](./3013.%20Divide%20an%20Array%20Into%20Subarrays%20With%20Minimum%20Cost%20II)
- [3640. Trionic Array II](./3640.%20Trionic%20Array%20II)
- [3650. Minimum Cost Path with Edge Reversals](./3650.%20Minimum%20Cost%20Path%20with%20Edge%20Reversals)
- [3719. Longest Balanced Subarray I](./3719.%20Longest%20Balanced%20Subarray%20I)
- [3721. Longest Balanced Subarray II](./3721.%20Longest%20Balanced%20Subarray%20II)
- [3713. Longest Balanced Substring I](./3713.%20Longest%20Balanced%20Substring%20I)

## Day 30: 2026-01-30
- [376. Wiggle Subsequence](./376.%20Wiggle%20Subsequence)
- [377. Combination Sum IV](./377.%20Combination%20Sum%20IV)
- [378. Kth Smallest Element in a Sorted Matrix](./378.%20Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix)
- [382. Linked List Random Node](./382.%20Linked%20List%20Random%20Node)
- [383. Ransom Note](./383.%20Ransom%20Note)
- [384. Shuffle an Array](./384.%20Shuffle%20an%20Array)
- [385. Mini Parser](./385.%20Mini%20Parser)
- [386. Lexicographical Numbers](./386.%20Lexicographical%20Numbers)
- [387. First Unique Character in a String](./387.%20First%20Unique%20Character%20in%20a%20String)

## Day 30 Part 2: 2026-01-30
- [2977. Minimum Cost to Convert String II](./2977.%20Minimum%20Cost%20to%20Convert%20String%20II)
- [385. Mini Parser (Fixed)](./385.%20Mini%20Parser)

## Day 31: 2026-01-31
- [388. Longest Absolute File Path](./388.%20Longest%20Absolute%20File%20Path)
- [389. Find the Difference](./389.%20Find%20the%20Difference)
- [390. Elimination Game](./390.%20Elimination%20Game)
- [391. Perfect Rectangle](./391.%20Perfect%20Rectangle)
- [392. Is Subsequence](./392.%20Is%20Subsequence)
- [393. UTF-8 Validation](./393.%20UTF-8%20Validation)
- [394. Decode String](./394.%20Decode%20String)
- [395. Longest Substring with At Least K Repeating Characters](./395.%20Longest%20Substring%20with%20At%20Least%20K%20Repeating%20Characters)
- [396. Rotate Function](./396.%20Rotate%20Function)
- [397. Integer Replacement](./397.%20Integer%20Replacement)

## Day 32: 2026-02-01
- [398. Random Pick Index](./398.%20Random%20Pick%20Index)
- [399. Evaluate Division](./399.%20Evaluate%20Division)
- [400. Nth Digit](./400.%20Nth%20Digit)
- [401. Binary Watch](./401.%20Binary%20Watch)
- [402. Remove K Digits](./402.%20Remove%20K%20Digits)
- [403. Frog Jump](./403.%20Frog%20Jump)
- [404. Sum of Left Leaves](./404.%20Sum%20of%20Left%20Leaves)
- [405. Convert a Number to Hexadecimal](./405.%20Convert%20a%20Number%20to%20Hexadecimal)
- [406. Queue Reconstruction by Height](./406.%20Queue%20Reconstruction%20by%20Height)
- [407. Trapping Rain Water II](./407.%20Trapping%20Rain%20Water%20II)

## Day 33: 2026-02-02
- [409. Longest Palindrome](./409.%20Longest%20Palindrome)
- [410. Split Array Largest Sum](./410.%20Split%20Array%20Largest%20Sum)
- [412. Fizz Buzz](./412.%20Fizz%20Buzz)
- [413. Arithmetic Slices](./413.%20Arithmetic%20Slices)
- [414. Third Maximum Number](./414.%20Third%20Maximum%20Number)
- [415. Add Strings](./415.%20Add%20Strings)
- [416. Partition Equal Subset Sum](./416.%20Partition%20Equal%20Subset%20Sum)
- [417. Pacific Atlantic Water Flow](./417.%20Pacific%20Atlantic%20Water%20Flow)
- [419. Battleships in a Board](./419.%20Battleships%20in%20a%20Board)
- [420. Strong Password Checker](./420.%20Strong%20Password%20Checker)
- [3013. Divide an Array Into Subarrays With Minimum Cost II](./3013.%20Divide%20an%20Array%20Into%20Subarrays%20With%20Minimum%20Cost%20II)

## Day 34: 2026-02-03
- [421. Maximum XOR of Two Numbers in an Array](./421.%20Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array)
- [423. Reconstruct Original Digits from English](./423.%20Reconstruct%20Original%20Digits%20from%20English)
- [424. Longest Repeating Character Replacement](./424.%20Longest%20Repeating%20Character%20Replacement)
- [427. Construct Quad Tree](./427.%20Construct%20Quad%20Tree)
- [429. N-ary Tree Level Order Traversal](./429.%20N-ary%20Tree%20Level%20Order%20Traversal)
- [433. Minimum Genetic Mutation](./433.%20Minimum%20Genetic%20Mutation)
- [434. Number of Segments in a String](./434.%20Number%20of%20Segments%20in%20a%20String)
- [435. Non-overlapping Intervals](./435.%20Non-overlapping%20Intervals)
- [436. Find Right Interval](./436.%20Find%20Right%20Interval)
- [437. Path Sum III](./437.%20Path%20Sum%20III)
- [430. Flatten a Multilevel Doubly Linked List](./430.%20Flatten%20a%20Multilevel%20Doubly%20Linked%20List)
- [438. Find All Anagrams in a String](./438.%20Find%20All%20Anagrams%20in%20a%20String)

## Day 35: 2026-02-04
- [440. K-th Smallest in Lexicographical Order](./440.%20K-th%20Smallest%20in%20Lexicographical%20Order)
- [441. Arranging Coins](./441.%20Arranging%20Coins)
- [442. Find All Duplicates in an Array](./442.%20Find%20All%20Duplicates%20in%20an%20Array)
- [443. String Compression](./443.%20String%20Compression)
- [445. Add Two Numbers II](./445.%20Add%20Two%20Numbers%20II)
- [446. Arithmetic Slices II - Subsequence](./446.%20Arithmetic%20Slices%20II%20-%20Subsequence)
- [447. Number of Boomerangs](./447.%20Number%20of%20Boomerangs)
- [448. Find All Numbers Disappeared in an Array](./448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array)
- [449. Serialize and Deserialize BST](./449.%20Serialize%20and%20Deserialize%20BST)
- [3640. Trionic Array II](./3640.%20Trionic%20Array%20II)

## Day 36: 2026-02-05
- [450. Delete Node in a BST](./450.%20Delete%20Node%20in%20a%20BST)
- [451. Sort Characters By Frequency](./451.%20Sort%20Characters%20By%20Frequency)
- [452. Minimum Number of Arrows to Burst Balloons](./452.%20Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons)
- [453. Minimum Moves to Equal Array Elements](./453.%20Minimum%20Moves%20to%20Equal%20Array%20Elements)
- [454. 4Sum II](./454.%204Sum%20II)
- [455. Assign Cookies](./455.%20Assign%20Cookies)
- [456. 132 Pattern](./456.%20132%20Pattern)
- [457. Circular Array Loop](./457.%20Circular%20Array%20Loop)
- [458. Poor Pigs](./458.%20Poor%20Pigs)
- [459. Repeated Substring Pattern](./459.%20Repeated%20Substring%20Pattern)
- [3379. Transformed Array](./3379.%20Transformed%20Array)
- [461. Hamming Distance](./461.%20Hamming%20Distance)
- [462. Minimum Moves to Equal Array Elements II](./462.%20Minimum%20Moves%20to%20Equal%20Array%20Elements%20II)
- [463. Island Perimeter](./463.%20Island%20Perimeter)
- [464. Can I Win](./464.%20Can%20I%20Win)
- [466. Count The Repetitions](./466.%20Count%20The%20Repetitions)

## Day 37: 2026-02-06
- [467. Unique Substrings in Wraparound String](./467.%20Unique%20Substrings%20in%20Wraparound%20String)
- [468. Validate IP Address](./468.%20Validate%20IP%20Address)
- [470. Implement Rand10() Using Rand7()](./470.%20Implement%20Rand10%28%29%20Using%20Rand7%28%29)
- [472. Concatenated Words](./472.%20Concatenated%20Words)
- [473. Matchsticks to Square](./473.%20Matchsticks%20to%20Square)

## Day 38: 2026-02-07
- [474. Ones and Zeroes](./474.%20Ones%20and%20Zeroes)
- [475. Heaters](./475.%20Heaters)
- [476. Number Complement](./476.%20Number%20Complement)
- [477. Total Hamming Distance](./477.%20Total%20Hamming%20Distance)
- [478. Generate Random Point in a Circle](./478.%20Generate%20Random%20Point%20in%20a%20Circle)
- [479. Largest Palindrome Product](./479.%20Largest%20Palindrome%20Product)
- [480. Sliding Window Median](./480.%20Sliding%20Window%20Median)
- [481. Magical String](./481.%20Magical%20String)
- [482. License Key Formatting](./482.%20License%20Key%20Formatting)
- [483. Smallest Good Base](./483.%20Smallest%20Good%20Base)

## Day 40: 2026-02-09
- [1382. Balance a Binary Search Tree](./1382.%20Balance%20a%20Binary%20Search%20Tree)

## Day 41: 2026-02-10
- [3719. Longest Balanced Subarray I](./3719.%20Longest%20Balanced%20Subarray%20I)

## Day 42: 2026-02-11
- [3721. Longest Balanced Subarray II](./3721.%20Longest%20Balanced%20Subarray%20II)

## Day 43: 2026-02-12
- [3713. Longest Balanced Substring I](./3713.%20Longest%20Balanced%20Substring%20I)

