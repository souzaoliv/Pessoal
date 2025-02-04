from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]
        widgets = {
            "file": forms.ClearableFileInput(attrs={"class": "form-control", "accept": ".txt, .csv"}),
        }
        labels = {
            "file": "Selecione um arquivo (TXT ou CSV):",
        }

    # Validação personalizada para verificar o formato do arquivo
    def clean_file(self):
        uploaded_file = self.cleaned_data.get("file")
        if uploaded_file:
            if not uploaded_file.name.endswith(".txt") and not uploaded_file.name.endswith(".csv"):
                raise forms.ValidationError("Somente arquivos .txt ou .csv são permitidos.")
        return uploaded_file
