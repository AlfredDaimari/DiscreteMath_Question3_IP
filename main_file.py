from time import sleep
from tkinter import *
from copy import deepcopy


# Class below uses tkinter to display polynomial output
class Display:
    frame_line_display = 150

    def __init__(self, master):
        master.geometry("1000x600")
        master.title("Polynomial GCD")
        # master.iconbitmap("D:/Python and Java/DM/Discrete_Mathematics/Poly.ico")
        master.config(bg="white")
        self.root = master
        self.displaynames()

    def displaynames(self):
        frame = Frame(self.root, height=600, width=1000, bg="white", relief=GROOVE, highlightbackground="slategray",
                      highlightthickness=4)
        frame.pack(side=LEFT)
        calc = Label(frame, font=("Times New Roman", 25, "bold italic"), text="Discrete Mathematics:Polynomial GCD",
                     bg="white", fg="darkcyan")
        calc.place(x=215, y=230)
        sleep(1)
        frame.update()
        names = Label(frame, font=("Ink Free", 25, "bold italic"), text="Created by Adya, Alfred, Ritul and  Samarth",
                      fg="gray", bg="white")
        sleep(1)
        names.place(x=160, y=270)
        frame.update()
        sleep(3)
        frame.destroy()
        self.inputdisplay()

    def inputdisplay(self):
        frame = Frame(self.root, height=600, width=1000, bg="white", relief=GROOVE, highlightbackground="slategray",
                      highlightthickness=4)
        ask_label = Label(frame, font=("Comic Sans MS", 17, "bold italic"), bg="white", fg="darkcyan",
                          text="Enter polynomials below in the form x^3-12x+1,-x-1, etc.")
        ask_label.place(x=170, y=230)
        div = Entry(frame, relief=GROOVE, bd=3, font=("Times New Roman", 15, "italic"), width=25, fg="slategray",
                    bg="ghostwhite")
        div.place(x=380, y=270)
        divisor = Entry(frame, relief=GROOVE, bd=3, font=("Times New Roman", 15, "italic"), width=25, fg="slategray",
                        bg="ghostwhite")
        divisor.place(x=380, y=300)

        def calculate():
            div_str = div.get()
            divisor_str = divisor.get()
            frame.destroy()
            self.finaldisplay(div_str, divisor_str)

        calc = Button(frame, font=("Comic Sans MS", 15, "bold"), text="Calculate", command=calculate,
                      activebackground="ghostwhite", bg="gainsboro", activeforeground="darkcyan", fg="darkcyan",
                      relief=GROOVE, width=7, bd=3, )
        calc.place(x=460, y=334)
        div_label = Label(frame, font=("Comic Sans MS", 14, "bold italic"), bg="white", fg="black", text="Dividend:",
                          cursor="pirate")
        div_label.place(x=276, y=270)
        divisor_label = Label(frame, font=("Comic Sans MS", 14, "bold italic"), bg="white", fg="black", text="Divisor:",
                              cursor="pirate")
        divisor_label.place(x=276, y=300)
        frame.pack()

    def finaldisplay(self, dividend, divisor):
        frame = Frame(self.root, width=1000, height=600, highlightbackground="slategray", highlightthickness=4)
        canvas = Canvas(frame, bg="white", width=1000, height=540, scrollregion=(0, 0, 1000, 1300))
        scroll = Scrollbar(frame, orient=VERTICAL)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=canvas.yview)
        canvas.config(yscrollcommand=scroll.set)
        canvas.create_text(500, 50, text="GCD AND BEZOUT'S COEFFICIENTS",
                           font=("Comic Sans MS", 25, "bold italic underline"), fill="darkcyan")
        canvas.create_text(100, self.frame_line_display, text="Dividend: " + dividend,
                           font=("Comic Sans MS", 15, "bold italic"), fill="black", anchor=NW)
        self.frame_line_display += 20
        canvas.create_text(100, self.frame_line_display, text="Divisor: " + divisor,
                           font=("Comic Sans MS", 15, "bold italic"), fill="black", anchor=NW)
        self.frame_line_display += 150
        canvas.create_text(500, self.frame_line_display, text="Calculating GCD",
                           font=("Comic Sans MS", 18, "bold italic underline"), fill="darkcyan")
        canvas.pack()
        frame.pack()
        backend_control(self, frame, canvas, dividend, divisor)

    def dis_div(self, st, canvas):  # The list sent has to have dividend, divisor, quotient and remainder in str form
        length = len(st) // 100
        if length >= 1:
            for i in range(0, length + 1):
                self.frame_line_display += 20
                canvas.create_text(50, self.frame_line_display,
                                   text=st[i * 100: i * 100 + 100 if i * 100 + 100 < len(st) else len(st)],
                                   font=("Cambria Math", 13, "normal"), fill="black", anchor=NW)
        else:
            self.frame_line_display += 20
            canvas.create_text(50, self.frame_line_display, text=st, font=("Cambria Math", 13, "normal"), fill="black",
                               anchor=NW)
        canvas.update()

    def dis_bez(self, canvas, st):
        length = len(st) // 100
        if length >= 1:
            for i in range(0, length + 1):
                self.frame_line_display += 20
                canvas.create_text(50, self.frame_line_display,
                                   text=st[i * 100: i * 100 + 100 if i * 100 + 100 < len(st) else len(st)],
                                   font=("Cambria Math", 13, "normal"), fill="black", anchor=NW)
        else:
            self.frame_line_display += 20
            canvas.create_text(50, self.frame_line_display, text=st, font=("Cambria Math", 13, "normal"), fill="black",
                               anchor=NW)

    def restart(self, frame):
        def restart_bt():
            frame.destroy()
            self.frame_line_display = 150
            self.inputdisplay()

        frame.config(bg="darkcyan")
        rst_button = Button(frame, font=("Comic Sans MS", 15, "bold"), text="Restart", command=restart_bt,
                            activebackground="ghostwhite", bg="gainsboro", activeforeground="darkcyan", fg="darkcyan",
                            relief=GROOVE, width=7, bd=3, )
        rst_button.pack()


