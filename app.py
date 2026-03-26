import streamlit as st

# Page config
st.set_page_config(page_title="Cute Bank App 💖", page_icon="🏦", layout="wide")

# Custom CSS (for cute UI)
st.markdown("""
<style>
.main {
    background-color: #fdf6f9;
}
.stButton>button {
    background-color: #ff85a2;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# ------------------ CLASS ------------------
class BankApplication:
    bank_name = 'SBI 💙'

    def __init__(self, name, account_num, age, mob_num, balance):
        self.name = name
        self.account_num = account_num
        self.age = age
        self.mob_num = mob_num
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"✅ Withdrawn ₹{amount}"
        return "❌ Insufficient balance"

    def deposit(self, amount):
        self.balance += amount
        return f"💰 Deposited ₹{amount}"

    def update_mob_num(self, new_num):
        self.mob_num = new_num
        return "📱 Mobile updated!"

    def check_balance(self):
        return f"💵 Balance: ₹{self.balance}"


# ------------------ SESSION ------------------
if "account" not in st.session_state:
    st.session_state.account = None


# ------------------ SIDEBAR ------------------
st.sidebar.title("🏦 Cute Bank Menu")
menu = st.sidebar.radio("Choose option", 
                       ["Create Account", "Dashboard"])

# ------------------ CREATE ACCOUNT ------------------
if menu == "Create Account":
    st.title("✨ Create Your Account")

    name = st.text_input("👤 Name")
    acc = st.text_input("🔢 Account Number")
    age = st.number_input("🎂 Age", min_value=1)
    mob = st.text_input("📱 Mobile Number")
    bal = st.number_input("💰 Initial Balance", min_value=0)

    if st.button("💖 Create Account"):
        st.session_state.account = BankApplication(name, acc, age, mob, bal)
        st.success("🎉 Account created successfully!")


# ------------------ DASHBOARD ------------------
elif menu == "Dashboard":

    if st.session_state.account:
        user = st.session_state.account

        st.title(f"👋 Welcome {user.name}")

        # Cards
        col1, col2, col3 = st.columns(3)

        col1.metric("💵 Balance", f"₹{user.balance}")
        col2.metric("📱 Mobile", user.mob_num)
        col3.metric("🏦 Bank", user.bank_name)

        st.divider()

        option = st.selectbox("⚙️ Choose Action",
                             ["Deposit", "Withdraw", "Update Mobile", "Check Balance"])

        if option == "Deposit":
            amt = st.number_input("Enter amount", min_value=0)
            if st.button("💰 Deposit"):
                st.success(user.deposit(amt))

        elif option == "Withdraw":
            amt = st.number_input("Enter amount", min_value=0)
            if st.button("💸 Withdraw"):
                st.warning(user.withdraw(amt))

        elif option == "Update Mobile":
            new_mob = st.text_input("Enter new number")
            if st.button("📱 Update"):
                st.success(user.update_mob_num(new_mob))

        elif option == "Check Balance":
            if st.button("🔍 Check"):
                st.info(user.check_balance())

    else:
        st.warning("⚠️ Please create an account first!")
        