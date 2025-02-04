from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    MAX_FILE_SIZE = 0.01 * 1024 * 1024  # 

    class Meta:
        model = UploadedFile
        fields = ["file"]
        widgets = {
            "file": forms.ClearableFileInput(attrs={"class": "form-control", "accept": ".txt"}),
        }
        labels = {
            "file": "Selecione um arquivo (apenas TXT):",
        }

    def clean_file(self):
        uploaded_file = self.cleaned_data.get("file")

        if uploaded_file:
            # Verifica a extensão do arquivo (somente .txt)
            if not uploaded_file.name.endswith(".txt"):
                raise forms.ValidationError("Somente arquivos .txt são permitidos.")

            # Verifica se o arquivo realmente contém texto
            if not uploaded_file.content_type.startswith("text/"):
                raise forms.ValidationError("O arquivo precisa ser um arquivo de texto válido.")

            # Verifica o tamanho do arquivo
            if uploaded_file.size > self.MAX_FILE_SIZE:
                raise forms.ValidationError(f"O arquivo não pode exceder {self.MAX_FILE_SIZE / 1024:.0f} KB.")

        return uploaded_file