#  This class helps us store the polynomial in the form of an object of 2 lists,coefficients and power
class Polynomial:

    def __init__(self, input_=None):
        self.coefficients = []
        self.power = []
        if input_:
            self.coe_power(input_)

    def coe_power(self, input_):  # Function to breakup the string into polynomial object
        input_ = polynomial_breakup(input_)
        for i in input_:
            self.coefficients.append(float(i[0:i.find('x')]))
            self.power.append(int(i[i.find('^') + 1:]))

    def pol_add(self, poly_):  # Function to add two polynomials that belong to the polynomial class
        a = self.power[0] < poly_.power[0]
        term1, term2 = deepcopy(poly_) if a else deepcopy(self), deepcopy(self) if a else deepcopy(poly_)
        ret_pol = Polynomial()
        ret_pol.power = [i for i in range(term1.power[0], -1, -1)]
        ret_pol.coefficients = [None] * (term1.power[0] + 1)
        j = 0
        for i in ret_pol.power:
            if term1.power.__contains__(i) and term2.power.__contains__(i):
                a = term1.coefficients[term1.power.index(i)] + term2.coefficients[term2.power.index(i)]
                ret_pol.coefficients[j] = a if a != 0 else None
            elif int(term1.power.__contains__(i)) + int(term2.power.__contains__(i)) == 1:
                ret_pol.coefficients[j] = term1.coefficients[term1.power.index(i)] if term1.power.__contains__(i) \
                    else term2.coefficients[term2.power.index(i)]
            else:
                ret_pol.coefficients[j] = None
            j += 1
        while ret_pol.coefficients.count(None) > 0:
            ret_pol.power.pop(ret_pol.coefficients.index(None))
            ret_pol.coefficients.remove(None)
        return ret_pol  # The polynomial is returned as an object of class Polynomial

    def pol_subtract(self, poly_):  # Function that converts each term to it's opposite sign then subtracts
        ret_pol = deepcopy(poly_)
        for i in range(len(poly_.coefficients)):
            ret_pol.coefficients[i] = - ret_pol.coefficients[i]
        return self.pol_add(ret_pol)

    def pol_multiplication(self, mul):  # Function to multiply two polynomial terms
        ret_pol = ""
        for i in range(len(mul.power)):
            temp_polynomial = deepcopy(self)
            for j in range(len(self.power)):
                temp_polynomial.power[j] += mul.power[i]
                temp_polynomial.coefficients[j] *= mul.coefficients[i]
            ret_pol = temp_polynomial.pol_add(ret_pol) if ret_pol else temp_polynomial
        return ret_pol  # Returned as object of class Polynomial

    # DeepCopy of dividend is required while calling this function, the quotient sent needs to be an empty Polynomial
    # object
    def pol_div(self, dividend, quotient):  # Function to divide two polynomial terms
        mul = self.find_num(dividend) if dividend.power else dividend
        if not quotient.power and mul.power:
            quotient = mul
        elif mul.power:
            quotient = quotient.pol_add(mul)
        else:
            return quotient, dividend  # Base case
        dividend.power.pop(0)
        dividend.coefficients.pop(0)  # Popping the first position because it will be removed during subtraction and to
        # avoid errors because python calculations with e causes errors in subtraction in some cases
        subtract = deepcopy(self.pol_multiplication(mul))
        subtract.coefficients.pop(0)
        subtract.power.pop(0)
        if dividend.power and subtract.power:
            dividend = dividend.pol_subtract(subtract)
        else:
            if (not dividend.power and not subtract.power) or (dividend.power and not subtract.power):
                dividend = dividend
            else:
                dividend = Polynomial("+0x^0").pol_subtract(subtract)
        return self.pol_div(dividend, quotient)  # Returns quotient and remainder as objects of class Polynomial

    def find_num(self, dividend):  # Function to find the quotient for the division function above
        term = Polynomial()
        if dividend.power[0] >= self.power[0]:
            term.coefficients = [dividend.coefficients[0] / self.coefficients[0]]
            term.power = [dividend.power[0] - self.power[0]]
        return term  # returns term to multiply by as object of class polynomial

    def string_convert(self):  # Converts Polynomial object to a string
        p_string = str(self.coefficients[0])
        p_string += "x^" + str(self.power[0]) + " " if self.power[0] > 1 else "x " if self.power[0] == 1 else ""
        if len(self.coefficients) > 1:
            for i in range(1, len(self.coefficients)):
                p_string += "+ " + str(self.coefficients[i]) if self.coefficients[i] > 0 else "- " + str(
                    str(self.coefficients[i])[1:])
                p_string += "x^" + str(self.power[i]) if self.power[i] > 1 else "x" if self.power[i] == 1 else ""
                p_string += " "
        return p_string  # Term is returned as string

    def pol_gcd_and_extended_euclid(self, dividend):  # Function that controls gcd and the extended euclidean functions
        lis = []
        lis2 = []
        divisor = deepcopy(self)
        lis = divisor.pol_gcd(deepcopy(dividend), lis)
        j = len(lis)
        if j == 1:  # If this is the case, then the divisor is itself GCD
            lis2 += [
                {"poly_1": Polynomial("+1x^0"), "dividend": lis[0]["dividend"], "divisor": lis[0]["divisor"],
                 "poly_2": lis[0]["divisor"].pol_div
                 (Polynomial("+0x^0").pol_subtract(lis[0]["dividend"].pol_subtract(lis[0]["divisor"])), Polynomial())}]
        else:
            lis2 = [
                {"poly_1": Polynomial("+1x^0"), "dividend": lis[j - 2]["dividend"], "divisor": lis[j - 2]["divisor"],
                 "poly_2": Polynomial("+0x^0").pol_subtract(lis[j - 2]["quotient"])}]
            if j >= 2:
                lis2 = extended_euclid(lis, lis2, j - 3)
        return lis, lis2

    def pol_gcd(self, dividend, lis):
        if not self.power:
            return lis
        else:
            quotient, remainder = self.pol_div(deepcopy(dividend), Polynomial())
            lis.append({"dividend": dividend, "divisor": self, "quotient": quotient,
                        "remainder": remainder if remainder.power else Polynomial("+0x^0")})
            return remainder.pol_gcd(deepcopy(self), lis)

    def get_coe_pow(self):  # Getter function
        return deepcopy(self.coefficients), deepcopy(self.power)


