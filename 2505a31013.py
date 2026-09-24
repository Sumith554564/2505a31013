import streamlit as st
import math

st.set_page_config(page_title="Mechanical Engineering Calculator", layout="centered")

st.title("⚙️ Complete Mechanical Engineering Calculator")
st.write("Select a module from the sidebar, enter your parameters with units, and instantly view calculated outcomes.")

# Sidebar Navigation for modules
st.sidebar.header("Modules")
module = st.sidebar.selectbox(
    "Choose a Category:",
    [
        "1. Mechanics",
        "2. Strength of Materials",
        "3. Thermodynamics",
        "4. Fluid Mechanics",
        "5. Thermal Engineering",
        "6. Machine Design",
        "7. Unit Conversion"
    ]
)

# ==========================================
# 1. MECHANICS
# ==========================================
if module == "1. Mechanics":
    st.header("1. Mechanics Module")
    calc_type = st.selectbox("Select Calculation", ["Force", "Work", "Power", "Kinetic Energy"])
    
    if calc_type == "Force":
        st.latex("F = m \\times a")
        m = st.number_input("Enter mass [Unit: kg]", min_value=0.0, value=1.0)
        a = st.number_input("Enter acceleration [Unit: m/s^2]", value=9.81)
        if st.button("Calculate"):
            result = m * a
            st.success(f"Result: Force = **{result:.4f} N** (Newtons)")

    elif calc_type == "Work":
        st.latex("W = F \\times d \\times \\cos(\\theta)")
        f = st.number_input("Enter force [Unit: N]", min_value=0.0, value=1.0)
        d = st.number_input("Enter distance [Unit: m]", min_value=0.0, value=1.0)
        angle = st.number_input("Enter angle theta [Unit: degrees]", value=0.0)
        if st.button("Calculate"):
            result = f * d * math.cos(math.radians(angle))
            st.success(f"Result: Work = **{result:.4f} J** (Joules)")

    elif calc_type == "Power":
        st.latex("P = \\frac{W}{t}")
        w = st.number_input("Enter work done or energy [Unit: J]", min_value=0.0, value=1.0)
        t = st.number_input("Enter time [Unit: s]", min_value=0.001, value=1.0)
        if st.button("Calculate"):
            result = w / t
            st.success(f"Result: Power = **{result:.4f} W** (Watts)")

    elif calc_type == "Kinetic Energy":
        st.latex("KE = \\frac{1}{2} m v^2")
        m = st.number_input("Enter mass [Unit: kg]", min_value=0.0, value=1.0)
        v = st.number_input("Enter velocity [Unit: m/s]", min_value=0.0, value=1.0)
        if st.button("Calculate"):
            result = 0.5 * m * (v ** 2)
            st.success(f"Result: Kinetic Energy = **{result:.4f} J** (Joules)")

# ==========================================
# 2. STRENGTH OF MATERIALS
# ==========================================
elif module == "2. Strength of Materials":
    st.header("2. Strength of Materials Module")
    calc_type = st.selectbox("Select Calculation", ["Stress", "Strain", "Young's Modulus"])
    
    if calc_type == "Stress":
        st.latex("\\sigma = \\frac{F}{A}")
        f = st.number_input("Enter applied force [Unit: N]", min_value=0.0, value=1.0)
        a = st.number_input("Enter cross-sectional area [Unit: m^2]", min_value=0.0001, value=1.0)
        if st.button("Calculate"):
            result = f / a
            st.success(f"Result: Stress = **{result:.4f} Pa** (Pascals or N/m^2)")

    elif calc_type == "Strain":
        st.latex("\\epsilon = \\frac{\\Delta L}{L_0}")
        dl = st.number_input("Enter change in length (delta L) [Unit: m]", value=0.0)
        l0 = st.number_input("Enter original length (L_0) [Unit: m]", min_value=0.0001, value=1.0)
        if st.button("Calculate"):
            result = dl / l0
            st.success(f"Result: Strain = **{result:.6f}** (Dimensionless)")

    elif calc_type == "Young's Modulus":
        st.latex("E = \\frac{\\text{Stress}}{\\text{Strain}}")
        stress = st.number_input("Enter stress [Unit: Pa]", min_value=0.0, value=1.0)
        strain = st.number_input("Enter strain [Dimensionless]", min_value=0.000001, value=0.01)
        if st.button("Calculate"):
            result = stress / strain
            st.success(f"Result: Young's Modulus = **{result:.4f} Pa** (Pascals)")

