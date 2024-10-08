clear all; close all;
load dt.dat
x_freq = dt(:,1);
y_ampli = dt(:,2);
figure(1)
plot(x_freq,y_ampli,'or',x_freq,y_ampli,'b')
xlabel('Frequency')
ylabel('Amplitude')
