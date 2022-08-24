# EXP-solver

This a prototypical solver for the extension of Presburger arithmetic with exponential functions, namely, linear integer arithmetic plus $10^x$ function $(\mathbb N,+,10^x)$. The solver is based on [Point's quantifier elimination procedure](https://cpb-us-w2.wpmucdn.com/u.osu.edu/dist/1/1952/files/2014/01/0AppB072710-1mnlwyn.pdf). For more details about this algorithm, please refer to our paper *A Decision Procedure for String Constraints with String-Integer Conversion and Flat Regular Constraints*. 

## Benchmarks

#### Arithmetic Benchmark
For example, in the $(2,3,3,4)$ group, the first test 
```
{-69,97,95792,19684,-10671,-78209,86876,0,-97300}
{-66,-73,2817,-24158,-15169,-90303,74384,6606}
{-35,-36,84682,63074,72701,-25207,-45670,58485}
{-43994,-34064,48000,95204,-79965,25}
{11240,-6357,-57242,57487,-82001,-8403}
{84701,-6295,25332,-20749,-37170,96869}
{-59357,-1494,-76257,56802,39683,-45546}
```
denotes a system of inequalities:
$$\begin{aligned}
-69\cdot 10^{x_1} + 97\cdot 10^{x_2} +95792 x_1+19684x_2-10671 x_3 -78209 x_4+86876 x_5 &\le -97300\\
-66\cdot 10^{x_1} -73\cdot 10^{x_2} +2817 x_1-24158 x_2-15169 x_3 -90303 x_4+74384 x_5 &\le 6606\\
-35\cdot 10^{x_1} -36\cdot 10^{x_2} +84682 x_1-63074 x_2-72701 x_3 -25207 x_4-45670 x_5 &\le 58485\\
-43994 x_1-34064 x_2+48000 x_3 +95204 x_4-79965 x_5 &\le 25\\
\cdots \text{3 more linear inequalites}
\end{aligned}$$

#### StringHash Function Benchmark
For example, in `all/head/paras`, `100` in the first line denotes the total number of tests. The 1st test `{1,0,12345,6789,331,179}` is to find a string $x\in 12345(0-9)^*$ such that $(\textsf{parseInt}(x) \mod 331)\mod 179=0$.

`test?` files are smt files for CVC4,CVC5.
`trautest?` files are smt files for Trau. (it seems Trau has some problem with regular expressions.)