# ==========================================
# 3. THERMODYNAMICS
# ==========================================
elif module == "3. Thermodynamics":
    st.header("3. Thermodynamics Module")
    calc_type = st.selectbox("Select Calculation", ["Heat Transfer", "Work Done", "Thermal Efficiency"])
    
    if calc_type == "Heat Transfer":
        st.latex("Q = m \\times c \\times \\Delta T")
        m = st.number_input("Enter mass [Unit: kg]", min_value=0.0, value=1.0)
        c = st.number_input("Enter specific heat capacity [Unit: J/kg*K]", min_value=0.0, value=1000.0)
        dt = st.number_input("Enter change in temperature (delta T) [Unit: K or °C]", value=1.0)
        if st.button("Calculate"):
            result = m * c * dt
            st.success(f"Result: Heat Transfer (Q) = **{result:.4f} J** (Joules)")

    elif calc_type == "Work Done":
        st.latex("W = P \\times \\Delta V")
        p = st.number_input("Enter pressure [Unit: Pa]", min_value=0.0, value=1000.0)
        dv = st.number_input("Enter change in volume (delta V) [Unit: m^3]", value=1.0)
        if st.button("Calculate"):
            result = p * dv
            st.success(f"Result: Work Done = **{result:.4f} J** (Joules)")

    elif calc_type == "Thermal Efficiency":
        st.latex("\\eta = \\frac{W_{\\text{out}}}{Q_{\\text{in}}}")
        w_out = st.number_input("Enter useful work output [Unit: J]", min_value=0.0, value=1.0)
        q_in = st.number_input("Enter heat input [Unit: J]", min_value=0.001, value=1.0)
        if st.button("Calculate"):
            result = (w_out / q_in) * 100
            st.success(f"Result: Thermal Efficiency = **{result:.2f} %**")

