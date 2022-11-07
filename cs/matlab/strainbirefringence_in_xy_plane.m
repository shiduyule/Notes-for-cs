%% 这是折射率xy 平面
no = 1.511; ne = 1.470;
beta11 = 1/no^2; % 主轴折射率
beta22 = 1/no^2;
p66 = -0.064;  % 应变弹光系数
S21 = 0.00002;
beta21 = p66.*S21; 
f = @(x,y) beta11*x.^2 + beta22 *y.^2  + 2*beta21*x.*y - 1;
fimplicit(f)
xlabel('nx');
ylabel('ny');
%title('理想状态下的折射率xy平面');
title('存在σ21下的折射率xy平面');
axis equal
%% 计算椭圆主值  P206
lambda11 = beta11 + beta21;
lambda22 = beta11 - beta21;
n11 = (1/lambda11)^(1/2);
n22 = (1/lambda22)^(1/2);
%% 计算光轴倾角 正光性双轴晶  P133
x = ((n22^2 - n11^2)/(ne^2 - n22^2))^(1/2);
omega = atan(ne*((n22^2 - n11^2)/(ne^2 - n22^2))^(1/2)/n11); 
theta = 180*omega/ pi;
fprintf('n11=%f n22=%f ne=%f \n应变是%f\n光轴倾角是%f',n11,n22,ne,S21,theta);

