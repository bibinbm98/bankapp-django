from django import forms

class adduserform(forms.Form):
    firstname=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    lastname=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    username=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get("password")
        password2=cleaned_data.get("confirm_password")
        if password1 !=password2:
            msg="password mismatch"
            self.add_error("password",msg)

class loginform(forms.Form):
    username=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class createaccountform(forms.Form):
    accountnumber=forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    actype = forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    amount = forms.CharField(max_length=12,widget=forms.TextInput(attrs={"class":"form-control"}))
    def clean(self):
        cleaned_data=super().clean()
        amount=int(cleaned_data.get("amount"))
        acctype=cleaned_data.get("actype")
        if amount<2000:
            msg="invalid! minimum bal amount must be 2000"
            self.add_error("amount",msg)
        if acctype!="savings":
            msg="u r not able to open an account"
            self.add_error("actype",msg)