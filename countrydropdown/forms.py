from django.forms import ModelForm

from .models import CountrySelect


class CountrySelectCreateForm(ModelForm): # Comments added by Harsha from Integration team on Monday
    class Meta:
        model = CountrySelect
        fields = "__all__"

    def as_p(self, *args, **kwargs):
        del self.fields["location"]
        return super().as_p(*args, **kwargs)
