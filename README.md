# CSCI-570-AnalysisofAlgorithms-FinalProject

  The project is related to the implementation of the two different solutions provided in chapter 6 of the Kleinberg textbook for the Sequence Alignment problem. 

II. Project Description
Implement the basic Dynamic Programming solution to the Sequence Alignment problem. Run the test set provided and show your results.

A. Algorithm Description:
Suppose we are given two strings X and Y, where X consists of the sequence of symbols x1, x2 . . . xm and Y consists of the sequence of symbols y1, y2 . . . yn. Consider the sets {1, 2, . . . , m} and {1, 2, . . . , n} as representing the different positions in the strings X and Y, and consider a matching of these sets; recall that a matching is a set of ordered pairs with the property that each item occurs in at most one pair. We say that a matching M of these two sets is an alignment if there are no “crossing” pairs: if (i, j), (i’, j’) ∈ M and i < i’, then j < j’ . Intuitively, an alignment gives a way of lining up the two strings, by telling us which pairs of positions will be lined up with one another.
Our definition of similarity will be based on finding the optimal alignment between X and Y, according to the following criteria. Suppose M is a given alignment between X and Y:
1. First, there is a parameter δe > 0 that defines a gap penalty. For each position of X or Y that is not matched in M — it is a gap — we incur a cost of δ.
2. Second, for each pair of letters p, q in our alphabet, there is a mismatch cost of αpq for lining up p with q. Thus, for each (i, j) ∈ M, we pay the appropriate mismatch
 
 cost αxiyj for lining up xi with yj. One generally assumes that αpp = 0 for each letter p—there is no mismatch cost to line up a letter with another copy of itself—although this will not be necessary in anything that follows.
 
3. The cost of M is the sum of its gap and mismatch costs, and we seek an alignment of minimum cost.
B. Input string Generator:

The input to the program would be a text file, input.txt containing the following information:
1. First base string
2. Next j lines would consist of indices corresponding the after which the previous string to be added to the cumulative string
3. Second base string
4. Next k lines would consist of where the base string to be added to the cumulative string

This information would help generate 2 strings from the original 2 base strings. This file could be used as an input to your program and your program could use the base strings and the rules to generate the actual strings. Also note that the numbers j and k corresponds to the first and the second string respectively. Make sure you validate the length of the first and the second string to be 2j*str1.length and 2k*str2.length. Please note that the base strings need not have to be of equal length and similarly, j need not be equal to k.
  
