clc;
clear;
clear all;

%input training data
month=xlsread('Total load 2006-2015.xls','2014','A2:A8761');
day=xlsread('Total load 2006-2015','2014','B2:B8761');
hour=xlsread('Total load 2006-2015','2014','C2:C8761');
Input=[month day hour];
Target=xlsread('Total load 2006-2015','2014','D2:D8761');    

%data normalization: mapping row minimum and maximum values to [-1 1]
[tn,ts] = mapminmax(Target');

%Create a feed-forward backpropagation network with 3 inputs. 1 output and
%8 hidden layers
net = newff(Input',tn,50);
net = revert(net);
net.trainParam.goal=1e-5;               % stop training if the error goal hit 1e-5
net.trainParam.epochs=100;              % Max no. of epochs to train
net.trainParam.max_fail=50;             % No. of validation checks
net.divideFcn = 'dividerand';           % Divide data randomly
net.divideParam.trainRatio = 85/100;    % 85% of data for training
net.divideParam.testRatio = 15/100;     % 15% of data for testing

net = train(net, Input', tn);

%retrain NN with data from 2010-2013
for i=2010:2013
    i=num2str(i);
    month=xlsread('Total load 2006-2015.xls',i,'A2:A8761');
    day=xlsread('Total load 2006-2015',i,'B2:B8761');
    hour=xlsread('Total load 2006-2015',i,'C2:C8761');
    P=[month day hour];
    T=xlsread('Total load 2006-2015',i,'D2:D8761');     %target load data
    [tn,ts] = mapminmax(T');
    net = train(net, P', tn);
end

%use input data from 2014 for a prediction set
output = sim(net, Input');
%return the normalizied data into original format
forecast = mapminmax('reverse',output,ts);

figure
plot(Target','g');
hold on
plot(forecast,'r');

Err_Percentage = mean(abs(forecast-Target')/Target'*100)

toc
