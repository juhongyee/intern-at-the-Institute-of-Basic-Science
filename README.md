# internship_Institute-of-Basic-Science

------
## Summary

Strategy in education refers to a sequence that incorporates learning material along with certain details, such as expected learning time and its importance (weight). Our objective is to devise this strategy using E-learning data. Initially, the data was unstructured, but we transformed it into a more useful format using Pandas. Subsequently, we applied a scheduling algorithm to obtain the optimal strategy.

We structured the data into a tree format by referencing the students' curriculum and applied the expanded c-mu rule to this tree.

The expanded c-mu rule is the c-mu rule applied in the context of a tree (the original c-mu rule was defined only within a set of sequences). We were able to prove the expanded c-mu rule with relative ease and apply it. Note that some others have previously proven this rule, excluding us.

The code for the expanded c-mu rule can be found in the 'scheduling' folder.

Additionally, our trial and error processes can be seen in the Gittin index folder and the Baum-Welch folder. For non-hierarchical structures, we utilized the Gittin index and Baum-Welch algorithm, but they were not suitable for hierarchical structures.
