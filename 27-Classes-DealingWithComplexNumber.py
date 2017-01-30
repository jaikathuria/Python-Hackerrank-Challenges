class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real,imaginary)
    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real,imaginary)
    def __mul__(self, no):
        real = (self.real*no.real) - (self.imaginary*no.imaginary)
        imaginary = (self.real*no.imaginary) + (self.imaginary*no.real)
        return Complex(real,imaginary)

    def __div__(self, no):
        div = math.pow(no.real,2) + math.pow(no.imaginary,2)
        real = ((self.real*no.real) + (self.imaginary*no.imaginary))/div
        imaginary = ((self.imaginary*no.real) - (self.real*no.imaginary))/div
        return Complex(real,imaginary)
    def mod(self):
        real = math.pow(self.real,2)
        imaginary = math.pow(self.imaginary,2)
        real = math.sqrt(real + imaginary)
        imaginary = 0
        return Complex(real,imaginary)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