def extended_euclid(lis, lis2, j):  # Function to find the Bezout's coefficients using extended euclidean method
    if j == -1:
        return lis2
    poly_1 = Polynomial("+1x^0")
    poly_2 = Polynomial("+0x^0").pol_subtract(lis[j]["quotient"])
    lst_poly_1 = lis2[j]["poly_1"]
    lst_poly_2 = lis2[j]["poly_2"]
    poly_1 = poly_1.pol_multiplication(lst_poly_2)
    poly_2 = lst_poly_1.pol_add(poly_2.pol_multiplication(lst_poly_2))
    lis2 += [{"poly_1": poly_1, "poly_2": poly_2, "divisor": lis[j]["divisor"], "dividend": lis[j]["dividend"]}]
    return extended_euclid(lis, lis2, j - 1)


# The function given below returns string polynomial with a proper structure with each term separated
def polynomial_breakup(polynomial):
    polynomial = polynomial.replace(" ", "")  # Removing spaces from the string
    j = 0
    terms_of_polynomial = []
    if ord(polynomial[0]) > 45:
        polynomial = "+" + polynomial
    polynomial += "+"
    for i in range(1, len(polynomial)):
        if polynomial[i] == "+" or polynomial[i] == "-":
            terms_of_polynomial.append(term_structure(polynomial[j:i]))
            j = i
    return terms_of_polynomial


