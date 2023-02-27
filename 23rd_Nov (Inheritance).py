# ----- Pillars of OOP ------ #

# 1. Inheritance
# 2. Polymorphism
# 3. Abstraction
# 4. Encasulation

#1. Inheritance -

# A. Single Level Inheritance

class Parent :
    def property (self) :
        l1 = ["car","Farm","Bunglow"]
        print(f"These are Parents Property {l1}")

class Child (Parent) :
    def prop (self) :
        l2 = ["Bike"]
        print(f"These are Child properties {l2}")
    
Rushi = Child ()
Rushi.property
Rushi.prop

# **************************************************************************************

# B. Multi Level Inheritance

class GP :
    def prop1 (self) :
        p1 = ["Shop","Land","Fame"]
        print(f"These are Grand Parent's Property {p1}")

class P (GP) :
    def prop2 (self) :
        p2 = ["Car","Bike","Bunglow"]
        print(f"These are Parent's Property {p2}")
        
class C (P) :
    def prop3 (self) :
        p3 = ["Cash"]
        print(f"These are child's Property {p3}")
        
Rushi = C ()
Rushi.prop1 ()
Rushi.prop2 ()
Rushi.prop3 ()


# ****************************************************************************************


# C. Multiple Level Inheritance

class Grand_M :
    def prop1 (self) :
        p1 = ["Gold"]
        print(f"These are Grand Mother's Property {p1}")

class Grand_F :
    def prop2 (self) :
        p2 = ["Shop"]
        print(f"These are Grand Father's Property {p2}")
        
class Parent (Grand_M,Grand_F) :
    def prop3 (self) :
        p3 = ["Shares"]
        print(f"These are Parents Property {p3}")

Mohan = Parent ()
Mohan.prop1 ()
Mohan.prop2 ()
Mohan.prop3 ()

# ***************************************************************************************************


# D. Hirarchicial Level Inheritance

class Parent :
    def prop1 (self) :
        p1 = ["Shares","Home","Land"]
        print(f"These are Parents Property {p1}")
        
class Child1 (Parent) :
    def prop2 (self) :
        p2 = ["Bike"]
        print(f"These are Child1 Properties {p2}")
        
class Child2 (Parent) :
    def prop3 (self) :
        p3 = ["car"]
        print(f"These are Child2 Property {p3}")
        
Rushi = Child1 ()
Rushi.prop1 ()
Rushi.prop2 ()

Shantanu = Child2 ()
Shantanu.prop1 ()
Shantanu.prop3 ()



# ***********************************************************************************************

# E. Hybrid Level Inheritance

class Mahadev :
    def prop1 (self) :
        p1 = ["Gold"]
        print(f"These are Mahadev's Property {p1}")

class Ganpat (Mahadev) :
    def prop2 (self) :
        p2 = ["Shop"]
        print(f"These are Ganpat's Property {p2}")
        
class Sindhu (Ganpat,Mahadev) :
    def prop3 (self) :
        p3 = ["Silver"]
        print(f"These are Sindhu's Property {p3}")
        
class Mohan (Sindhu) :
    def prop4 (self) :
        p4 = ["Shares","Home","Land"]
        print(f"These are Mohan's Property {p4}")
        
class Kailas (Sindhu) :
    def prop5 (self) :
        p5 = ["LIC","Car"]
        print(f"These are Kailas's Properties {p5}")
        
class Vandana (Mohan) :
    def prop6 (self) :
        p6 = ["Gold","Cash"]
        print(f"These are Vandana's Property {p6}")
        
class Lalita (Kailas) :
    def prop7 (self) :
        p7 = ["Cash"]
        print(f"These are Lalita's Property {p7}")
        
V = Vandana ()
V.prop1 ()
V.prop2 ()
V.prop3 ()
V.prop4 ()
V.prop6 ()

L = Lalita ()
L.prop1 ()
L.prop2 ()
L.prop3 ()
L.prop7 ()