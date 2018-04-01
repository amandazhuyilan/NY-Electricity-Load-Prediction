## New York State Electricity Prediction with Tensorflow and MATLAB
Remaking my undergrad capstone design with Google's Machine Learning Framework [Tensorflow](https://www.tensorflow.org/). See poster [here](https://github.com/amandazhuyilan/TensorFlow-Electricity-Load-Prediction/blob/master/Yilan%20Zhu-Forecasting%20system%20of%20electricity%20load%20of%20New%20York%20State%20Poster.pdf) for more information on previous prediction done with Matlab's Neural Network Toolbox.

Electricity load data from [NYISO](http://www.nyiso.com/public/markets_operations/market_data/load_data/index.jsp). Link on how read data [here](https://blog.csdn.net/JR_lu/article/details/69499494).

Weather data from [Mesowest](http://mesowest.utah.edu/).

### TensorFlow

TensorFlow is Google’s system for the implementation and deploy- ment of large-scale machine learning models. 

Edges in TensorFlow graphs serve three different purposes:
- Data dependency edges represent tensors, or multidimensional arrays, that are input and output data of the operations. 
- Reference edges, or outputs of variable operations, represent pointers to the variable rather than its value, allowing dependent operations (e.g., ```Assign```) to mutate the referenced variable. 
- Control dependency edges do not represent any data but indicate that their source operations must execute before their tail operations can start.


#### Installation and Configuration (MacOS)
- Install [Anaconda](https://www.anaconda.com/download/#macos).
- Run ```conda env create -f mac_tfdl_env.yml``` on Terminal in the project directory.
