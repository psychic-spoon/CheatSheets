
## Association Rule Mining
> Predict the occurrence of an item based on the occurrences of other items in the transaction.**It is based on co-occurence doesn't imply causality**

An implication expression of the form X :arrow_right: Y, where X and Y are itemsets

Association rules discovery is used in market basket analysis, item placement planning, and promotional sales planning, among many other applications.

#### Support count
Frequency of occurrence of an itemset.

#### Support
Fraction of transactions that contain an itemset. 
Fraction of transactions that contain both X and Y. \
**The support of an association rule is the percentage of groups that contain all of the items listed in that association rule.**
		
#### Frequent Itemset
An itemset whose support is greater than or equal to a minsup threshold

#### Confidence
**The confidence value indicates how reliable this rule is.** \
Measures how often items in Y appear in transactions that contain X.

### Lift
The lift value is a measure of importance of a rule.

\
Rules originating from the same itemset have identical support but can have different confidence.
 Thus, we may decouple the support and confidence requirements.
\

## Apriori principle:
– If an itemset is frequent, then all of its subsets must also
be frequent.
– Support of an itemset never exceeds the support of its subsets.
– This is known as the _anti-monotone property_ of support. 

## RULE Creation
For each frequent itemset f, generate all nonempty subsets of f. \
For every nonempty subset s of f, output the rule “s --> (f - s)“ \
Compute the confidence for each rule.
_Prune based on minconf_

> confidence does not have an anti-monotone property.
	c(ABC :right_arrow: D) can be larger or smaller than c(AB :right_arrow: D)

But confidence of rules generated from the same itemset has an anti-monotone property \
e.g., L = {A,B,C,D}:  \
		c(ABC :right_arrow: D) >= c(AB :right_arrow: CD) >= c(A :right_arrow: BCD)
 
 Confidence is anti-monotone w.r.t. number of items on the RHS of the rule


