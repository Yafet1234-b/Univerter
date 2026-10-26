from flask import Flask, render_template, request

#importing the necessary tools

app = Flask(__name__)
# I am not really speaking to the randomness
# Frontend and Backend Integration
# i am still working to make it functional yet unable to do so 

Length_Units = ["meter","kilometer","centimeter","inches","yard","feet"]
@app.route('/', methods=['POST', 'GET'])

def home():
    return render_template('index.html')

@app.route('/final', methods=['GET', 'POST'])

def Get_Info():
    if request.method == "POST":
                try:
                    Magni = float(request.form.get("Magnitude"))
                    First_Unit = request.form.get("Input_2")
                    Second_Unit = request.form.get("Input_3")

                    if First_Unit not in Length_Units or Second_Unit not in Length_Units:
                        raise ValueError("Please enter one of the specified units for both the first and the second units")
                    else:
                        def Feet_Converter(x, y):
                            meter = 3.28084
                            kilometer = 3280.84
                            centimeter = 0.0328084
                            inches = 3
                            yard = 1/3
                            conversions = {"meter":meter,"inch":inches,"centimeter":centimeter,"kilometer":kilometer,"yard":yard}
                            return(conversions[x]*y)
                        def Meter_Converter(x,y):
                            feet = 3.280084
                            return(Feet_Converter(x,y)*feet)
                        def Yard_Converter(x,y):
                            feet = 1/3
                            return(Feet_Converter(x, y)*feet)
                        def Centimeter_Converter(x,y):
                            feet = 1/0.0328084
                            return(Feet_Converter(x, y)*feet)
                        def Kilometer_Converter(x,y):
                            feet = 1/3280.84 
                            return(Feet_Converter(x, y)*feet)
                        def Inches_Converter(x,y):
                            feet = 12
                            return(Feet_Converter(x, y)*feet)
                        def Length_Conversion(x, y):
                            if x == Second_Unit:
                                return(str(Meter_Converter(x, y)) + " " + x)
                            elif Second_Unit == "feet":
                                return(str(Feet_Converter(x, y)) + " " + Second_Unit)
                            elif Second_Unit == "inch":
                                return(str(Inches_Converter(x, y)) + " " + Second_Unit)
                            elif Second_Unit == "yard":
                                return(str(Yard_Converter(x, y)) + " " + Second_Unit)
                            elif Second_Unit == "centimeter":
                                return(str(Centimeter_Converter(x, y)) + " " + Second_Unit)
                            elif Second_Unit == "kilometer":
                                return(str(Kilometer_Converter(x, y)) + " " + Second_Unit)
                            else:
                                return(" None ")
                        result = Length_Conversion(First_Unit, Magni)
                        return render_template('index.html', result = result)
                except(ValueError, TypeError):
                        return render_template('index.html', result = "Please enter valid values")
                return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