# ==========================================
# 4. FLUID MECHANICS
# ==========================================
elif module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics Module")
    calc_type = st.selectbox("Select Calculation", ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"])
    
    if calc_type == "Pressure":
        st.latex("P = \\rho \\times g \\times h")
        rho = st.number_input("Enter fluid density [Unit: kg/m^3]", min_value=0.0, value=1000.0)
        g = st.number_input("Enter gravity [Unit: m/s^2]", min_value=0.0, value=9.81)
        h = st.number_input("Enter height/depth [Unit: m]", min_value=0.0, value=1.0)
        if st.button("Calculate"):
            result = rho * g * h
            st.success(f"Result: Pressure = **{result:.4f} Pa** (Pascals)")

    elif calc_type == "Reynolds Number":
        st.latex("Re = \\frac{\\rho \\times v \\times D}{\\mu}")
        rho = st.number_input("Enter density [Unit: kg/m^3]", min_value=0.0, value=1000.0)
        v = st.number_input("Enter flow velocity [Unit: m/s]", min_value=0.0, value=1.0)
        d = st.number_input("Enter diameter [Unit: m]", min_value=0.0001, value=0.1)
        mu = st.number_input("Enter dynamic viscosity [Unit: Pa*s]", min_value=0.000001, value=0.001)
        if st.button("Calculate"):
            result = (rho * v * d) / mu
            st.success(f"Result: Reynolds Number = **{result:.4f}** (Dimensionless)")

    elif calc_type == "Flow Velocity":
        st.latex("v = \\frac{Q}{A}")
        q = st.number_input("Enter discharge rate [Unit: m^3/s]", min_value=0.0, value=1.0)
        a = st.number_input("Enter cross-sectional area [Unit: m^2]", min_value=0.0001, value=1.0)
        if st.button("Calculate"):
            result = q / a
            st.success(f"Result: Flow Velocity = **{result:.4f} m/s**")

    elif calc_type == "Discharge":
        st.latex("Q = A \\times v")
        a = st.number_input("Enter cross-sectional area [Unit: m^2]", min_value=0.0, value=1.0)
        v = st.number_input("Enter flow velocity [Unit: m/s]", min_value=0.0, value=1.0)
        if st.button("Calculate"):
            result = a * v
            st.success(f"Result: Discharge = **{result:.4f} m^3/s**")

# ==========================================
# 5. THERMAL ENGINEERING
# ==========================================
elif module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering Module")
    calc_type = st.selectbox("Select Calculation", ["Heat Conduction", "COP", "Heat-Engine Efficiency"])
    
    if calc_type == "Heat Conduction":
        st.latex("Q = \\frac{k \\times A \\times \\Delta T}{L}")
        k = st.number_input("Enter thermal conductivity [Unit: W/m*K]", min_value=0.0, value=1.0)
        a = st.number_input("Enter surface area [Unit: m^2]", min_value=0.0, value=1.0)
        dt = st.number_input("Enter temperature difference [Unit: K or °C]", value=1.0)
        l = st.number_input("Enter thickness/length [Unit: m]", min_value=0.0001, value=0.1)
        if st.button("Calculate"):
            result = (k * a * dt) / l
            st.success(f"Result: Heat Conduction Rate = **{result:.4f} W** (Watts)")

    elif calc_type == "COP":
        st.latex("COP = \\frac{\\text{Desired Output}}{\\text{Work Input}}")
        desired = st.number_input("Enter desired output energy/cooling effect [Unit: J or W]", min_value=0.0, value=1.0)
        work_in = st.number_input("Enter work input [Unit: J or W]", min_value=0.001, value=1.0)
        if st.button("Calculate"):
            result = desired / work_in
            st.success(f"Result: COP = **{result:.4f}** (Dimensionless)")

    elif calc_type == "Heat-Engine Efficiency":
        st.latex("\\eta = \\left(1 - \\frac{Q_{\\text{out}}}{Q_{\\text{in}}}\\right) \\times 100")
        q_out = st.number_input("Enter heat rejected (Q_out) [Unit: J]", min_value=0.0, value=1.0)
        q_in = st.number_input("Enter heat supplied (Q_in) [Unit: J]", min_value=0.001, value=2.0)
        if st.button("Calculate"):
            result = (1 - (q_out / q_in)) * 100
            st.success(f"Result: Heat-Engine Efficiency = **{result:.2f} %**")

# ==========================================
# 6. MACHINE DESIGN
# ==========================================
elif module == "6. Machine Design":
    st.header("6. Machine Design Module")
    calc_type = st.selectbox("Select Calculation", ["Torque", "Shaft Power", "Shaft Diameter"])
    
    if calc_type == "Torque":
        st.latex("T = F \\times r")
        f = st.number_input("Enter force applied [Unit: N]", min_value=0.0, value=1.0)
        r = st.number_input("Enter radius/moment arm [Unit: m]", min_value=0.0, value=1.0)
        if st.button("Calculate"):
            result = f * r
            st.success(f"Result: Torque = **{result:.4f} N*m** (Newton-meters)")

    elif calc_type == "Shaft Power":
        st.latex("P = \\frac{2 \\pi N T}{60}")
        n_rpm = st.number_input("Enter rotational speed [Unit: RPM]", min_value=0.0, value=1000.0)
        t = st.number_input("Enter torque [Unit: N*m]", min_value=0.0, value=10.0)
        if st.button("Calculate"):
            result = (2 * math.pi * n_rpm * t) / 60
            st.success(f"Result: Shaft Power = **{result:.4f} W** (Watts)")

    elif calc_type == "Shaft Diameter":
        st.latex("d = \\sqrt[3]{\\frac{16 T}{\\pi \\tau}}")
        t = st.number_input("Enter applied torque [Unit: N*m]", min_value=0.0, value=100.0)
        tau = st.number_input("Enter allowable shear stress [Unit: Pa]", min_value=0.001, value=50000000.0)
        if st.button("Calculate"):
            d = ((16 * t) / (math.pi * tau)) ** (1/3)
            st.success(f"Result: Required Shaft Diameter = **{d:.4f} m** ({d*1000:.2f} mm)")

# ==========================================
# 7. UNIT CONVERSION
# ==========================================
elif module == "7. Unit Conversion":
    st.header("7. Unit Conversion Module")
    conv_type = st.selectbox("Select Type", ["Length", "Pressure", "Temperature"])
    
    if conv_type == "Length":
        sub = st.selectbox("Conversion", ["Meters to Feet", "Feet to Meters", "Millimeters to Inches", "Inches to Millimeters"])
        val = st.number_input("Enter value to convert", value=1.0)
        if st.button("Convert"):
            if sub == "Meters to Feet": st.success(f"{val} m = **{val * 3.28084:.4f} ft**")
            elif sub == "Feet to Meters": st.success(f"{val} ft = **{val / 3.28084:.4f} m**")
            elif sub == "Millimeters to Inches": st.success(f"{val} mm = **{val / 25.4:.4f} in**")
            elif sub == "Inches to Millimeters": st.success(f"{val} in = **{val * 25.4:.4f} mm**")

    elif conv_type == "Pressure":
        sub = st.selectbox("Conversion", ["Pascals to psi", "psi to Pascals", "Bar to Pascals", "Pascals to Bar"])
        val = st.number_input("Enter value to convert", value=1.0)
        if st.button("Convert"):
            if sub == "Pascals to psi": st.success(f"{val} Pa = **{val / 6894.76:.4f} psi**")
            elif sub == "psi to Pascals": st.success(f"{val} psi = **{val * 6894.76:.4f} Pa**")
            elif sub == "Bar to Pascals": st.success(f"{val} bar = **{val * 100000:.4f} Pa**")
            elif sub == "Pascals to Bar": st.success(f"{val} Pa = **{val / 100000:.4f} bar**")

    elif conv_type == "Temperature":
        sub = st.selectbox("Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
        val = st.number_input("Enter value to convert", value=0.0)
        if st.button("Convert"):
            if sub == "Celsius to Fahrenheit": st.success(f"{val} °C = **{(val * 9/5) + 32:.4f} °F**")
            elif sub == "Fahrenheit to Celsius": st.success(f"{val} °F = **{(val - 32) * 5/9:.4f} °C**")
            elif sub == "Celsius to Kelvin": st.success(f"{val} °C = **{val + 273.15:.4f} K**")
            elif sub == "Kelvin to Celsius": st.success(f"{val} K = **{val - 273.15:.4f} °C**")
Mechanical Engineering Calculator