def term_structure(term):  # Function that makes each term of polynomial have proper structure
    if term.find('x') != -1:
        term = term[0] + "1" + term[term.find('x'):] if term.find('x') == 1 else term
        term = term + "^1" if term.find('^') == -1 else term
    else:
        term = term + "x^0"
    return term  # Term is returned as a string


def backend_control(root, frame, canvas, dividend, divisor):
    dividend = Polynomial(dividend)
    divisor = Polynomial(divisor)
    lis, lis2 = divisor.pol_gcd_and_extended_euclid(dividend)
    for i in lis:
        root.dis_div(i["dividend"].string_convert() + " = (" + i["divisor"].string_convert() + ") * ("
                     + i["quotient"].string_convert() + ") + (" + i["remainder"].string_convert() + ")", canvas)
        root.frame_line_display += 10
    root.frame_line_display += 50
    canvas.create_text(50, root.frame_line_display, font=("Cambria Math", 14, "italic"), fill="black",
                       text="Hence, the GCD is: " + lis[len(lis) - 1]["divisor"].string_convert(), anchor=NW)
    root.frame_line_display += 150
    canvas.create_text(500, root.frame_line_display, font=("Comic Sans MS", 18, "bold italic underline"),
                       fill="darkcyan", text="Calculating Bezout's Coefficients")
    canvas.update()
    gcd = lis[len(lis) - 1]["divisor"].string_convert()
    for i in lis2:
        st = gcd + " = (" + i["dividend"].string_convert() + ") * (" + i["poly_1"].string_convert() + ") + (" \
             + i["poly_2"].string_convert() + ") * (" + i["divisor"].string_convert() + ")"
        root.dis_bez(canvas, st)
        root.frame_line_display += 10

    root.frame_line_display += 50
    canvas.create_text(50, root.frame_line_display, font=("Cambria Math", 14, "italic"), fill="black",
                       text="Hence, the Bezout's Coeffiecients, a(x) and b(x) are: ", anchor=NW)
    root.frame_line_display += 25
    canvas.create_text(50, root.frame_line_display, font=("Cambria Math", 14, "normal"), fill="black",
                       text="a(x) = "+lis2[len(lis2)-1]["poly_1"].string_convert(), anchor=NW)
    root.frame_line_display += 25
    canvas.create_text(50, root.frame_line_display, font=("Cambria Math", 14, "normal"), fill="black",
                       text="b(x) ="+lis2[len(lis2)-1]['poly_2'].string_convert(), anchor=NW)
    canvas.update()
    root.restart(frame)


def main():
    root = Tk()
    app = Display(root)
    app.root.mainloop()


if __name__ == '__main__':
    main()
