def test_ugly_number1():
    assert ugly_number(1)== True
def test_ugly_number2():
    assert ugly_number(2)==True
def test_ugly_number3():
    assert ugly_number(3)==True
def test_ugly_number4():
    assert ugly_number(7)==False

def test_ugly_series1():
    assert ugly_series(2)==[1,2]
def test_ugly_series2():
    assert ugly_series(3)==[1,2,3]
def test_ugly_series3():
    assert ugly_series(7)==[1,2,3,4,5,6,8]
def test_ugly_series4():
    assert ugly_series(10)==[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

def test_fibonacci1():
    assert fibonacci(5)==3
def test_fibonacci2():
    assert fibonacci(6)==5
def test_fibonacci3():
    assert fibonacci(7)==8
def test_fibonacci4():
    assert fibonacci(10)==34

def test_fibonacci_series1():
    assert fibonacci_series(2)==[0,1]
def test_fibonacci_series2():
    assert fibonacci_series(5)==[0,1,1,2,3]
def test_fibonacci_series3():
    assert fibonacci_series(10)==[0,1,1,2,3,5,8,13,21,34]
def test_fibonacci_series4():
    assert fibonacci_series(12)==[0,1,1,2,3,5,8,13,21,34,55,89] 

def test_catalan1():
    assert catalan(2)==1   
def test_catalan2():
    assert catalan(3)==2
def test_catalan3():
    assert catalan(5)==14
def test_catalan4():
    assert catalan(8)==429

def test_catalan_series1():
    assert catalan_series(2)==[1,1]
def test_catalan_series2():
    assert catalan_series(5)==[1,1,2,5,14]
def test_catalan_series3():
    assert catalan_series(9)==[1,1,2,5,14,42,132,429,1430]
def test_catalan_series4():
    assert catalan_series(12)==[1,1,2,5,14,42,132,429,1430,4862,16796]

def test_factorial1():
    assert factorial(5)==120
def test_factorial2():
    assert factorial(9)==362880
def test_factorial3():
    assert factorial(8)==40320
def test_factorial4():
    assert factorial(10)==3628800

def test_stirling_factorial1():
    assert stirling_factorial(1)==[0.92,1.00]
def test_stirling_factorial2():
    assert stirling_factoria(5)==[118.02,120.00]
def test_stirling_factorial13():
    assert stirling_factoria(9)==[359536.87,362881.38]
def test_stirling_factorial4():
    assert stirling_factorial(12)==[475687486.47,479002368.48]

def test_bell_number1():
    assert bell_number(1)==1
def test_bell_number2():
    assert bell_number(2)==1
def test_bell_number3():
    assert bell_number(5)==15
def test_bell_number4():
    assert bell_number(8)==877

def test_bell_series1():
    assert bell_series(2)==[1,1]
def test_bell_series2():
    assert bell_series(3)==[1,1,2]
def test_bell_series3():
    assert bell_series(5)==[1,1,2,5,15]
def test_bell_series4():
    assert bell_series(9)==[1,1,2,5,15,52,203,877,4140]

def test_binomialCoef1():
    assert binomialCoef(3,3)==1
def test_binomialCoef2():
    assert binomialCoef(5,3)==10
def test_binomialCoef3():
    assert binomialCoef(5,4)==5
def test_binomialCoef4():
    assert binomialCoef(5,5)==1

def test_nCkModp1():
    assert nCkModp(10,2,13)==6
def test_nCkModp2():
    assert nCkModp(6,2,13)==2
def test_nCkModp3():
    assert nCkModp(10,11,13)==0
def test_nCkModp4():
    assert nCkModp(10,6,5)==0